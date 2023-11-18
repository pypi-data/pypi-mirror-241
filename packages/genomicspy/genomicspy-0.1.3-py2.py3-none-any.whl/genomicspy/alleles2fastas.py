"""CLI program to convert vcfs to fasta seqs using VCF"""

# Vivian Leung
# Created:      27 Aug 2023
# Last updated: 05 Oct 2023
# Last used:    05 Oct 2023

# Changelog:

# Note: requires ncpus + 1 threads
# Note that df.groupby.parallel_apply doesn't preserve group.name

# IMPORTANT: vcfpy is actually 1-indexed, left open
# GFF3 and VCF are 1-indexed, closed
# Making all start, end intervals 1-indexed, closed (consistent with GFF3, VCF)


# %%
# IMPORTS
from __future__ import annotations

import argparse
import gzip
import logging
import os
import pickle
import sys
from argparse import ArgumentError

import pandas as pd
import vcfpy

from Bio.AlignIO import MultipleSeqAlignment
from pandarallel import pandarallel

import oddsnends as oed

from genomicspy.Variants import MSAVariants, VCFVariants
from genomicspy.alleles.tools import (
    calc_circular,
    calc_end_pos,
    check_overlap,
)
from genomicspy.fasta import (
    SampleErrorHandlingType,
    parse_fasta_refs,
    write_outputs,
)
from genomicspy.main import SeqType
from genomicspy import gff3


# %% # USER PARAMS

# use as FA_FNAME_FMT.format(**kws)
# file root format (will add .fa on run)
FA_FNAME_FORMAT = (
    "{name}_{geneId}_{seqid}_{start:0{seqlen_pad}}_{end:0{seqlen_pad}}{suffix}"
)
# use as SEQ_ID_FORMAT.format(**kws). vars named per GFF3 (except sample and
# IDs as <gene,cds,exon,rna,other>ID)
# double-wrap sample as .format is done in two steps
# (the first for region/entry-specific info, and the second with 'sample')
# using gt_alias

SEQ_ID_FORMAT = "{{sample}}_{geneId}_{entry_name}_n_{{n_samples}}"

SEQ_NAME_FORMAT = "{{sample}}"

SEQ_DESCRIPTION_FORMAT = ""

# SEQ_DESCRIPTION_FORMAT = "{geneID}|{cdsID}|{seqid}|{start}-{end}|{strand}|{product}"

FASTA_COMMENT_FORMAT = None  # f"naming is {SEQ_ID_FORMAT} {SEQ_DESCRIPTION_FORMAT}"

##### Params #####

# %%
####  Functions  #####


