"""For extracting genotypes and other data from vcfs"""

from __future__ import annotations
from collections.abc import Callable, Collection, Generator
from typing import Any, Union

import pandas as pd
import vcfpy

import oddsnends as oed

__all__ = [
    "VCF_COLS",
    "get_entry_data",
    "gts_to_long",
    "parse_records_generator",
]

VCF_COLS = ["CHROM", "POS", "ID", "REF",
            "ALT", "QUAL", "FILTER", "INFO", "FORMAT"]


def gts_to_long(fpath: str, value_name: str = "FORMAT/GT") -> pd.DataFrame:
    """Reads and melts bcftools-generated TSV to get GTs

    fpath: str
        TSV with columns CHROM, POS, REF, and SAMPLES with GTs as values

    Returns:
        pd.DataFrame with columns CHROM, POS, END_POS, SAMPLE, REF and VALUE
    """
    melted = pd.read_csv(fpath, sep="\t").melt(
        id_vars=["CHROM", "POS", "REF"],
        var_name="SAMPLE",
        value_name=value_name,
        )
    melted["END_POS"] = melted["POS"] + melted["REF"].apply(len) - 1
    oed.reorder_cols(
        melted, first=["CHROM", "POS", "END_POS", "SAMPLE"], inplace=True)

    return melted


def get_entry_data(
    rec: vcfpy.Record,
    sample: str,
    field: tuple[str],
    custom: dict[str, Callable] = None,
    func_args: dict[str, Collection] = None,
    func_kws: dict[str, dict] = None,
) -> Any:
    """Extract data from vcfpy.Record entry"""
    custom = oed.default(custom, {}).copy()
    custom.setdefault(field, lambda _: None)

    func_args = oed.default(func_args, {})
    func_kws = oed.default(func_kws, {})

    try:
        value = getattr(rec, field[0])

        # subfield, e.g. for INFO or FILTER
        return value[field[1]]

    except AssertionError as error:
        return error.args[0]

    except AttributeError:  # custom/calculated column
        return custom[field](
            rec, sample, *func_args.get(field, []), **func_kws.get(field, {})
        )

    except IndexError:  # no subfield. IndexError > TypeError
        return value

    except TypeError:  # rec.FORMAT is a list of Calls
        return rec.call_for_sample[sample].data[field[1]]


def parse_records_generator(
    vcf: str,
    chrom: str,
    start: int = 1,
    end: int = None,
    fields_list: list[str] = None,
    samples: Collection[str] = None,
    custom: dict[str, Callable] = None,
    end_pos_closed: bool = True,
    func_args: dict[str, Collection] = None,
    func_kws: dict[str, dict] = None,
) -> Generator[list]:
    """Parses vcfpy.Records and generates entries for each record-sample

    Note:
    custom: dict[str, Callable]
        field as key, function as value. Function takes record, sample as
        first two positional args, and then *func_args, **func_kws

    """
    #TODO: Streamline fields parsing
    def _tupelize_keys(dct: dict, inplace: bool = True) -> Union[dict, None]:
        non_tuple_keys = [k for k in dct if not isinstance(k, tuple)]
        updated = dct if inplace else dct.copy()
        for k in non_tuple_keys:
            updated[(k,)] = updated.pop(k)
        if not inplace:
            return updated

    if isinstance(start, dict):
        start = start.get(chrom, 1)

    if isinstance(end, dict):
        end = end.get(chrom, None)

    # set defaults
    custom = oed.default(custom, {})
    func_args = oed.default(func_args, {})
    func_kws = oed.default(func_kws, {})

    custom = {
        "END_POS": (lambda rec, _, shift=0: rec.POS + len(rec.REF) + shift),
        "SAMPLE": (lambda _, sample: sample),
    } | custom

    func_kws.setdefault("END_POS", {"shift": -1 if end_pos_closed else 0})

    for func in custom:
        func_args.setdefault(func, [])
        func_kws.setdefault(func, {})

    _tupelize_keys(custom)
    _tupelize_keys(func_args)
    _tupelize_keys(func_kws)

    with vcfpy.Reader.from_path(vcf) as reader:
        # check and parse fields
        if fields_list is None:
            # get all fields
            fields = [(fd,) for fd in VCF_COLS if fd not in ["INFO", "FORMAT"]]
            fields.extend(("INFO", fd) for fd in reader.header.info_ids())
            fields.extend(("FORMAT", fd) for fd in reader.header.format_ids())

        else:
            fields = [
                tuple(oed.parse_literal_eval(d) for d in fd.split("/", 1))
                for fd in fields_list
            ]
            # check that fields are valid
            try:
                for fd in fields:
                    match fd[0]:
                        case "INFO":
                            assert fd[1] in reader.header.info_ids(), fd
                        case "FORMAT":
                            assert fd[1] in reader.header.format_ids(), fd
                        case _ if fd[0] in VCF_COLS:
                            pass
                        case _ if fd in custom:
                            pass
                        case _:
                            raise ValueError(fd)
            except (AssertionError, ValueError) as error:
                raise ValueError("Bad field", error.args[0]) from error

        # default get all samples
        samples = oed.default(samples, reader.header.samples.names)

        for rec in reader.fetch(chrom, start - 1, end):
            for sample in samples:
                yield [
                    get_entry_data(
                        rec,
                        sample,
                        fd,
                        custom=custom,
                        func_args=func_args,
                        func_kws=func_kws,
                    )
                    for fd in fields
                ]
    return