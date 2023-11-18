# trim.py

"""Trimming alleles"""

from __future__ import annotations
from collections.abc import Collection, Sequence
from typing import Annotated

import pandas as pd
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import MutableSeq, Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed
from genomicspy.main import SeqType, copy_seqrecord

__all__ = [
    "trim_alleles",
    "trim_allele_seqs",
]

def _calc_new_pos(anns: dict, left=None, right=None, pos_field: str = "POS",
                 end_pos_field: str = "END_POS") -> dict[str, int]:
    """Calculate new positions after trimming"""

    new_anns = {}
    try:
        new_anns |= {"POS": anns[pos_field] + left,
                     "OLD_POS": anns[pos_field]}
    except (KeyError, TypeError):
        pass

    try:
        # +1 because end pos bound is open
        new_anns |= {"END_POS": anns[end_pos_field] - right + 1,
                     "OLD_END_POS": anns[end_pos_field]}

    except (KeyError, TypeError):
        pass

    return new_anns



def _trim_seqs(seqs: Collection[str | Seq | MutableSeq],
               left: int = None,
               right: int = None,
               length: int = None,
               ) -> Collection[str | Seq | MutableSeq]:
    """Makes a copy of the allele sequences and adjust for short seqs"""

    if length is None:
        length = max(len(s) for s in seqs)

    if right is not None:
        for i, seq in enumerate(seqs):
            t_right = right - (length - len(seq))
            t_left = left - (length - len(seq))
            seqs[i] = seq[t_left:-t_right]

    elif right is not None:
        for i, seq in enumerate(seqs):
            t_right = right - (length - len(seq))
            seqs[i] = seq[:-t_right]

    elif left is not None:
        for i, seq in enumerate(seqs):
            t_left = left - (length - len(seq))
            seqs[i] = seq[t_left:]

    return seqs


def _calc_trim(seqs: Sequence[str | Seq | MutableSeq],
               left: int = None,
               right: int = None,
               length: int = None,
               ) -> list[tuple[int, int]]:
    """Calculate how much to trim from each end relative to full length"""
    if length is None:
        length = max(len(seq) for seq in seqs)

    t_left_right = []

    # calculate how much to trim each record
    for seq in enumerate(seqs):
        try:
            t_left = left - (length - len(seq))
        except TypeError:
            t_left = 0
        try:
            t_right = right - (length - len(seq))
        except TypeError:
            t_right = 0
        t_left_right.append((t_left, t_right))
    return t_left_right


def _trim_seq_recs(records: Collection[SeqRecord],
                   left: int = None,
                   right: int = None,
                   length: int = None,
                   inplace: bool = False,
                   ) -> list[SeqRecord] | None:
    """Trim alleles inplace, adjusting for short seqs"""
    # calculate how much to trim each record
    t_left_right = _calc_trim([rec.seq for rec in records], left, right, length)


    trimmed = []
    for rec, (t_left, t_right) in zip(records, t_left_right):
        rec_anns = {"TRIMMED_LEFT": t_left,
                    "TRIMMED_RIGHT": t_right,
                    "SEQ_TRIMMED_RIGHT": rec.seq[-t_right:],
                    "SEQ_TRIMMED_LEFT": rec.seq[:t_left],
                    }
        seq = rec.seq[t_left:-t_right]
        trimmed.append((seq, rec_anns))

    if inplace:
        for rec, (seq, anns) in zip(records, trimmed):
            rec.seq = seq
            rec.annotations |= anns

    else:
        return [copy_seqrecord(rec, seq=seq, annotations=anns, append=True)
                for rec, (seq, anns) in zip(records, trimmed)]


def _trim_mutableseqs(seqs: Collection[MutableSeq],
                      left: int = None,
                      right: int = None,
                      length: int = None,
                      ) -> None:

    """Trims MutableSeq in place"""
    # calculate how much to trim each record
    t_left_right = _calc_trim(seqs, left, right, length)

    for seq, (t_left, t_right) in zip(seqs, t_left_right):
        for _ in range(t_right):
            seq.pop()
        for _ in range(t_left):
            seq.pop(0)


