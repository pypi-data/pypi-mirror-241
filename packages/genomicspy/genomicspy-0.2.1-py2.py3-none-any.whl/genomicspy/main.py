"""Main module."""
# alleles.py
from __future__ import annotations
from collections.abc import Collection, Sequence
from typing import Annotated

from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import MutableSeq, Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed

__all__ = [
    "SeqType",
    "add_gaps",
    "copy_multipleseqalignment",
    "copy_seqrecord",
    "seq_astype",
    "seq_as_msa",
]


class SeqType(metaclass=oed.OptionsMetaType):
    """Types for single sequences"""

    bases = (type,)
    options = (str, Seq, MutableSeq, SeqRecord)


class SequencesType(metaclass=oed.OptionsMetaType):
    """Types for one or multiple sequences"""

    bases = (type,)
    options = (SeqType, MultipleSeqAlignment, Sequence[SeqType])


def add_gaps(alleles: MultipleSeqAlignment | Collection[SeqType]):
    "Appends sequences with gaps. Assumes alleles are left-aligned" ""
    msa_len = max(len(a) for a in alleles)
    gapped = [a + "-" * (msa_len - len(a)) for a in alleles]
    if isinstance(alleles, MultipleSeqAlignment):
        new_msas = copy_multipleseqalignment(alleles, records=gapped, append=False)
        return new_msas
    return gapped


def copy_seqrecord(rec: SeqRecord, append: bool = True, **kws):
    """Makes a copy of SeqRecord, overriding any kwargs with **kws

    append: applies to dbxrefs, features, annotations, and letter_annotations
    """

    # defaults
    features = rec.features
    dbxrefs = rec.dbxrefs
    annotations = rec.annotations
    letter_annotations = rec.letter_annotations

    # set defaults
    if append:
        features += kws.pop("features", [])
        dbxrefs += kws.pop("dbxrefs", [])
        annotations |= kws.pop("annotations", {})
        letter_annotations |= kws.pop("letter_annotations", {})

    kws = {
        "seq": rec.seq,
        "name": rec.name,
        "id": rec.id,
        "description": rec.description,
        "dbxrefs": dbxrefs,
        "features": features,
        "annotations": annotations,
        "letter_annotations": letter_annotations,
    } | kws
    return SeqRecord(**kws)


def copy_multipleseqalignment(msa: MultipleSeqAlignment, append: bool = True, **kws):
    """Makes a copy of MultipleSeqAlignment, overriding with any **kws

    append applies to records, annotations and column_annotations
    """
    # defaults

    records = [copy_seqrecord(rec) for rec in msa]
    annotations = msa.annotations
    column_annotations = msa.column_annotations

    try:
        if append:
            kws["records"] = records + kws["records"]
    except KeyError:
        kws["records"] = records

    try:
        if isinstance(kws["annotations"], Collection) and not isinstance(
            kws["annotations"], dict
        ):
            kws["annotations"] = dict(
                (k, records[0].get(k, None)) for k in kws["annotations"]
            )

        if append:
            kws["annotations"] = annotations | kws["annotations"]

    except KeyError:
        kws["annotations"] = annotations

    try:
        if append:
            kws["column_annotations"] = column_annotations + kws["column_annotations"]
    except KeyError:
        kws["column_annotations"] = column_annotations

    return MultipleSeqAlignment(**kws)


def seq_as_seqrecord(
    seq_obj: SeqType,
    inplace: bool = False,
    append: bool = True,
    mutable: bool = False,
    **kws,
) -> MultipleSeqAlignment:
    """Convert sequence object to SeqRecord

    Parameters
    ----------
    seq_obj: SeqType
    inplace: bool, optional
        Modify object in place. Default False
    append: bool, optionanl
        Update annotations to the object (existing if inplace, or else the new
        object). If False, existing annotations are overwritten. Default True.
    **kws:
        passed to MultipleSeqAlignment copy or init

    """
    cast_seq = MutableSeq if mutable or isinstance(seq_obj, MutableSeq) else Seq

    if isinstance(seq_obj, SeqRecord):
        # copy the msa
        if not inplace:
            return copy_seqrecord(seq_obj, append=append, **kws)

        if append:
            seq_obj.annotations |= annotations
        else:
            seq_obj.annotations = annotations
        return seq_obj

    # construct/get seq first, then make new record
    if isinstance(seq_obj, str):
        seq = Seq(f"{seq_obj}")

    elif not isinstance(seq_obj, (Seq, MutableSeq)):
        raise TypeError("Input must be SeqType", type(seq_obj), seq_obj)

    elif not inplace:
        seq = cast_seq(seq_obj)

    else:
        seq = seq_obj

    return SeqRecord(seq, **kws)