def argparser() -> argparse.ArgumentParser:
    """Generates ArgumentParser for CLI"""
    parser = argparse.ArgumentParser(
        description="Generate fastas from VCF and optionally table of variants",
        formatter_class=oed.SmartFormatter,
        add_help=True,
    )

    parser.add_argument(
        "-f",
        "--fasta-ref ",
        required=True,
        dest="fasta_refs",
        action="append",
        type=lambda x: oed.argtype_filepath(parser, x),
        help="Reference fasta. Can use flag multiple times",
    )
    g_variants = parser.add_argument_group(
        "Input variants",
        "Must provide (1) --vcf or (2) --variants-msa and --variants-kws",
    )

    g_variants.add_argument(
        "-i",
        "--vcf",
        dest="vcf",
        type=lambda x: oed.argtype_filepath(parser, x),
        help="Input VCF filepath with GT",
    )

    g_variants.add_argument(
        "--variant-msas",
        dest="variant_msas",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=(
            "Pickle of pd.DataFrame containing CHROM, POS, MSA or ALLELE, "
            "(and optionally END_POS) with Bio.AlignIO.MultipleSeqAlignment "
            "objects. Seeparse_allele_msas.py. Variant POS (and END_POS ) "
            "must be 1-indexed closed/inclusive (consistent with VCF and GFF3"
            "). If given, --variant-gts must also be given. "
            "See parse_allele_msas.py"
        ),
    )

    g_variants.add_argument(
        "--variant-gts",
        dest="gt_file_lookup",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=(
            "Headerless TSV lookup with CHROM, START, END, and FPATH to region "
            "GTs pickled pd.DataFrame containing cols CHROM, POS "
            "REF, SAMPLE, GT (and other fields). See wrangle_gts.py or "
            "genomicspy.parse_gff3()"
        ),
    )

    g_variants.add_argument(
        "--variants-kws",
        dest="variants_kws",
        type=str,
        help="\n".join(
            [
                "R|semicolon-separated KEY=VALUE list for parsing variants. Options:",
                "- fields: comma-separated list of fields to extract",
                "- gt_i: int  (for multiplods) index in GT field. Default 0",
                "- indexing: int  Indexing of positions. Default 1 (1-indexing)",
                "- interval_type  How position intervals are closed. Options:",
                "       'lower', 'left'       : [l, u)",
                "       'upper', 'right'      : (l, u]",
                "       'closed', 'both', True: [l, u]",
                "       'open', False         : (l, u)",
                "  Default is 'closed'.",
                "- start_col:  label of (start) position column. Default 'POS'.",
                "- seq_col:    label of column with sequences. Default 'ALLELES'.",
            ]
        ),
    )

    parser.add_argument(
        "-O",
        "--out-dir",
        dest="out_dir",
        default=".",
        type=str,
        help="Output directory.",
    )
    parser.add_argument(
        "--suffix",
        dest="file_suffix",
        type=str,
        help="File suffix for output files (excluding extensions)",
    )

    parser.add_argument(
        "--tmp-dir",
        dest="tmp_dir",
        default="./tmp/",
        type=str,
        help="Temporary directory.",
    )
    parser.add_argument(
        "--save-interim",
        dest="save_interim",
        action="store_true",
        help="Save trimmed alleles and GTs as pickled DataFrames",
    )

    g_regions = parser.add_argument_group("GFF3 and region options")

    g_regions.add_argument(
        "-g",
        "--gff3",
        dest="ref_gff3",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=("Reference GFF3. seqids must correspond to " "CHROM in VCF"),
    )
    g_regions.add_argument(
        "-G",
        "--gff3-parsed",
        dest="parsed_gff3",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=(
            "Pre-processed GFF3 pkl pr tsv (from previous run). Also see "
            "genomicspy.gts_to_long() and genomicspy.consolidate_gff3()."
        ),
    )

    g_regions.add_argument(
        "--cds-only",
        dest="cds_only",
        action="store_true",
        help="Process only CDS (i.e. has cdsID).",
    )

    g_regions.add_argument(
        "--genes-only",
        dest="genes_only",
        action="store_true",
        help="Process only genes (i.e. has geneID).",
    )

    g_regions.add_argument(
        "--names",
        dest="names_list",
        type=str,
        help=(
            "comma-separated list of GFF3 entries by name "
            "to process. Must specify field to check using --names-field"
        ),
    )
    g_regions.add_argument(
        "--names-fpath",
        dest="names_fpath",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=(
            "File with list of GFF3 entries by name to process. Must specify "
            "field to check using --names-field"
        ),
    )

    g_regions.add_argument(
        "--regions",
        dest="regions_tsv",
        type=lambda x: oed.argtype_filepath(parser, x),
        help=(
            "(Headerless) GFF3-like TSV of regions with "
            f"{', '.join(gff3.GFF3_COLS)} "
            "and naming and annotation fields. If provided, --gff3 "
            "and --gff3-parsed args are ignored"
        ),
    )
    g_regions.add_argument(
        "--names-field",
        dest="names_field",
        type=str,
        help=(
            "GFF3 field or attriibute to check for names, if given. The ID "
            "attribute is parsed as <cds,gene,exon,rna,other>ID"
        ),
    )

    g_samples = parser.add_argument_group("Options for samples")

    g_samples.add_argument(
        "--samples",
        dest="samples_fpath",
        type=lambda x: oed.argtype_filepath(parser, x),
        help="File with list of samples to process",
    )

    # used in gen_fasta and write_fasta_seq
    g_samples.add_argument(
        "--error-sample",
        dest="errors_sample",
        choices=SampleErrorHandlingType.options,
        default="ignore",
        help=(
            "If sample is missing from GTs (VCF), ignore sample and warn "
            "('ignore'), assume it is same as refseq and generate fasta "
            "anyway ('force'). or raise error and exit ('raise'), "
            "Default 'ignore'"
        ),
    )

    g_other = parser.add_argument_group("Other processing options")

    g_other.add_argument(
        "--is-circular",
        dest="is_circular",
        action="store_true",
        help=(
            "Treat refseqs as circular. Important for "
            "checking for overlapping variants"
        ),
    )

    g_other.add_argument(
        "--ncpus",
        dest="ncpus",
        type=int,
        default=None,
        help=("Number of processes (for multiprocessing) " "Default single."),
    )

    g_other.add_argument(
        "-l",
        "--log-level",
        choices=["DEBUG", "INFO", "WARN", "ERROR"],
        default="INFO",
        dest="log_level",
        help="logging level",
    )

    g_other.add_argument(
        "--progress-bar",
        action="store_true",
        dest="progress_bar",
        help="Show progress bar(s)",
    )

    g_other.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
    )

    return parser


