"""Alleles class"""

# from __future__ import annotations

# import pandas as pd

# class Alleles(pd.DataFrame):
#     """Alleles property class"""

#     def __init__(
#         self,
#         *args,
#         start_col: str = "POS",
#         end_col: str = "END_POS",
#         seq_col: str = "ALLELES",
#         **kws
#     ):
#         self._start_col = start_col
#         self._end_col = end_col
#         self._seq_col = seq_col
#         pd.DataFrame.__init__(*args, **kws)

#     @property
#     def start(self):
#         """Start position column values"""
#         return self._data[self._start_col]

#     @start.setter
#     def start(self, _) -> None:
#         raise AttributeError("Cannot set property `start`")

#     @property
#     def end(self):
#         """End position column values"""
#         return self._data[self._end_col]

#     @end.setter
#     def end(self, value) -> None:
#         raise AttributeError("Cannot set property `end`")

#     @property
#     def seqs(self):
#         """Seqs column values"""
#         return self._data[self._seq_col]

#     @seqs.setter
#     def seqs(self, value) -> None:
#         raise AttributeError("Cannot set property `seqs`")
