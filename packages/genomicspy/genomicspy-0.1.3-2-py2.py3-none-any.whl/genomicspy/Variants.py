"""Variants Classes"""

# Variants.py

# %%
from __future__ import annotations
import dataclasses as datacls
from collections.abc import Hashable, Sequence
from dataclasses import dataclass
from logging import Logger, getLogger
from typing import Annotated

import pandas as pd
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqIO import SeqRecord
from vcfpy import Reader

import oddsnends as oed
from genomicspy.alleles.tools import pos_conditions
from genomicspy.main import seq_astype
from genomicspy.trim import trim_alleles
from genomicspy.vcf import parse_records_generator

__all__ = [
    "Variants",
    "MSAVariants",
    "VCFVariants",
]

# StrandType = type("StrandType", (str,), {"options": ["+", "-"]})

# %%
@dataclass(init=True, repr=True, eq=False, order=False, kw_only=False,
           slots=True)
class Variants:
    """
    Required parameters
    ===================
    refseq: Seq or SeqRecord
        Reference sequence. Use Seq or SeqRecord to conserve memory
    chrom: str
        Chromosome name

    Optional parameters
    ===================
    Region
    ------
    start: int, optional
        Start position. Default None (i.e. from beginning)
    end: int, optional
        End position. Default None (i.e. to end of sequence)
    name: str, optional
        Name of region
    strand: str ('+' or '-'), optional
        Strand of region. Default None

    Indexing
    --------
    gt_i: int, optional
        Index in genotype (GT) field. Default 0
    indexing: int
        0- or 1-indexing of positions. default 1
    interval_type: oed.IntervalType, default "closed"
        Interval types for positions. See help(IntervalType)

    Column labels
    -------------
    start_col: Hashable
        Column label for start positions. Default "POS"
    end_col: Hashable
        Column label for end positions. Default "END_POS"
    seq_col: Hashable
        Column label for sequences. Default "ALLELES"
    """

    refseq: Seq | SeqRecord
    chrom: str
    start: int = None
    end: int = None
    name: str = None
    strand: Annotated[str, '+', '-'] = datacls.field(
        default=None, metadata={"type": "<'+','-'>"})

    _ = datacls.KW_ONLY

    # indexing settings
    gt_i: int = datacls.field(repr=False, default=0)
    indexing: int = datacls.field(repr=False, default=None)
    interval_type: oed.IntervalType = datacls.field(repr=False, default=None)

    # column labels
    start_col: Hashable = datacls.field(repr=False, default="POS")
    end_col: Hashable = datacls.field(repr=False, default="END_POS")
    seq_col: Hashable = datacls.field(repr=False, default="ALLELES")

    logger_name: str = datacls.field(default=None)

    # to be computed later
    _alias_crossrefs: pd.DataFrame = datacls.field(
        init=False, repr=False, default=None
    )
    _aliased_genotypes: pd.DataFrame = datacls.field(
        init=False, repr=False, default=None
    )
    _alleles: pd.DataFrame = datacls.field(
        init=False, repr=False, default=None
    )
    _variants_locs: pd.Index = datacls.field(
        init=False, repr=False, default=None
    )
    _ivrs_locs: pd.Index = datacls.field(
        init=False, repr=False, default=None
    )
    _genotypes: pd.DataFrame = datacls.field(
        init=False, repr=False, default=None
    )
    _trimmed: pd.DataFrame = datacls.field(
        init=False, repr=False, default=None
    )

    @classmethod
    def fields(cls, pprint=False) -> tuple[str] | tuple[datacls.Field]:
        """Fields of this dataclass"""
        if pprint:
            return tuple((
                f"{fd.name}: {fd.metadata.get('type', fd.type)}"
                for fd in datacls.fields(cls)
            ))
        return datacls.fields(cls)

    # Optional
    def __post_init__(self):
        # init as kw opt initially to let optional start, end, ... be first
        required_kw_only = [
            "start_col",
            "end_col",
            "seq_col",
            "indexing",
            "interval_type",
        ]
        for kw in required_kw_only:
            if getattr(self, kw) is None:
                raise TypeError(f"{kw} cannot be None.")
        if self.logger_name is not None:
            pad = len(str(len(self.refseq)))
            self.logger_name = f"{{}}{{}}:{{:0{pad}d}}-{{:0{pad}d}}".format(
                oed.default(self.name, "", f"{self.name} - "),
                self.chrom,
                oed.default(self.start, 1),
                oed.default(self.end, len(self.refseq))
            )

    # other
    def copy(self) -> Variants:
        """Make a shallow copy of the object"""

        # get kws/slots
        init_kws = {}
        for fd in self.field_names:
            val = getattr(self, fd.name)
            try:
                init_kws[fd] = val.copy()
            except AttributeError:
                init_kws[fd] = val

        copy = self.__class__(**init_kws)

        # make shallow copies of dataframes
        computed_attrs = [
            "_alleles",
            "_genotypes",
            "_alias_crossrefs",
            "_aliased_genotypes",
            "_trimmed",
        ]
        for attr in computed_attrs:
            try:
                setattr(copy, attr, getattr(self, attr))
            except AttributeError:
                pass
        return copy

    def gen_genotypes(self) -> pd.DataFrame:
        """Generate genotypes dataframe"""
        raise NotImplementedError

    def gen_alleles(self, inplace: bool = True, **kws) -> Variants | pd.DataFrame:
        """Generate alleles

        Parameters
        ----------
        self:
            VCFVariants object
        astype: type, optional
            Output type of alleles, one of SequencesType. Defaults to
            MultipleSeqAlignment
        inplace: bool, optional
            Update self with start, end (if provided) and alleles
        Returns
        -------
        None or pd.DataFrame
            None if inplace=True (allow for chaining). if inplace=False, then
            returns pd.DataFrame of alleles

        `alleles` is a DataFrame with
            - index "CHROM", self._start_col, self._end_col
            - values self.seq_col
        """
        self.logger.debug("Generating alleles")

        loc_cols = ["CHROM", self.start_col, self.end_col]
        variants = self.gen_variants(**kws)

        ivrs = self.gen_ivrs(variants)

        # do this after calculating ivrs
        variants.set_index(loc_cols, inplace=True)
        ivrs.set_index(loc_cols, inplace=True)

        alleles = self.combine_ivrs_variants(variants, ivrs)


        self.logger.debug("Done generating alleles.")

        if inplace:
            self._variants_locs = variants.index
            self._ivrs_locs = ivrs.index
            self._alleles = alleles
            return self

        return alleles

    def gen_variants(self) -> pd.DataFrame:
        """Generate variants as dataframe"""
        raise NotImplementedError

    def gen_ivrs(
        self,
        var_intervals: pd.DataFrame | Sequence[tuple[int, int]] = None,
        start: int = None,
        end: int = None,
    ) -> pd.DataFrame:
        """Calculate intervariant (aka. invariant) region POS and END_POS

        Parameters
        ------------
        var_intervals: pd.DataFrame or sequence of 2-tuples of ints
            with variant intervals corresponding to variant ranges.

        start: int, optional
            Start position in refseq. Default self.start. If self.start is
            None, then defaults to beginning

        end: int, optional
            Start position in refseq. Default self.end. If self.end is None,
            then defaults to end of seq

        `start` and `end` must be consistent with self.indexing and
        self.interval_type

        Returns
        -------
        pd.DataFrame with cols
            - 'CHROM': str
            - start col: int
            - end col: int
            - seq col: SeqType or MultipleSeqAlignment
        """
        self.logger.debug("Generating invariant regions")
        # define vars from args
        start = oed.defaults(start, self.start, self.indexing)
        end = oed.defaults(end, self.end, len(self.refseq) - 1 + self.indexing)

        if len(var_intervals) == 0:
            ivrs = pd.DataFrame(
                [(start, end)], columns=[self.start_col, self.end_col])

        else:
            self.logger.debug("Calculating intervals")
            # calculate the ivr positions and merge into ranges
            ivrs = oed.setops_ranges(
                var_intervals,
                [(start, end)],
                col_from=self.start_col,
                col_to=self.end_col,
                how="right_only",
                interval_type=self.interval_type,
            )

        self.logger.debug("Getting sequences")
        # get allele sequences
        # shift intervals
        if len(ivrs) > 0:
            # shift to left-closed for python slicing
            shift_start, shift_end = oed.shift_interval(
                self.interval_type, "left", self.indexing, 0
            )

            seqs = ivrs.apply(
                lambda ser: self.refseq[
                    ser[self.start_col] + shift_start
                    : ser[self.end_col] + shift_end
                ],
                axis=1,
            )
        else:
            seqs = None

        ivrs = ivrs.assign(**{"CHROM": self.chrom, self.seq_col: seqs})
        self.logger.debug("IVRs generated.")
        return ivrs

    def combine_ivrs_variants(
        self,
        variants: pd.DataFrame = None,
        ivrs: pd.DataFrame = None,
    ) -> pd.DataFrame:
        """Concatenate and format variant and invariant data"""

        def _update_seq_astype(ser: pd.Series) -> pd.Series:
            """Apply function `seq_astype`"""

            # annotate msa with loc info
            annotations = dict(zip(
                ("CHROM", self.start_col, self.end_col), ser.name))

            ser[self.seq_col] = seq_astype(
                ser[self.seq_col],
                MultipleSeqAlignment,
                annotations=annotations,
                inplace=True,  # avoid making copies/using extra memory/time
                append=True,
            )
            return ser

        self.logger.debug("Combining IVRs and variants")

        alleles = pd.concat(
            [variants, ivrs]).apply(_update_seq_astype, axis=1).sort_index()

        self.logger.debug("Combining done.")

        return alleles

    def alias_identical_gts(
        self, inplace: bool = True
    ) -> Variants | tuple[pd.DataFrame, pd.DataFrame]:
        """Group samples with identical genotypes and make aliases.

        A wrapper for oddsnends.group_identical_rows

        Returns
        -------
        None or (pd.DataFrame, pd.DataFrame)
            None if inplace=True. if inplace=False, returns deduplicated
            alleles and cross-reference table
        """
        loc_cols = ["CHROM", self.start_col, self.end_col]

        # remove unwanted columns
        # group rows
        # perform aliasing and cross-reference
        aliased, xrefs = (
            oed.drop_labels(self._genotypes, keep=[*loc_cols, "SAMPLE", "GT"])
            .pipe(oed.group_identical_rows, id_col="SAMPLE", value_col="GT")
            .pipe(lambda ser: oed.rank_sort(
                ser,
                lambda x: 1 if isinstance(x, Hashable) else len(x),
                ascending=[False, *(True for _ in ser.index.names)]
            ))
            .pipe(oed.alias_crossref, "GT_ALIAS", "GT")
        )
        #FIXME CHECK s

        # multiindex
        if isinstance(aliased.columns[0], tuple):
            aliased.columns = pd.MultiIndex.from_tuples(
                aliased.columns, names=loc_cols)

        # stack index and format
        aliased_genotypes = (
            aliased
            .stack(loc_cols)
            .astype(int)
            .to_frame("GT")
            .reorder_levels([*loc_cols, "GT_ALIAS"])
        )

        if inplace:
            self._aliased_genotypes = aliased_genotypes
            self._alias_crossrefs = xrefs
            return self

        return aliased_genotypes, xrefs


    def trim_alleles(
        self, inplace: bool = True, **kws
    ) -> Variants | pd.DataFrame:
        """Trim alleles, removing overhangs. Wrapper for trim.trim_alleles()

        Parameters
        ----------
        self:  Variants
        inplace: bool, optional
            Update self
        replace: bool, optional
            Replace seq_col (of alleles) with trimmed seqs. Default True
        **kws
            Additional kws passed to `trim.trim_alleles()`. See documentation.
            kws from self:  start, end, start_col, end_col, interval_type

        Returns
        -------
        self or pd.DataFrame of trimmed alleles
        """

        trimmed = (
            trim_alleles(
                self._alleles,
                start=self.start,
                end=self.end,
                start_col=self.start_col,
                end_col=self.end_col,
                interval_type=self.interval_type,
                **kws
            )
        )
        trimmed_col = self.seq_col if kws.get("replace", False) else kws.get(
            "trimmed_col", self.seq_col)

        # compute reverse-complement for negative strand seqs
        if self.strand == "-":
            trimmed[f"{trimmed_col}_RC"] = trimmed[trimmed_col].apply(
                lambda msa: [rec.seq.reverse_complement(
                    inplace=False) for rec in msa]
            )

        if inplace:
            self._trimmed = trimmed
            return self

        return trimmed



    ## Properties ##

    @property
    def field_names(self) -> tuple[str]:
        """Names of fields of this dataclass"""
        return tuple(fd.name for fd in datacls.fields(self))

    @field_names.setter
    def field_names(self, _):
        raise AttributeError("Cannot set property field_names")

    @property
    def logger(self) -> Logger:
        """logging.Logger"""
        return getLogger(self.logger_name)

    @logger.setter
    def logger(self, _):
        raise AttributeError(
            "Cannot set logger property. Please set self.logger_name"
        )

    # Computed values. Cannot be manually set by user
    @property
    def alleles(self) -> pd.DataFrame:
        """Generated alleles"""
        if self._alleles is None:
            raise AttributeError("Please run self.gen_alleles() to init.")
        return self._alleles


    @alleles.setter
    def alleles(self, value: pd.DataFrame):
        self._alleles = value


    @alleles.deleter
    def alleles(self):
        self._alleles = None

    @property
    def variants(self) -> pd.DataFrame:
        """Variant entries in alleles"""
        return self._alleles.loc[self._variants_locs]

    @property
    def ivrs(self) -> pd.DataFrame:
        """Invariant allele entries in alleles"""
        return self._alleles.loc[self._ivrs_locs]


    @property
    def variants_locs(self) -> pd.MultiIndex:
        """Variant loci in alleles"""
        return self._variants_locs


    @property
    def ivrs_locs(self) -> pd.MultiIndex:
        """Invariant loci in alleles"""
        return self._ivrs_locs


    @property
    def start_pos(self) -> pd.Index:
        """Start positions of alleles"""

        # use property to raise AttributeError if no alleles df
        return self.alleles.index.get_level_values(self.start_col)

    @property
    def end_pos(self) -> pd.Index:
        """End positions of alleles"""

        # use property to raise AttributeError if no alleles df
        return self.alleles.index.get_level_values(self.end_col)

    @property
    def genotypes(self) -> pd.DataFrame:
        """Generated genotypes

        pd.DataFrame with
            - index "CHROM" self.start_col, self._end_col, "SAMPLE"
            - columns "GT"
            - values GT
        """
        if self._genotypes is None:
            raise AttributeError("Please run self.gen_genotypes() to init.")
        return self._genotypes

    @genotypes.setter
    def genotypes(self, value: pd.DataFrame):
        self._genotypes = value

    @genotypes.deleter
    def genotypes(self):
        self._genotypes = None

    @property
    def alias_crossrefs(self):
        """Generated alias_crossrefs"""
        if self._alias_crossrefs is None:
            raise AttributeError("Please run self.alias_crossrefs() to init.")
        return self._alias_crossrefs

    @alias_crossrefs.setter
    def alias_crossrefs(self, value: pd.DataFrame):
        self._alias_crossrefs = value

    @alias_crossrefs.deleter
    def alias_crossrefs(self):
        self._alias_crossrefs = None

    @property
    def aliased_genotypes(self) -> pd.DataFrame:
        """Generated aliased_genotypes

        pd.DataFrame with
            - index "CHROM" self.start_col, self._end_col, "GT_ALIAS"
            - columns "GT"
            - values GT
        """
        if self._aliased_genotypes is None:
            raise AttributeError("Please run self.alias_crossrefs() to init.")
        return self._aliased_genotypes

    @aliased_genotypes.setter
    def aliased_genotypes(self, value: pd.DataFrame):
        self._aliased_genotypes = value

    @aliased_genotypes.deleter
    def aliased_genotypes(self):
        self._aliased_genotypes = None

    @property
    def trimmed(self):
        """Trimmed alleles dataframe"""
        if self._trimmed is None:
            raise AttributeError("Please run self.trim_alleles() to init.")
        return self._trimmed

    @trimmed.setter
    def trimmed(self, value: pd.DataFrame):
        self._trimmed = value

    @trimmed.deleter
    def trimmed(self):
        self._trimmed = None