def init_logger(verbose: bool = False, **kws) -> None:
    """Initialize logger"""

    # get job number if parallel
    try:
        log_pseq = f" J{os.environ['PARALLEL_SEQ']} - "
    except KeyError:
        log_pseq = ""

    # date and logging format
    if verbose:
        log_datefmt = "%Y-%m-%d %H:%M:%S"
        logging_format = (
            f"%(asctime)s{log_pseq} %(levelname)s "
            "%(name)s - %(funcName)s: %(message)s"
        )
    else:
        log_datefmt = "%H:%M:%S"
        logging_format = (
            f"%(relativeCreated)d {log_pseq}" "%(name)s - %(funcName)s: %(message)s"
        )

    # config
    logging.basicConfig(format=logging_format, datefmt=log_datefmt, **kws)


def check_args(ns: argparse.Namespace) -> None:
    """Check input args, particularly I/O"""

    try:
        # input vcf
        oed.assertfile(ns.vcf, "--vcf")

        # Variant MSA pickled dataframe
        if oed.isnull(ns.variant_msas) and oed.isnull(ns.gt_file_lookup):
            pass
        else:
            oed.assertfile(ns.variant_msas, "--variant-msas", null="raise")
            oed.assertfile(ns.gt_file_lookup, "--variant-gts", null="raise")

        # Reference FASTA
        assert len(ns.fasta_refs) > 0, "No --fasta-ref given"
        for fa in ns.fasta_refs:
            oed.assertfile(fa, "--fasta-ref", null="raise")

        # Reference GFF3

        # Region coordinates to process
        oed.assertfile(ns.regions_tsv, "--regions")

        if ns.regions_tsv is None:
            assert oed.xor(oed.isnull(ns.ref_gff3), oed.isnull(ns.parsed_gff3)), (
                "--gff3|--gff3-parsed",
                "give exactly one if no --regions",
            )
            oed.assertfile(ns.ref_gff3, "--gff3")
            oed.assertfile(ns.parsed_gff3, "--gff3-parsed")

        # Samples to process
        oed.assertfile(ns.samples_fpath, "--samples-fpath")

        # Region names to process
        if not oed.isnull(ns.names_list):
            assert (
                ns.names_field is not None
            ), f"--names-field:required for --names {ns.names}"

        if not oed.isnull(ns.names_fpath):
            oed.assertfile(ns.names_fpath)
            assert ns.names_field is not None, (
                "--names-field",
                f"required for --names-fpath {ns.names_fpath}",
            )

    except AssertionError as error:
        raise ArgumentError(error.args[0], error.args[1]) from error

    except FileNotFoundError as error:
        raise ArgumentError(error.args[1], error.args[0]) from error

    # Check number of processes
    if ns.ncpus is not None:
        logging.info(
            "%d CPUs available. Specified %d for pandarallel.",
            os.environ.get("OMP_NUM_THREADS", os.cpu_count()),
            ns.ncpus,
        )


