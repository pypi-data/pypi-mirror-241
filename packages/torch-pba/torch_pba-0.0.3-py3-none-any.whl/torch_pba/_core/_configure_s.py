
# -- import packages: ---------------------------------------------------------
import ABCParse
import numpy as np
from annoyance import kNN
import anndata


# -- Operational class: -------------------------------------------------------
class ConfigureS(ABCParse.ABCParse):
    def __init__(
        self,
        adata: anndata.AnnData,
        fate_key: str = "Cell type annotation",
        *args,
        **kwargs,
    ):

        self.__parse__(locals(), public = [None])
        self._configure_graph()
        self._grouped = self._adata.obs.groupby(self._fate_key)

    def _configure_graph(self):

        self.Graph = kNN(self._adata)
        self.Graph.build()

    def _configure_fates(self):
        if not hasattr(self, "_fates"):
            self._fates = self._adata.obs[self._fate_key].unique().tolist()
            self._adata.uns['fates'] = self._fates

    @property
    def fates(self):
        self._configure_fates()
        return self._fates

    @property
    def n_cells(self):
        return self._adata.shape[0]

    @property
    def n_fates(self):
        return len(self.fates)

    @property
    def S_init(self):
        return np.zeros([self.n_cells, self.n_fates])

    def __call__(self, sink_val=10, use_key="X_pca", potential_key="V"):

        # TODO-POTENTIALLY: supply a dict mapping fates to sink values

        self.S = self.S_init.copy()

        for n, fate in enumerate(self.fates):
            fate_df = self._grouped.get_group(fate)
            # requires a consistent index (no subsetting adata without resetting index)
            nn_idx = self.Graph.query(
                self._adata[fate_df[potential_key].idxmin()].obsm[use_key]
            ).flatten()
            sink_idx = self._adata[nn_idx.flatten()].obs.index.astype(int)
            self.S[sink_idx, n] = sink_val

        return self.S
    
def configure_S(
    adata: anndata.AnnData,
    fate_key: str = "Cell type annotation",
    sink_val: float = 10,
    use_key: str = "X_pca",
    potential_key: str = "V",
    key_added: str = "S",
    *args,
    **kwargs,
):
    """
    Configure S.
    """

    s_config = ConfigureS(adata = adata, fate_key=fate_key)
    adata.obsm[key_added] = s_config(
        sink_val=sink_val, use_key=use_key, potential_key=potential_key
    )