@dataclass(slots=True)
class MSAVariants(Variants):
    """A set of variants and genotypes from variant MSAs and genotypes.
    See Variants class documentation.

    gt_files: pd.DataFrame
        DataFrame with columns `CHROM`, start_col, end_col and `fpath`.
        Filepaths are of pickled DataFrames with cols `CHROM`, start_col,
        end_col, `SAMPLE`, `REF`, `FORMAT/GT`, [and other fields]
    """
    gt_files: pd.DataFrame = datacls.field(repr=False, default=None)

    def __post_init__(self):
        self.logger.warning("MSAVariants has not been fully tested!")
        return super().__post_init__()

    def filter_genotype_files(self, gt_files: pd.DataFrame,
                              inplace: bool = True) -> MSAVariants | pd.DataFrame:
        """Filter for genotype files within a given chromsome and range.

        Parameters
        ----------
        gt_files: pd.DataFrame
            See MSAVariants documentation.

        inplace: bool, optional
            Updates object inplace. Default True

        Returns
        -------
        self or pd.DataFrame:  self if inplace=True, else the filtered gt files
        """
        #   gt_files: pd.DataFrame with columns CHROM, start_col, end_col and fpath to
        # pickled dataframes with cols CHROM, start_col, end_col, SAMPLE, REF,
        # FORMAT/GT, [and other fields]

        # get relevant genotype files
        left_cond, right_cond = pos_conditions(self.interval_type)

        gt_files = gt_files.loc[
            (
                (gt_files["CHROM"] == self.chrom)
                & gt_files[self.start_col].apply(left_cond, ref=self.start)
                & gt_files[self.end_col].apply(right_cond, ref=self.end)
            ),
            "fpath",
        ]
        if inplace:
            self.gt_files = gt_files
            return self
        return gt_files

    def copy(self) -> MSAVariants:
        """Make a shallow copy of the object"""
        return super().copy()

    def gen_genotypes(
        self,
        fields: Hashable | Sequence[Hashable] = None,
        inplace: bool = True,
    ) -> MSAVariants | pd.Series | pd.DataFrame:
        """Generate genotypes

        Parameters
        ----------
        self: MSAVariants
        fields: label or sequence of labels, optional
            Column labels to get from genotypes table in addition to
            "CHROM", self.start_col, self.end_col, "SAMPLE", "FORMAT/GT"
        Returns
        -------
        pd.DataFrame
            genotypes as a long frame (if more than one field) with
            - index CHROM, start_col, end_col, SAMPLE
            - values FIELDS
        """

        self.logger.debug("Generating genotypes")

        # defaults
        if samples is None:
            samples = []

        if fields is None:
            fields = []
        elif isinstance(fields, Hashable):
            fields = [fields]

        # add mandatory fields
        fields = ["CHROM", self.start_col, self.end_col, "SAMPLE", "FORMAT/GT"
                  ] + fields

        # conditions for getting subset of gt files and genotypes
        left_cond, right_cond = pos_conditions(self.interval_type)

        #TODO: clean up assertion
        try:
            assert len(self.gt_files) > 0, "No objects to concatenate"
            gts = (
                self.gt_files.apply(pd.read_pickle)
                .pipe(lambda ser: ser.loc[ser.apply(len) > 0])
                .pipe(lambda ser: pd.concat(ser.values))
            )
        except (AssertionError, ValueError) as error:
            if error.args[0] == "No objects to concatenate":
                # init empty dataframe
                gts = pd.DataFrame(columns=fields)
            else:
                raise error

        # amend fields list of genotypes col is named GT instead of FORMAT/GT
        if ("GT" in gts.columns) and ("FORMAT/GT" not in gts.columns):
            fields[fields.index("FORMAT/GT")] = "GT"

        # drop unwanted columns
        oed.reorder_cols(gts, fields, inplace=True)

        drop_gts_index = gts.index[
            ~(
                (gts["CHROM"] == self.chrom)
                & gts[self.end_col].apply(left_cond, ref=self.start)
                & gts[self.start_col].apply(right_cond, ref=self.end)
                & gts["SAMPLE"].isin(samples)
            )
        ]
        # get only relevant GTs
        gts.drop(drop_gts_index, inplace=True)
        gts.sort_index(inplace=True)
        self.logger.debug("Done generating genotypes")

        if inplace:
            self._genotypes = gts
            return self

        return gts

    def gen_variants(self, variant_msas: pd.DataFrame = None) -> pd.DataFrame:
        """Get subset of variants from dataframe"""
        # conditions for getting subset of variants
        left_cond, right_cond = pos_conditions(self.interval_type)

        variants = variant_msas.loc[
            (variant_msas["CHROM"] == self.chrom)
            & variant_msas[self.start_col].apply(left_cond, ref=self.start)
            & variant_msas[self.end_col].apply(right_cond, ref=self.end)
        ]
        return variants