# %%


def gen_fasta(
    ser: pd.Series = None,
    refseqs: oed.SeriesType[str, SeqType, None] = None,
    vcf: str = None,
    variants_kws: dict = None,
    dirs: dict = None,
    is_circular: bool = False,
    formatters: dict = None,
    save_interim: bool = False,
    errors_sample: SampleErrorHandlingType = "ignore",
    **format_kws,
) -> None:
    """Generates fasta sequences for a given region (and samples)

    Start and end of intervals are 1-indexed, closed (GFF3 format). For
    example, a SNP at the first position has start of 1, end of 2.

    Parameters
    ==========
    Region specifiers
    -----------------
    ser:     pd.Series
        Specifies region to use, containing the seqid (chrom), start, end, and
        other fields. (Based on GFF3.)

    Note: chrom, start and end may be specified in lieu of or to override ser.
    See **format_kws for details.

    For alleles and genotypes (Variants)
    ------------------------------------------
    refseqs:     pd.Series. required.
        Contains index as CHROM, refseqs as SeqRecord or str. Required if
        alleles is None. Also used to get chrom length
    vcf:     str
        File path to vcf
    variants_kws: dict, optional. additional kws for Variants class. Takes:
        (in addition to chrom, start, end, name. See **format_kws below)
    - variant_msas:  pd.DataFrame, optional
        Contains CHROM, POS, END_POS, ALLELES[list[SeqType]. If given, this
        is used instead of variants in vcf.
    - gts_lookup:  pd.Series, optional
        Contains index SAMPLE, values as fpaths to pickled DataFrames with
        cols CHROM, POS, REF, SAMPLE, GT, ...
    - samples: list[str]
        Samples to process. Default None is all samples
    - gt_i: int, default 0
        Index of GT allele to use (for diploids or multiploids)
    - interval_type: str or bool or None.
        Interval notation. Passed to genomicspy.trim_alleles().
        See documentation. Default True
    - indexing, int, default 1
        indexing base number. default 1-indexed

    formatters: dict, optional
        - fname_fmt: str
            Formatter str for fasta filename. If None, fasta files are not
            written and retseq is set to True. Default "{seqid}_{start}_{end}"
        - seqrec_fmts: str
            See `genomicspy.write_outputs()` documentation

    Write outputs
    ---------------------------
    `seqrec_fmts`, `errors_sample`, `save_interim`, and `**format_kws`
    (including `ser` info, if `ser` is provided) are passed to
    genomicspy.write_outputs(). See documentation.

    Output options
    --------------
    dirs: dict. Takes:
        - fasta: str, required
        - alias: str, required if save_interim
        - msa: str, required if save_interim
        - variants: str, required if save_interim
        - xrefs: str, required if save_interim
        - tmp: str, optional. Default ./tmp


    **format_kws to specify region or other, or overrides ser (if given). Takes:
    -------------------
    - chrom:  str
        Chromosome/contig name to look up in VCF
    - start:  int
        start position of the 1-indexed right open interval
    - end:  int.
        end position of the 1-indexed closed interval
    - name:  str, oed.default ser.name or None
        Name for logging. Default inferred from ser (if given) or None.
    - names_field: str, default 'Name'
        if given, then use value in names_field of ser (unless 'name' is given).
    - suffix:  str
        File suffix (excluding extension)

    Returns
    -------
    None or Generator of sample SeqRecords
    """
    # augment format_kws with series info
    if ser is not None:
        format_kws = ser.to_dict() | format_kws

    # put together format_kws and get name
    if (ser is None) or "name" in format_kws:  # use explicitly given name
        entry_name = format_kws.get("name")

    elif format_kws.get("name_field") is not None:  # get ser field
        entry_name = ser[format_kws.pop("name_field")]
    else:
        entry_name = ser.name

    # add entry_name to dict for filling in format
    format_kws["entry_name"] = entry_name

    # rename seqid (GFF3 name for chrom) to chrom
    format_kws.setdefault("chrom", format_kws.get("seqid"))

    # kwargs for variants. Need to make a copy since we're poppin'...
    variants_kws = {} if variants_kws is None else variants_kws.copy()

    # read/generate alleles and genotypes
    vcf = variants_kws.pop("vcf", None)

    variant_msas = variants_kws.pop("variant_msas", None)
    gts_lookup = variants_kws.pop("gts_lookup", None)

    # set defaults for kws for init Variants objects
    variants_kws = {
        "refseq": refseqs[format_kws["chrom"]],
        "chrom": format_kws["chrom"],
        "start": format_kws["start"],
        "end": format_kws["end"],
        "name": entry_name,
        "strand": format_kws.get("strand", None),
    } | variants_kws

    if (variant_msas is None) and (gts_lookup is None):
        # read from VCF
        genotypes_kws = {
            "samples": variants_kws.pop("samples", None),
            "fields": variants_kws.pop("fields", None),
        }

        variants = VCFVariants(vcf=vcf, **variants_kws)
        variants.logger.debug("Reading alleles and genotypes from VCF")
        _ = variants.gen_alleles().gen_genotypes(**genotypes_kws)

    else:
        # read from MSA and genotype files
        variants = MSAVariants(**variants_kws)
        variants.logger.debug(
            "Reading alleles and genotypes from MSA and GT file lookup"
        )
        _ = (
            variants.filter_genotype_files(gt_files=gts_lookup)
            .gen_alleles(variant_msas=variant_msas)
            .gen_genotypes(**genotypes_kws)
        )

    # dedup/alias and trim inplace (default True)
    variants.logger.debug("Grouping, aliasing and trimming")

    _ = variants.alias_identical_gts().trim_alleles(update_pos=False, replace=True)

    if is_circular:
        which_span_break = (
            calc_circular(variants.end_pos, len(variants.refseq)) != variants.end_pos
        )

        if any(which_span_break):
            variants.logger.warning(
                "%d alleles span chrom break!", sum(which_span_break)
            )

    seqlen = len(variants.refseq)

    check_overlap(
        variants.alleles.reset_index(),
        variants.chrom,
        length=seqlen,
        is_circular=is_circular,
        errout=oed.defaults(
            dirs["main_out"], dirs["tmp"], os.environ.get("TMPDIR", "./")
        ),
    )

    fname = formatters.get("fname_fmt", "{chrom}_{start}_{end}").format(
        seqlen_pad=len(str(seqlen)), **format_kws
    )

    # outpaths
    fa_path = f"{dirs['fasta']}/{fname}.fa.gz"

    # series/entry/region-level annotations to add to each seq record
    annotations = {
        "entry_name": format_kws["entry_name"],
        "strand": ser["strand"],
        "geneId": ser["geneId"],
        "cdsId": ser["cdsId"],
    }

    variants.logger.debug("Processing variants for output")
    fasta_records = write_outputs(
        variants,
        fa_path,
        seqrec_fmts=formatters.get("seqrec_fmts", None),
        format_kws=format_kws,
        annotations=annotations,
        save_interim=save_interim,
        errors_sample=errors_sample,
    )

    # save other files

    sample_xref_tsv = f"{dirs['xrefs']}/{fname}.sample_alias.xref.tsv.gz"
    variants.logger.debug("Saving sample alias xref to %s", sample_xref_tsv)
    (
        variants.alias_crossrefs["SAMPLE"]
        .explode()
        .pipe(oed.swap_index)
        .to_csv(sample_xref_tsv, sep="\t")
    )

    if save_interim:
        variants.logger.debug("Saving interim files")

        # variants object
        with gzip.open(f"{dirs['variants']}/{fname}.variants.pkl.gz", "wb") as fout:
            pickle.dump(variants, fout)

        # gts
        variants.alias_crossrefs.to_pickle(
            f"{dirs['alias']}/{fname}.alias_xrefs.df.pkl.gz"
        )

        with gzip.open(f"{dirs['msa']}/{fname}.msa.pkl.gz", "wb") as msa_out:
            pickle.dump(
                MultipleSeqAlignment(fasta_records, annotations=format_kws), msa_out
            )

    variants.logger.info("Finished.")


