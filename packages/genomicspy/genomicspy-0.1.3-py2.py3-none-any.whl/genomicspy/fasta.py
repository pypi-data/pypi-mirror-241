"""alleles2fastas.py"""

from __future__ import annotations

import gzip
import sys
from collections.abc import Hashable
from logging import Logger, getLogger
from typing import Annotated

import pandas as pd
import vcfpy
from Bio import SeqIO
from Bio.Seq import MutableSeq, Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed


__all__ = [
    "SampleErrorHandlingType",
    "check_fasta_seq_coverage",
    "get_seqlen",
    "parse_fasta_refs",
    "write_fasta_seq",
    "write_outputs",
]


class SampleErrorHandlingType(metaclass=oed.OptionsMetaType):
    """Sample error handling type"""

    bases = (str,)
    options = ("ignore", "force", "raise")


# Helpers
def check_fasta_seq_coverage(merged: pd.DataFrame, logger_name: str = None) -> None:
    """check for entries with GT but no alleles"""
    logger = getLogger(logger_name)

    assert merged["CHROM"].nunique() <= 1, "Multiple CHROMs in merged"
    try:
        _ = merged.iloc[0, :]
        missing_alleles = merged.loc[merged["ALLELES"].isnull()]
        assert len(missing_alleles) == 0, missing_alleles

    except KeyError as err:
        err_msg = "Has GTs and alleles, but empty after merge"
        logger.error(err_msg)
        raise ValueError(err_msg) from err

    except AssertionError as err:
        err_msg = f"{len(missing_alleles)} entries have GT but no ALLELES!"
        logger.error(err_msg)
        print(
            f"[{logger_name} ERROR] Positions with missing alleles!",
            merged.merge(missing_alleles["POS"], "right").to_string(max_rows=None),
            sep="\n",
            file=sys.stderr,
        )
        raise ValueError(err_msg) from err

    if "TRIMMED_POS" in merged:
        col_from = "TRIMMED_POS"
        col_to = "TRIMMED_END_POS"
    else:
        col_from = "POS"
        col_to = "END_POS"

    # TODO: may need to make interval_type dynamic
    locs = oed.intervals2locs(
        merged,
        col_from=col_from,
        col_to=col_to,
        drop_duplicates=False,
        interval_type="closed",
    )

    locs_full_span = oed.intervals2locs(
        [(merged[col_from].min(), merged[col_to].max())],
        col_from=col_from,
        col_to=col_to,
        interval_type="closed",
    )

    try:
        overlap = locs.loc[locs.duplicated(keep=False)]
        assert not locs.duplicated().any(), [
            "Some overlap in alleles!",
            overlap.to_string(max_rows=None),
        ]

        pos_discrepancies = (
            pd.merge(locs, locs_full_span, how="outer", indicator=True)
            .pipe(lambda df: df.loc[df["_merge"] != "both"])
            .replace({"_merge": {"right_only": "missing", "left_only": "extra pos"}})
        )

        assert len(pos_discrepancies) == 0, [
            "Some discrepancies in positions",
            oed.calc_intervals(pos_discrepancies["loc"]),
        ]

    except AssertionError as error:
        logger.error(error.args[0])
        print(f">> {error.args[0]}", error.args[1], sep="\n", file=sys.stderr)
        raise error


def get_seqlen(vcf: str, chrom: str) -> int:
    """figure out refseq len"""
    # calculate padding from chrom (contig) length (from vcf)
    with vcfpy.Reader.from_path(vcf) as reader:
        contigs = reader.header.get_lines("contig")
        try:
            contig = next(filter(lambda ctg: (ctg.id == chrom), contigs))

        except StopIteration as err:
            raise ValueError(f"Contig {chrom} not found in vcf.") from err

        return contig.length


# Parsing and selecting
def parse_fasta_refs(*fasta_refs: str) -> pd.Series:
    """Parse fasta refs given by args as fpaths"""

    def _parse_fasta_ref(fa: str) -> SeqRecord:
        try:
            return SeqIO.read(fa, "fasta")
        except UnicodeDecodeError:  # likely gzipped file
            with gzip.open(fa, "rt") as fin:
                for record in SeqIO.parse(fin, "fasta"):
                    return record

    refseqs = pd.Series([_parse_fasta_ref(fa) for fa in fasta_refs])
    refseqs.index = pd.Index(refseqs.apply(getattr, args=("id",)), name="CHROM")

    return refseqs


# Writers