def _trim_mutableseq_recs(records: Collection[SeqRecord],
                          left: int = None,
                          right: int = None,
                          length: int = None,
                          ) -> None:

    """Trims records with MutableSeq in place"""

    t_left_right = _calc_trim([rec.seq for rec in records], left, right, length)

    for rec, (t_left, t_right) in zip(rec, t_left_right):
        rec.annotations |= {"TRIMMED_LEFT": t_left,
                            "TRIMMED_RIGHT": t_right,
                            "SEQ_TRIMMED_RIGHT": MutableSeq(rec.seq[-t_right:]),
                            "SEQ_TRIMMED_LEFT": MutableSeq(rec.seq[:t_left]),
                            }
        for _ in range(t_right):
            rec.seq.pop()
        for _ in range(t_left):
            rec.seq.pop(0)



def trim_allele_seqs(alleles: MultipleSeqAlignment | Collection[SeqType],
                     left: int = None,
                     right: int = None,
                     length: int = None,
                     dtype: Annotated[str | type, "first", SeqType] = "first",
                     inplace: bool = False
                     ) -> MultipleSeqAlignment | Collection[SeqType] | None:
    """Trim alleles. Supply only one of left or right

    Parameters
    ----------
    alleles:  MultipleSeqAlignment or list-like of SeqType obj
        Alleles to trim
    left:   int
        If given, trim this many bases from the left
    right:   int
        If given, trim this many bases from the right
    length: int
        Length of MSA (used for adjust cutting short sequences). Default
        longest allele in given data
    dtype:  SeqType type or 'first'
        data type of the alleles. Default checks the first allele
    inplace: bool
        For MutableSeq, SeqRecord, and MultipleSeqAlignment. Trim in place.
        Default False

    Returns:  trimmed alleles or None (if inplace is True)
    """

    # add annotations

    if len(alleles) == 0:
        return alleles

    if dtype == "first":
        dtype = type(alleles[0])

    if length is None:
        length = max(len(a) for a in alleles)

    trimmed = None  # init here for easier returns

    # process based on output dtype
    
    # MutableSeq 
    if issubclass(dtype, MutableSeq) and inplace:
        _trim_mutableseqs(alleles, left=left, right=right, length=length)

    # either a list-like of SeqRecords or a MultipleSeqAlignment
    elif issubclass(dtype, SeqRecord):

        msa_anns = {"MSA_TRIMMED_LEFT": left,
                    "MSA_TRIMMED_RIGHT": right} | \
                    _calc_new_pos(alleles.annotations, left=left, right=right)

        if inplace:
            
            # process MutableSeq and regular Seq in SeqRecs differently
            mutableseqs = []
            immutableseqs = []
            for rec in alleles:
                if isinstance(rec.seq, MutableSeq):
                    mutableseqs.append(rec)
                else:
                    immutableseqs.append(rec)
                    
            _trim_mutableseq_recs(
                mutableseqs, left=left, right=right, length=length)

            _trim_seq_recs(
                immutableseqs, left=left, right=right, length=length,
                inplace=inplace)

            # annotate with updated positions
            for rec in alleles:
                rec.annotations |= _calc_new_pos(
                    rec.annotations, left=left, right=right)

            # add higher-order annotations for MSA
            if isinstance(alleles, MultipleSeqAlignment):
                    alleles.annotations |= msa_anns

        else:  # not inplace
            
            trimmed =_trim_seq_recs(
                alleles, left=left, right=right, length=length,
                inplace=inplace)

            # annotate with updated positions
            for rec in trimmed:
                rec.annotations |= _calc_new_pos(
                    rec.annotations, left=left, right=right)

            # conform to MSA if input was MSA
            if isinstance(alleles, MultipleSeqAlignment):

                trimmed = MultipleSeqAlignment(
                    trimmed,
                    annotations=alleles.annotations | msa_anns,
                    column_annotations=alleles.column_annotations,
                    )

    
    else:  # str, Seq, or MutableSeq with inplace=False
        trimmed = _trim_seqs(
            [a for a in alleles], left=left, right=right, length=length)


    return trimmed


