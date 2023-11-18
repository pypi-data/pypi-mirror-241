"""Alleles-related tools"""

#%%
from __future__ import annotations
import sys
from collections.abc import Callable, Hashable, Sequence

import pandas as pd
from Bio.AlignIO import MultipleSeqAlignment
from Bio.SeqIO import SeqRecord
from Bio.Seq import MutableSeq, Seq
from numpy import array, ndarray
from pandas.core.generic import NDFrame

import oddsnends as oed
from genomicspy.main import SeqType


__all__ = [
    "VCF_DEFAULT_DICT",
    "calc_circular",
    "calc_end_pos",
    "check_overlap",
    "pos_conditions",
]


VCF_DEFAULT_DICT = {"ID": [],
                    "QUAL": None,
                    "FILTER": ["PASS"],
                    "INFO": {},
                    "FORMAT": ["GT"],
                    }

def calc_circular(pos: NDFrame | Sequence,
                  length: int) -> NDFrame | ndarray:
    """Calculate real positions on circle as 1-indexed"""
    #TODO: TESTS
    if isinstance (pos, NDFrame):
        return (pos % length).mask(lambda ser: ser == 0, length)

    mods = array(pos) % length
    mods[mods == 0] = length
    return mods


def calc_end_pos(ser: pd.Series = None,
                 seq: SeqType = None,
                 start: int = None,
                 seq_field: str = "ALLELES",
                 start_field: str = "POS",
                 closed: bool = True,
                 gaps: str = "-") -> int:
    """Calculate end position using length of sequence.

    Parameters
    ----------
    ser: pd.Series
        Contains sequence(s) and start positions. If None, seq and start_pos
        are required. If ser[seq_field] has multiple seqs, the first is taken
    seq: SeqType
        Sequence for which to calculate end pos. If None, ser is required
    start: int
        starting position (assumes left-closed). Required if ser is None
    seq_field: str
        Name of field containing sequence object
    start_field: str
        Name of field containing starting position
    closed: bool
        Whether end position should be closed or open

    Returns:  end position as int

    Usage:
    >>> calc_end_pos(pd.Series(dict(ALLELES="ACACCCTGGT", POS=4)), closed=True)
    13
    >>> calc_end_pos(seq="ACACCCTGGT", start=4, closed=False)
    14
    >>> calc_end_pos(seq="GGAC-CTGG-", start=1, closed=True)
    8

    """
    if ser is not None:
        start = oed.default(start, ser[start_field])
        seq = oed.default(seq, ser[seq_field])

    # multiple seqs given. Use the first
    if isinstance(seq, (str, Seq)):
        pass
    elif isinstance(seq, Hashable):
        raise TypeError("seq type should be SeqType", type(seq), seq)
    else: # MultipleSeqAlignment or collection of seq types
        seq = seq[0]

    if isinstance(seq, (str, MutableSeq, Seq)):
        pass
    elif isinstance(seq, (MultipleSeqAlignment, Sequence)): # multiple seqs
        seq = seq[0]
    else:
        raise TypeError(
            "seq must be SeqType or collection of SeqType.", type(seq), seq)

    # check if obtained seq object is record (if so, get the actual seq)
    if isinstance(seq, SeqRecord):
        seq = seq.seq

    return start + len(seq.replace(gaps, "")) - (1 if closed else 0)

#%%