def main(ns: argparse.Namespace):
    """Main function"""

    ### Initialize
    start_time = pd.Timestamp.now()

    # set up loggger
    init_logger(
        verbose=ns.verbose,
        level=getattr(logging, ns.log_level.upper(), None),
        stream=sys.stdout,
    )
    logger = logging.getLogger()
    logging.info("Start time: %s", oed.now())

    # pandarallel for parallel processing
    if ns.ncpus is not None:
        pandarallel.initialize(nb_workers=ns.ncpus, progress_bar=ns.progress_bar)

    ### Parse arguments

    # Check args, particularly I/O
    check_args(ns)

    fasta_refs = ns.fasta_refs

    # variants options
    vcf = ns.vcf
    variant_msas = ns.variant_msas
    gt_file_lookup = ns.gt_file_lookup
    samples_fpath = ns.samples_fpath

    ## Variants input options
    variants_kws = {}
    for kv in ns.variants_kws.split(";"):
        k, v = kv.split("=", maxsplit=1)
        variants_kws[k] = v.split(",") if k == "fields" else oed.parse_literal_eval(v)

    # set defaults
    variants_kws = {
        "vcf": vcf,
        "gt_i": 0,
        "interval_type": "closed",
        "indexing": 1,
        "start_col": "POS",
        "end_col": "END_POS",
        "seq_col": "ALLELES",
    } | variants_kws

    # output options
    out_dir = ns.out_dir
    tmp_dir = ns.tmp_dir
    save_interim = ns.save_interim

    dirs = {
        "main_out": f"{out_dir}",
        "tmp": tmp_dir,
        "fasta": f"{out_dir}/fasta",
    }
    if save_interim:
        dirs |= {
            "xrefs": f"{out_dir}/xrefs",
            "variants": f"{out_dir}/variants",
            "alias": f"{out_dir}/alias",
            "msa": f"{out_dir}/msa",
        }

    suffix = oed.default(
        oed.default(ns.file_suffix, os.environ.get("PARALLEL_SEQ", None)),
        "",
        lambda x: f".{x}",
    )

    # regions options
    ref_gff3 = ns.ref_gff3
    parsed_gff3 = ns.parsed_gff3
    regions_tsv = ns.regions_tsv

    cds_only = ns.cds_only
    genes_only = ns.genes_only
    names_fpath = ns.names_fpath
    names_list = oed.default(ns.names_list, "").split(",")
    names_field = ns.names_field

    # samples options
    samples_fpath = ns.samples_fpath
    errors_sample = ns.errors_sample

    # other options
    is_circular = ns.is_circular
    ncpus = ns.ncpus

    ## Process args

    for d in dirs.values():
        os.makedirs(d, exist_ok=True)

    # read in reference fasta
    logger.debug("Reading in reference fastas")
    refseqs = parse_fasta_refs(*fasta_refs)

    # get sample list (if provided)
    try:
        with open(samples_fpath, "r") as fin:
            logger.debug("Reading samples")
            samples = [el for el in (line.rstrip() for line in fin) if el != ""]

    except TypeError:
        if vcf is not None:
            with vcfpy.Reader.from_path(vcf) as reader:
                samples = reader.header.samples.names
    try:
        variants_kws["samples"] = samples
        logger.info("%d samples", len(samples))
    except NameError:
        pass

    # read variant msas and gt lookup file if (provided)
    if variant_msas is not None:
        logger.debug("Reading in variants and gts from files")

        # calc END_POS for closed interval
        end_closed = oed.IntervalType.isclosed(
            variants_kws["interval_type"], lower=False
        )

        variant_msas = pd.read_pickle(variant_msas).assign(
            **{
                variants_kws["end_col"]: lambda df: df.apply(
                    calc_end_pos, closed=end_closed, axis=1
                )
            }
        )
        gts_lookup = pd.read_csv(
            gt_file_lookup,
            sep="\t",
            header=None,
            names=[
                "CHROM",
                variants_kws["start_col"],
                variants_kws["end_col"],
                "fpath",
            ],
        )

        if len(gts_lookup) == 0:
            raise TypeError("--gts-lookup is empty")
        gts_lookup.fpath.apply(oed.assertfile)

        variants_kws |= {
            "variant_msas": variant_msas,
            "gts_lookup": gts_lookup,
        }

    # get regions or gff3
    if regions_tsv is not None:
        logger.debug("Reading in regions")
        regions = pd.read_csv(regions_tsv, sep="\t")

    else:
        # read in GFF3 (with regions of interest)
        logger.debug("Parsing GFF3")

        gff3_name_order = [
            "Name",
            "gene",
            "geneID",
            "cdsID",
            "rnaID",
            "exonID",
            "otherID",
        ]
        if parsed_gff3 is None:
            # need to parse from gff3
            gff3_df = (
                gff3.parse(ref_gff3)
                .pipe(gff3.consolidate)
                .pipe(oed.ordered_fillna, label="name", order=gff3_name_order)
                .pipe(oed.reorder_cols, ["name", "geneID", "cdsID", "product", "type"])
            )
            gff3_df.to_csv(f"{out_dir}/gff3{suffix}.tsv.gz", sep="\t")
            gff3_df.to_pickle(f"{out_dir}/gff3{suffix}.pkl.gz")
        else:
            try:
                gff3_df = pd.read_pickle(parsed_gff3)

            except pickle.UnpicklingError:
                # read as tsv
                gff3_df = pd.read_csv(parsed_gff3, sep="\t").map(oed.parse_literal_eval)

            if "name" not in gff3_df.columns:
                oed.ordered_fillna(gff3_df, "name", gff3_name_order, inplace=True)

        logger.debug("Selecting GFF3 regions")
        regions = gff3.select_regions(
            gff3_df,
            cds_only=cds_only,
            genes_only=genes_only,
            names_list=names_list,
            names_fpath=names_fpath,
            names_field=names_field,
            regions_tsv=regions_tsv,
        )
        regions.to_csv(f"{out_dir}/regions{suffix}.tsv", sep="\t")

    # kws for gen fasta function
    formatters = {
        "fname_fmt": FA_FNAME_FORMAT,
        "seqrec_fmts": {
            "id": SEQ_ID_FORMAT,
            "name": SEQ_NAME_FORMAT,
            "description": SEQ_DESCRIPTION_FORMAT,
        },
    }

    apply_gen_fasta_kws = {
        "refseqs": refseqs,
        "vcf": vcf,
        "variants_kws": variants_kws,
        "formatters": formatters,
        "dirs": dirs,
        "save_interim": save_interim,
        "is_circular": is_circular,
        "errors_sample": errors_sample,
        "suffix": suffix,
    }

    logger.info(
        "Processing %d region%s...", len(regions), "" if len(regions) == 1 else "s"
    )

    if ncpus is not None:
        regions.parallel_apply(gen_fasta, axis=1, **apply_gen_fasta_kws)
    else:
        regions.apply(gen_fasta, axis=1, **apply_gen_fasta_kws)

    logger.info("Done in %s", str(pd.Timestamp.now() - start_time)[:-4])


# %%

if __name__ == "__main__":
    parser = argparser()
    namespace = parser.parse_args()
    main(namespace)

# %%