def trim_alleles(alleles: pd.DataFrame,
                 start: int = 1,
                 end: int = None,
                 col_start: str = "POS",
                 col_end: str = "END_POS",
                 closed: oed.ClosedIntervalType = "left",
                 update_pos: bool = False,
                 inplace: bool = False) -> pd.DataFrame:
    """Trim alleles that span over start/end of interval. Assumes closed



    closed:  'left', 'lower', 'right', 'upper', 'both', True, False, or None
    Treat ranges as closed on the
    - 'left' or 'lower':  left/lower bound only, i.e. [from, to)
    - 'right' or 'upper': right/upper bound only, i.e. (from, to]
    - 'both' or True:     both bounds (interval is closed), i.e. [from, to]
    - None or False:      interval is open, i.e. (from, to)
    Default 'lower' (which is the native python range interpretation)

    update_pos: bool, default False
        If True, updates col_start and col_end columns. If False, makes new
        columns TRIMMED_{col_start,col_end}
    """
    # drop positions that are wholly out of interval

    def _apply_trim_allele_seqs(ser: pd.Series,
                                ) -> pd.Series:

        trim_left = max(0, start - ser[col_start])
        trim_right = max(0, ser[col_end] - end)

        new_pos = ser[col_start] + trim_left
        new_end_pos = ser[col_end] - trim_right

        updates = {
            "TRIMMED": trim_allele_seqs(
                ser["ALLELES"], left=trim_left, right=trim_right)
        }
        if update_pos:
            updates |= {col_start: new_pos, col_end: new_end_pos}
        else:
            updates |= {f"TRIMMED_{col_start}": new_pos,
                        f"TRIMMED_{col_end}": new_end_pos}

        return ser.combine(pd.Series(updates), lambda x, y: oed.default(y, x))

    def _fillna_trimmed(df):
        return df.fillna({"TRIMMED": df["ALLELES"], t_col_start: df[col_start], t_col_end: df[col_end]})

    t_col_start = f"TRIMMED_{col_start}"
    t_col_end = f"TRIMMED_{col_end}"
    dtypes = dict.fromkeys([t_col_start, t_col_end], int)


    if end is None:
        end = max(alleles[col_end])

    match closed:

        case "left" | "lower":
            left_cond = alleles[col_end] >= start
            right_cond = alleles[col_start] < end

        case "right" | "upper":
            left_cond = alleles[col_end] > start
            right_cond = alleles[col_start] <= end

        case "both" | True:
            left_cond = alleles[col_end] >= start
            right_cond = alleles[col_start] <= end

        case None | False:
            left_cond = alleles[col_end] > start
            right_cond = alleles[col_start] < end

        case _:
            raise ValueError("closed", closed)


    pruned = alleles.loc[left_cond & right_cond]

    which_spans = (pruned[col_start] < start) | (pruned[col_end] > end)

    if which_spans.any():
        spans = pruned.loc[which_spans].apply(_apply_trim_allele_seqs, axis=1)

        trimmed = pd.concat([pruned.loc[~which_spans], spans]
                            ).pipe(_fillna_trimmed).astype(dtypes)

    else:
        trimmed = (
            pd.DataFrame(
                columns=["TRIMMED", t_col_start, t_col_end],
                index=pruned.index,
            )
            .pipe(lambda df: pd.concat([pruned, df], axis=1))
            .pipe(_fillna_trimmed)
            .astype(dtypes)
        )

    trimmed.sort_values(["CHROM", col_start, col_end], inplace=True)

    if inplace:
        trimmed.drop("ALLELES", axis=1, inplace=True)
        trimmed.rename({"TRIMMED": "ALLELES"}, axis=1, inplace=True)

    return trimmed
