"""alleles2fastas.py"""

from __future__ import annotations

import logging
import sys
from typing import Annotated

import pandas as pd
import vcfpy
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import MutableSeq, Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed
from genomicspy.main import add_gaps
from genomicspy.alleles import (
    SampleErrorHandlingType,
    gen_alleles_for_chrom_vcf,
    gen_alleles_from_variants_df,
)
from genomicspy.vcf import parse_records_generator


__all__ = [
    "check_fasta_seq_coverage",
    "get_seqlen",
    "infer_entry_name",
    "read_alleles_gts_from_variants",
    "read_alleles_gts_from_vcf",
    "write_fasta_seq",
]
# Helpers
def check_fasta_seq_coverage(merged: pd.DataFrame, logger_name: str = None
                             ) -> None:
    """check for entries with GT but no alleles"""
    logger = logging.getLogger(logger_name)
    
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
            merged.merge(missing_alleles["POS"], "right"
                         ).to_string(max_rows=None),
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

    locs = oed.intervals2locs(
        merged, col_from=col_from, col_to=col_to,
        drop_duplicates=False, closed=True
    )

    locs_full_span = oed.intervals2locs(
        [(merged[col_from].min(), merged[col_to].max())],
        col_from=col_from,
        col_to=col_to,
        closed=True,
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
            .replace(
                {"_merge": {"right_only": "missing", "left_only": "extra pos"}}
            )
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


def infer_entry_name(ser: pd.Series, **format_kws) -> str:
    """name priority: explicit name in format_kws, ser name field, ser.name"""
    try:
        # name given, so get it
        assert "name" not in format_kws, format_kws.get("name")

        # get ser name from field
        if format_kws.get("name_field", None) is None:
            name = ser.name
        else:
            name = ser[format_kws.pop("name_field")]

    except AssertionError as err:
        name = err.args[0]

    except KeyError as err:
        # bad name field
        raise KeyError("Bad name_field", err.args[0]) from err

    return name


# Readers/parsers
def read_alleles_gts_from_vcf(
    vcf: str,
    *args,
    chrom: str = None,
    start: int = 1,
    end: int = None,
    refseqs: pd.Series = None,
    closed: oed.ClosedIntervalType = True,
    samples: list[str] = None,
    gt_allele_i: int = 0,
    logger_name: str = None, **kws
):
    """Wrapper for reading and wrangling alleles and gts for gen_fasta"""

    logger = logging.getLogger(logger_name)
    try:
        assert refseqs is not None, "refseq is None"
        assert chrom is not None, "chrom is None"
    except AssertionError as error:
        logger.error(error.args[0])
        raise ValueError(*error.args) from error

    alleles = gen_alleles_for_chrom_vcf(
        vcf,
        chrom=chrom,
        start=start,
        end=end,
        refseq=refseqs.loc[chrom],
        astype=MultipleSeqAlignment,
        closed=closed,
    )
    alleles.reset_index(inplace=True, drop=True)

    # insert gaps and convert all to MSAs
    # assumes alleles are all left-aligned
    which_not_msa = alleles.index[
        alleles["ALLELES"].apply(lambda x: not isinstance(x, MultipleSeqAlignment))
    ]

    alleles.loc[which_not_msa, "ALLELES"] = (
        alleles.loc[which_not_msa, "ALLELES"]
        .apply(
            lambda lst: [
                SeqRecord(MutableSeq(a), id=f"{i}") for i, a in enumerate(lst)
            ]
        )
        .apply(add_gaps)
        .apply(MultipleSeqAlignment)
    )
    # Get genotypes and other info for samples in the given region
    logger.debug("Reading GTs")

    columns = ["CHROM", "POS", "END_POS", "SAMPLE",  "FORMAT/GT"]
    end_pos_closed = closed in ["right", "lower", "both", True]

    gts = pd.DataFrame(
        parse_records_generator(
            vcf,
            chrom,
            start=start,
            end=end,
            fields_list=columns,
            samples=samples,
            end_pos_closed=end_pos_closed,
        ),
        columns=columns,
    )

    gts["FORMAT/GT"].update(gts["FORMAT/GT"].apply(lambda gt: gt[gt_allele_i]))

    # handle
    if len(gts) == 0:  # no variants, in GT. assume all ref GT
        logger.warning("%s:%d-%d No VCF entries for any samples", chrom, start, end)

        # assume all ref GT
        gts = pd.DataFrame(
            [(chrom, start, end, sample, 0) for sample in samples], columns=columns
        )
    return alleles, gts 


def read_alleles_gts_from_variants(
    variants: pd.DataFrame,
    gts_lookup: pd.Series,
    *args,
    chrom: str = None,
    start: int = 1,
    end: int = None,
    refseqs: pd.Series = None,
    closed: oed.ClosedIntervalType = True,
    samples: list[str] = None,
    logger_name: str = None, **kws
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Wrapper for reading and wrangling alleles and gts for gen_fasta"""

    # conditions for getting subset of variants
    def _left_closed(df, pos: int, col: str): return df[col] >= pos

    def _left_open(df, pos: int, col: str): return df[col] > pos

    def _right_closed(df, pos: int, col: str): return df[col] <= pos

    def _right_open(df, pos: int, col: str): return df[col] < pos


    logger = logging.getLogger(logger_name)
    try:
        assert variants is not None, "variants is None"
        assert refseqs is not None, "refseqs is None"
    except AssertionError as error:
        logger.error(error.args[0])
        raise ValueError(*error.args) from error

    alleles = gen_alleles_from_variants_df(
        variants,
        chrom=chrom,
        start=start,
        end=end,
        refseq=refseqs.loc[chrom],
        closed=closed,
        astype=MultipleSeqAlignment,
    )
    # clean up unmeaningful index
    alleles.reset_index(inplace=True, drop=True)
    

    gt_files = (
        gts_lookup
        .loc[((gts_lookup["CHROM"] == chrom) & 
              (gts_lookup.POS <= start) &
              (gts_lookup.END_POS >= end)), "fpath"]
        .apply(pd.read_pickle)
        .pipe(lambda ser: ser.loc[ser.apply(len) > 0])
    )
    
    if len(gt_files) == 0:
        gts = pd.DataFrame(
            columns=["CHROM", "POS", "END_POS", "SAMPLE", "REF", "FORMAT/GT"])
    else:
        gts = pd.concat(gt_files.values)


    # left cond checks col_end vs start
    # right cond checks col_start vs end
    match closed:

        case "right" | "upper":
            left_cond = _left_open
            right_cond = _right_closed

        case "both" | True:
            left_cond = _left_closed
            right_cond = _right_closed

        case None | False:
            left_cond = _left_open
            right_cond = _right_open

        case "left" | "lower":
            left_cond = _left_closed
            right_cond = _right_open

        case _:
            raise ValueError("closed", closed)

    # get only relevant GTs
    gts = gts.loc[(gts["CHROM"] == chrom) & 
                  left_cond(gts, start, "POS") &
                  right_cond(gts, end, "END_POS")
                  ]
    if samples is not None:
        gts = gts.loc[gts["SAMPLE"].isin(samples)]



    # # locus info for genotypes
    # loc_cols = ["CHROM", "POS", "END_POS", "REF"]
    
    # # check for consistency
    # gts_locs = gts[loc_cols].drop_duplicates().assign(
    #     REF=lambda df: df.REF.astype(str).str.upper().str.replace("-", ""))


    # alleles["REF"] = alleles["ALLELES"].apply(
    #     lambda a: a[0]).apply(lambda rec: str(rec.seq)).str.upper().str.replace("-","")

    # check = alleles.merge(
    #     gts_locs, how="outer", on=["CHROM", "POS", "END_POS", "REF"],
    #     indicator=True)
    
    # which_only_GT = check.loc[check["_merge"] == "right_only"]
    # assert len(which_only_GT) == 0, \
    #     ("Some conflicts between alleles and GTs:",
    #         check.loc[check.POS.isin(which_only_GT.POS)])
    

    return alleles, gts

# Writers

def write_fasta_seq(
    sample_gts: pd.DataFrame,
    alleles: pd.DataFrame,
    strand: Annotated[str, "+", "-"] = "+",
    rec_metadata: dict[str, str] = None,
    mutable: bool = False,
    errors: SampleErrorHandlingType = "ignore",
    logger_name: str = None,
) -> SeqRecord:
    """Core generator to construct seqs. See gen_fasta() for details

    rec_metadata: for updating/making SeqRecord
    gts: genotypes (for a sample)
    sample: str
        Name of sample. Used for SeqRecord and logging
    """

    id_cols = ["CHROM", "POS", "END_POS"]

    logger = logging.getLogger(logger_name)

    rec_metadata = dict.fromkeys(["id", "name", "description"], "") | oed.default(
        rec_metadata, {}
    )

    try:
        assert len(sample_gts) > 0, "no GTs"
        _ = alleles.iloc[0, :]

    except (AssertionError, KeyError) as err:
        msg = f"{rec_metadata.get('id', None)}: {err.args[0]}"
        match errors:
            case "raise":
                logger.error(msg)
                raise ValueError(sample_gts) from err
            case "ignore":
                raise AssertionError(msg) from err
            case "force":
                logger.warning("Assuming ref for %s", msg)
            case _:
                raise ValueError(f"Invalid arg for errors: {errors}") from err

    # get sequences/alleles for the sample
    merged = alleles.merge(
        sample_gts, "outer", on=id_cols).fillna({"GT": 0}).astype({"GT": int})

    check_fasta_seq_coverage(merged.reset_index(), logger_name=logger_name)
    
    # set index to preserve info in sample_alleles
    try:
        assert merged.index.names != id_cols
        merged.set_index(id_cols, inplace=True)
    except AssertionError:
        pass

    # cross-ref GT with ALLELES
    if strand == "-":  # use revcomp data
        sample_alleles = merged.apply(
            lambda ser: ser["ALLELES_RC"][ser["GT"]], axis=1
        ).sort_index(ascending=[True, False, False])
    else:
        sample_alleles = merged.apply(
            lambda ser: ser["ALLELES"][ser["GT"]], axis=1
        ).sort_index(ascending=True)

    # write seq (after putting the alleles in order)
    rec = oed.agg(sample_alleles) + SeqRecord("")

    # update seq object type
    rec.seq = MutableSeq(rec.seq) if mutable else Seq(rec.seq)
    # update metadata
    for k, v in rec_metadata.items():
        setattr(rec, k, v)

    return rec


