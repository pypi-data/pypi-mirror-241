
# -- import packages: ---------------------------------------------------------
import ABCParse
import numpy as np
import anndata


# -- set typing: --------------------------------------------------------------
from typing import Optional


# -- Operational class: -------------------------------------------------------
class ConfigureR(ABCParse.ABCParse):
    def __init__(
        self,
        adata: anndata.AnnData,
        source_sink_col: str = "Cell type annotation",
        baseline: float = -1.0e-03,
        *args,
        **kwargs,
    ):

        self.__configure__(locals())

    def __configure__(
        self, kwargs, ignore=["self"], private=["adata", "source_sink_col"]
    ):

        self.__parse__(kwargs=kwargs, ignore=ignore, private=private)

        self._df = self._adata.obs.copy()
        self._grouped = self._df.groupby(self._source_sink_col)
        self.R = np.zeros(len(self._adata)) + self.baseline

    def _as_list(self, key):
        if not isinstance(key, list):
            return list(key)
        else:
            return key

    def _configure_sinks_not_provided(self, sink_key):
        if not sink_key:
            self._sinks = [
                key for key in list(self._grouped.groups.keys()) if not key == self.source_key
            ]
        else:
            self._sinks = self._as_list(sink_key)

    def configure_source(self, key="undiff", val=0.2):

        idx = self._df.loc[self._df[self._source_sink_col] == key].index.astype(int)
        self.R[idx] = val

    def configure_sink(self, key=None, val=-0.2):

        self._configure_sinks_not_provided(key)

        for annot, annot_df in self._grouped:
            idx = annot_df.index.astype(int)
            if annot in self._sinks:
                self.R[idx] = val

    def __call__(
        self,
        source_key: str = "Undifferentiated",
        source_val: float = 0.2,
        sink_key: Optional[str] = None,
        sink_val: float = -0.2
    ):
        
        self.__parse__(locals())

        self.configure_source(source_key, source_val)
        self.configure_sink(sink_key, sink_val)

        return self.R


def configure_R(
    adata: anndata.AnnData,
    source_sink_col: str = "Cell type annotation",
    baseline: float = -1.0e-03,
    source_key: str = "Undifferentiated",
    source_val: float = 0.2,
    sink_key: Optional[str] = None,
    sink_val: float = -0.2,
    key_added: str = "R",
):
    """
    
    """
        
    r_param = ConfigureR(
        adata=adata,
        source_sink_col=source_sink_col,
        baseline=baseline,
    )

    adata.obs[key_added] = r_param(
        source_key=source_key,
        source_val=source_val,
        sink_key=sink_key,
        sink_val=sink_val,
    )