def seq_as_msa(
    seq_obj: SequencesType,
    inplace: bool = False,
    mutable: bool = False,
    append: bool = True,
    **kws,
) -> MultipleSeqAlignment:
    """Convert sequence object to MultipleSeqAlignment

    Parameters
    ----------
    seq_obj: SequencesType
    ser: pd.Series, optional
        Used for getting annotations. Required if annotations is list-like.
        Default None.
    inplace: bool, optional
        Modify object in place. Default False
    append: bool, optionanl
        Update annotations to the object (existing if inplace, or else the new
        object). If False, existing annotations are overwritten. Default True.
    **kws:
        passed to MultipleSeqAlignment copy or init

    """
    cast_seq = MutableSeq if mutable else Seq
    # check input type

    # is MSA
    if isinstance(seq_obj, MultipleSeqAlignment):
        if not inplace:
            return copy_multipleseqalignment(seq_obj, append=append, **kws)

        try:  # in place
            if append:
                seq_obj.annotations |= kws["annotations"]
            else:
                seq_obj.annotations = kws["annotations"]
        except KeyError:
            pass

        return seq_obj

    # not an MSA. need to initialize one. Make items into records first
    if isinstance(seq_obj, SeqRecord):
        # input is already a SeqRecord

        records = [seq_obj if inplace else copy_seqrecord(seq_obj)]

    elif isinstance(seq_obj, (str, Seq, MutableSeq)):
        # input is a single obj that needs to first be made into a SeqRecord
        match seq_obj:
            case str():
                seq = cast_seq(f"{seq_obj}")

            case Seq() | MutableSeq() if not inplace:
                seq = cast_seq(seq_obj)

            case _:
                seq = seq_obj

        records = [SeqRecord(seq)]

    elif isinstance(seq_obj, Collection):
        # multiple sequences to process

        if len(set(len(seq) for seq in seq_obj)) > 1:
            # print("Warning: Input seqs are different lengths. Adding gaps")
            seq_obj = add_gaps(seq_obj)

        records = [
            seq_astype(seq=seq, astype=SeqRecord, inplace=inplace) for seq in seq_obj
        ]

    # make msa from records
    return MultipleSeqAlignment(records, **kws)


def seq_astype(
    seq: SequencesType | Collection[SeqType] = None,
    astype: Annotated[type, SeqType, MultipleSeqAlignment] = SeqRecord,
    annotations: dict = None,
    **kws,
) -> SequencesType:
    """
    Parameters
    ----------
    seq: SeqType, MultipleSeqAlignment, Collection[SeqType]
        Sequence or collection of sequences or MSA to cast
    astype: Annotated[type, SeqType, MultipleSeqAlignment]
        Cast as this type. Default SeqRecord
    annotations: dict, optional
        Annotations for ret obj. If a list-like, then each element
        is looked up in `ser`. Default None.

    **kws
        Other kws to pass to seq_as_X functions: Takes: `mutable`, `append`,
        `inplace`

    """

    # parse anns
    # sort out MultipleSeqAlignment kws
    kws |= {"annotations": oed.default(annotations, {})}

    # return an MSA
    if issubclass(astype, MultipleSeqAlignment):
        return seq_as_msa(seq, **kws)

    # return as SeqRecord
    if issubclass(astype, SeqRecord):
        return seq_as_seqrecord(seq, **kws)

    # return as MutableSeq
    if issubclass(astype, (MutableSeq, Seq, str)):
        match seq:
            case SeqRecord():
                return astype(seq.seq)

            case Seq() | MutableSeq() | str():
                return astype(f"{seq}")

            case _:
                raise TypeError(
                    f"Input for target type {astype} must be SeqType", type(seq), seq
                )

    return TypeError("`astype` must be a SequencesType.", astype)