def check_overlap(positions: pd.DataFrame,
                  chrom: str,
                  length: int = None,
                  is_circular: bool = False,
                  errout: str = ".",
                  **kws,
                  ) -> None:
    """Check if intervals of entries overlap.

    Intervals are right-open and 1-indexed.

    Parameters
    ------------
    positions: pd.DataFrame
        Contains chrom and start/endpositions
    chrom:      str
    length:     int     Total contig length. Required if is_circular is True

    Optional:
    is_circular: bool   Treat entries on circular contig. Default False
    errout:      str    Output directory for error files. Default "."

    **kws takes:
    chrom_col:  str     Name of chrom col. Default "CHROM
    start_col:  str     Col name of interval start index
    end_col:    str     Col name of interval end index

    Returns:  None
    """
    assert not(is_circular and length is None), \
        f"is_circular is {is_circular} but length is {length}"

    chrom_col = kws.get("chrom_col", "CHROM")
    start_col = kws.get("start_col", "POS")
    end_col = kws.get("end_col", "END_POS")

    # get interval start and end columns
    entries = positions.loc[positions["CHROM"] == chrom, [start_col, end_col]]

    # group entries by each position and count
    # resulting df has index as pos, values as ids from entries index and n_ids
    locs = oed.intervals2locs(
        entries, col_from=start_col, col_to=end_col,
        ignore_index=False, drop_duplicates=False)


    if is_circular:

        # calculate real position on a circular chromosome
        locs = calc_circular(locs, length)

        # make same pos val as dot for easier reading
        entries[f"{end_col}_circ"] = (
            calc_circular(entries[end_col], length)
            .mask(lambda ser: entries[end_col] <= ser, ".")
        )

    locs = (
        locs
        .rename_axis("positions_index")
        .reset_index(name="pos")
        .pivot_table("positions_index", "pos", aggfunc=lambda x: x)
    )
    locs["n_entries"] = locs["positions_index"].apply(
        lambda x: 1 if isinstance(x, Hashable) else len(x))

    try:
        # check if there are overlaps
        overlaps = locs.loc[locs.n_entries > 1]
        assert len(overlaps) == 0, "Overlapping entries exist."

    except AssertionError:

        # ranges of overlap
        overlap_ranges = oed.calc_intervals(overlaps.index, interval_type="closed")

        # ids corresponding to entries index
        overlap_entries = (
            overlaps["positions_index"].explode().drop_duplicates()
            .pipe(lambda ser: entries.loc[ser, :])
            .assign(**{chrom_col: chrom})
            .pipe(positions.merge, "inner", on=[chrom_col, start_col, end_col])
            )

        suffix = oed.default(chrom, "", has_value=f".{chrom}")

        # save entries for review
        positions_check_fname = f"positions_check{suffix}.tsv"
        locs.to_csv(f"{errout}/{positions_check_fname}", sep="\t")

        overlap_entries_fname = f"overlapping_alleles{suffix}.tsv"
        overlap_entries.to_csv(f"{errout}/{overlap_entries_fname}", sep="\t")

        print(
            ">> OVERLAPS",
            f">> {len(overlap_ranges)} intervals span {len(overlaps)} position:",
            "",
            *(f"{chrom}:{i}-{j}" for i, j in overlap_ranges),
            "",
            f">> {len(overlap_entries)} overlapping entries:",
            overlap_entries.to_string(),
            "",
            ">> Checks and ranges saved to:",
            f"    {positions_check_fname} and ",
            f"    {overlap_entries_fname}",
            sep="\n", file=sys.stderr, flush=True)



def pos_conditions(interval_type: oed.IntervalType) -> tuple[Callable, Callable]:
    """
    Returns functions for lower and upper bound conditions to filter data
    based on `interval_type` parameter

    Parameter
    ---------
    interval_type: oed.IntervalType
        interval type. see help(IntervalType)

    Returns
    -------
    tuple of 2 functions
        (lower bound, upper bound) filter condition. Each function takes a
        position and a reference position, and returns a bool

        left_closed:  pos >= ref
        left_open:    pos > ref
        right_closed: pos <= ref
        right_open:   pos < ref
    """
    # Determine range conditions on lower and upper bounds for filter

    # conditions for getting subset of variants
    def _left_closed(pos: int, ref: int):
        return pos >= ref

    def _left_open(pos: int, ref: int):
        return pos > ref

    def _right_closed(pos: int, ref: int):
        return pos <= ref

    def _right_open(pos: int, ref: int):
        return pos < ref

    # left cond checks col_end vs start
    # right cond checks col_start vs end
    match interval_type:
        case "right" | "upper":
            left_cond = _left_open
            right_cond = _right_closed

        case "closed" | "both" | True:
            left_cond = _left_closed
            right_cond = _right_closed

        case "open" | False:
            left_cond = _left_open
            right_cond = _right_open

        case "left" | "lower":
            left_cond = _left_closed
            right_cond = _right_open

        case _:
            raise TypeError(
                "interval_type must be oed.IntervalType.",
                interval_type,
                type(interval_type),
            )

    return left_cond, right_cond