@dataclass
class VCFVariants(Variants):
    """A set of variants and genotypes from VCF. See Variants class
    documentation
    """

    vcf: str = None

    # re-define defaults
    gt_i: int = datacls.field(repr=False, default=0)
    indexing: int = datacls.field(repr=False, default=1)
    interval_type: oed.IntervalType = datacls.field(
        repr=False, default="closed")

    def __post_init__(self):
        if self.vcf is None:
            raise TypeError("vcf is required")
        return super().__post_init__()

    def copy(self) -> VCFVariants:
        """Make a shallow copy of the object"""
        return super().copy()

    def gen_genotypes(
        self,
        samples: Sequence[str] = None,
        fields: Hashable | Sequence[Hashable] = None,
        inplace: bool = True,
    ) -> VCFVariants | pd.Series:
        """Parse and generate genotypes dataframe from VCF

        Parameters
        ----------
        self: VCFVariants
        samples: sequence of strings, optional
            Samples to process. Default all
        fields: Hashable or sequence of Hashables, optional
            Fields to get from VCF. INFO and FORMAT fields should be written as
            'INFO/X' or 'FORMAT/X'. 'SAMPLE' and 'FORMAT/GT' are added
            automatically. Default is:
                CHROM, start_col, end_col, REF, SAMPLE, FORMAT/GT.
        inplace: bool, optional
            Write genotypes to object in place. Default True
        **kws:
            Other kws passed to `genomicspy.vcf.parse_records_generator()`.
            Excludes start, end, fields_list, end_pos_closed.
        Returns
        -------
        None if inplace=True, or pd.Series of genotypes if inplace=False
        `genotypes` is a long pd.Series with:
            - index CHROM, start_col, end_col, SAMPLE
            - values GT

        """
        self.logger.debug("Generating genotypes")

        # default fields
        if fields is None:
            fields = [
                "CHROM",
                self.start_col,
                self.end_col,
                "REF",
                "SAMPLE",
                "FORMAT/GT",
            ]
        elif isinstance(fields, Hashable):
            fields = [fields]
        else:
            if "SAMPLE" not in fields:
                fields.append("SAMPLE")
            if "FORMAT/GT" not in fields:
                fields.append("FORMAT/GT")

        # default samples
        if samples is None:
            with Reader.from_path(self.vcf) as reader:
                samples = reader.header.samples.names

        rec_generator = parse_records_generator(
            self.vcf,
            self.chrom,
            start=self.start,
            end=self.end,
            fields_list=fields,
            samples=samples,
            end_pos_closed=oed.IntervalType.isclosed(
                self.interval_type, False),
        )
        gts = pd.DataFrame(rec_generator, columns=fields)

        gts["FORMAT/GT"].update(
            gts["FORMAT/GT"].apply(lambda gt: gt[self.gt_i]).astype(int)
        )

        # handle empty dataframe (no variant records)
        if len(gts) == 0:  # no variants, in GT. assume all ref GT
            self.logger.warning(
                "%s:%d-%d No VCF entries for any samples",
                self.chrom,
                self.start,
                self.end,
            )

            # assume all ref GT
            gts = pd.DataFrame(
                [(self.chrom, self.start, self.end, s, 0) for s in samples],
                columns=fields,
            )

        gts.rename({"FORMAT/GT": "GT"}, axis=1, inplace=True, errors="ignore")

        gts.set_index(["CHROM", self.start_col,
                      self.end_col, "SAMPLE"], inplace=True)

        self.logger.debug("Done generating genotypes")
        if inplace:
            self._genotypes = gts
            return self

        return gts

    def gen_variants(self) -> pd.DataFrame:
        """Read in variants"""
        self.logger.debug("Generating variants")
        # get start and end
        start = oed.default(self.start, 1)
        end = oed.default(self.end, None)

        # Shift from lower (since we add len(rec), it's technically the 'lower'
        # interval type. The shift target interval_type is self.interval_type
        shift_left, shift_right = oed.shift_interval(
            "lower", self.interval_type, 1, self.indexing
        )

        with Reader.from_path(self.vcf) as reader:
            self.logger.debug("Reading VCF")
            variants = pd.DataFrame.from_records(
                (
                    (
                        rec.CHROM,
                        rec.POS + shift_left,
                        rec.POS + len(rec.REF) + shift_right,
                        [rec.REF, *[alt.value for alt in rec.ALT]],
                    )
                    for rec in reader.fetch(self.chrom, start - 1, end)
                    # vcfpy is 0-indexed, left-open
                ),
                columns=["CHROM", self.start_col, self.end_col, self.seq_col],
            ).sort_values(["CHROM", self.start_col, self.end_col])

        self.logger.debug("Variants generated")

        return variants