def write_outputs(
    variants,
    fa_path: str,
    seqrec_fmts: dict = None,
    format_kws: dict = None,
    annotations: dict = None,
    save_interim: bool = False,
    errors_sample: SampleErrorHandlingType = "ignore",
) -> list[SeqRecord] | None:
    """Construct and write fasta and other interim output

    Parameters
    ----------
    variants: Variants
    fa_path:  str
        Fasta output path
    seqrec_fmts: dict. Takes:
    - seqid_fmt: str
        Format strings for seq record id, name, and description. Wrap
        region/entry-level fields in single brackets and sample-specific
        fields in double brackets as the former are substituted first, and
        the latter in a later step. Default is ""
    errors_sample: str    <ignore, force, raise>. Default 'ignore'.
        If sample is missing from GTs in VCF
        - 'ignore': warn and skip the sample
        - 'force':  assume it is same as refseq and generate fasta anyway
        - 'raise':  raise error and exit

    """
    # Output formatting
    seqrec_fmts = dict.fromkeys(["id", "name", "description"], "") | seqrec_fmts

    # format with region-level data
    for k, fmt in seqrec_fmts.items():
        seqrec_fmts[k] = fmt.format(**format_kws)

    fasta_records = []
    with gzip.open(fa_path, "wt") as fa_out:
        for alias, xrefs in variants.alias_crossrefs.iterrows():
            # alias = GT_ALIAS_FORMAT.format(gt_alias=gt_alias, gt_pad=gt_pad)

            # write metadata
            rec_fmt_kws = {
                "sample": alias,
                "n_samples": len(xrefs["SAMPLE"])
                # "GT": xrefs["KEY"],
            }
            rec_metadata = dict(
                (k, fmt.format(**rec_fmt_kws)) for k, fmt in seqrec_fmts.items()
            )

            # add sample-level annotations
            rec_metadata["annotations"] = {
                "sample": alias,
                "n_samples": len(xrefs["SAMPLE"]),
            } | annotations

            # write fasta seq record
            rec = write_fasta_seq(
                variants.aliased_genotypes.xs(alias, 0, "GT_ALIAS"),
                variants.trimmed,
                strand=variants.strand,
                rec_metadata=rec_metadata,
                errors=errors_sample,
                logger=variants.logger,
            )

            if save_interim:  # save mem if we don't need to return/save recs
                fasta_records.append(rec)

            fa_out.write(rec.format("fasta"))

    if save_interim:
        return fasta_records

    return

def write_fasta_seq(
    sample_gts: pd.DataFrame,
    alleles: pd.DataFrame,
    strand: Annotated[str, "+", "-"] = "+",
    rec_metadata: dict[str, str] = None,
    interval_type: oed.IntervalType = "closed",
    colnames: dict[Annotated[str, "start", "end", "seq", "seq_rc"], Hashable] = None,
    mutable: bool = False,
    errors: SampleErrorHandlingType = "ignore",
    logger: str | Logger = None,
) -> SeqRecord:
    """Core generator to construct seqs. See gen_fasta() for details

    #TODO docstr
    #TODO test
    rec_metadata: for updating/making SeqRecord
    gts: genotypes (for a sample)
    sample: str
        Name of sample. Used for SeqRecord and logging

    colnames:
        Column labels for start pos, end pos, alleles, rev comp alleles.
        Default POS, END_POS, ALLELES, ALLELES_RC
    """

    def _check_coverage(intervals: pd.DataFrame, col_from: str, col_to: str):
        locs = oed.intervals2locs(
            intervals,
            col_from=col_from,
            col_to=col_to,
            drop_duplicates=False,
            interval_type=interval_type,
        )

        assert not locs.duplicated().any(), [
            "Some overlap in alleles!",
            locs.loc[locs.duplicated(keep=False)].to_string(max_rows=None),
        ]

        assert (
            len(oed.calc_intervals(locs, interval_type=interval_type)) == 1
        ), "Some internal positions are missing"

    if colnames is None:
        colnames = {}

    start_col = colnames.get("start", "POS")
    end_col = colnames.get("start", "END_POS")
    seq_col = colnames.get("seq", "ALLELES")
    seq_col_rc = colnames.get("seq_rc", "ALLELES_RC")

    if isinstance(logger, str):
        logger = getLogger(logger)

    rec_metadata = dict.fromkeys(["id", "name", "description"], "") | oed.default(
        rec_metadata, {}
    )

    try:
        assert len(sample_gts) > 0, "no GTs"
        _ = alleles.iloc[0, :]

    except AssertionError as err:
        msg = f"{rec_metadata.get('id', None)}: {err.args[0]}"
        match errors:
            case "raise":
                logger.error(msg)
                raise ValueError(sample_gts) from err
            case "ignore":
                raise AssertionError(msg) from err
            case "force":
                logger.info("Assuming ref for %s", msg)
            case _:
                raise ValueError(f"Invalid arg for errors: {errors}") from err

    # get sequences/alleles for the sample
    merged = alleles.join(sample_gts, how="outer").fillna({"GT": 0}).astype({"GT": int})

    # check for entries with GT but no alleles (don't know how this happens)
    try:
        _ = merged.iloc[0, :]
        missing_alleles = merged.loc[merged[seq_col].isnull()]
        assert len(missing_alleles) == 0, missing_alleles

    except KeyError as err:
        raise ValueError("Has GTs and alleles, but empty after merge") from err

    except AssertionError as err:
        print(
            "Missing alleles!",
            missing_alleles.to_string(max_rows=None),
            file=sys.stderr,
        )
        raise ValueError(
            f"{len(missing_alleles)} entries have GT but no alleles!"
        ) from err

    # check that whole region is covered (exactly once)
    _check_coverage(merged.index.to_frame(), start_col, end_col)
    # TODO put in separate function to test
    # cross-ref GT with ALLELES
    if strand == "-":  # use revcomp data
        sample_alleles = merged.apply(
            lambda ser: ser[seq_col_rc][ser["GT"]], axis=1
        ).sort_index(
            level=["CHROM", end_col, start_col], ascending=[True, False, False]
        )

    else:
        sample_alleles = merged.apply(
            lambda ser: ser[seq_col][ser["GT"]], axis=1
        ).sort_index(ascending=True)

    # write seq (after putting the alleles in order)
    rec = oed.agg(sample_alleles) + SeqRecord("")

    # update seq object type
    rec.seq = MutableSeq(rec.seq) if mutable else Seq(rec.seq)
    # update metadata
    for k, v in rec_metadata.items():
        setattr(rec, k, v)

    return rec
