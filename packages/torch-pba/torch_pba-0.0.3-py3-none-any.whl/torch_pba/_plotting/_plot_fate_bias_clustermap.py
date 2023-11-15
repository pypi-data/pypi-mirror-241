
# -- import packages: ---------------------------------------------------------
import ABCParse
import anndata
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -- set typing: --------------------------------------------------------------
from typing import Optional, Tuple, Dict


class FateBiasClusterMap(ABCParse.ABCParse):
    
    def __init__(self, adata: anndata.AnnData, fate_key: str = "Cell type annotation"):
        
        self.__parse__(locals(), public = [None])
        
    @property
    def fates(self):
        return self._adata.uns['fates']
        
    @property
    def fate_bias(self):
        return self._adata.obsm["fate_bias"]
    
    @property
    def S(self):
        return self._adata.obsm['S']
    
    @property
    def fate_bias(self):
        return self._adata.obsm['fate_bias']
    
    @property
    def sorted_fate_idx(self):
        
        if not hasattr(self, "_sorted_fate_idx"):
    
            self._sorted_fate_idx = np.array([])
            df = self._adata.obs.copy()

            for fate in self.fates:
                idx = df.loc[df[self._fate_key] == fate].index.to_numpy()
                self._sorted_fate_idx = np.append(self._sorted_fate_idx, idx)

        return self._sorted_fate_idx
    
    @property
    def fate_cmap(self):
        if not hasattr(self, "_fate_cmap"):
            self._fate_cmap = {fate: mcolors.rgb2hex(cm.tab20.colors[en]) for en, fate in enumerate(self.fates)}
        return self._fate_cmap
    
    @property
    def row_colors(self):
        return self._adata[self.sorted_fate_idx].obs[self._fate_key].map(self.fate_cmap).to_numpy()
    
    @property
    def column_colors(self):
        return [self.fate_cmap[fate] for fate in self.fates]
        
    def __call__(
        self,
        subset: Tuple[str, float] = None,
        title: Optional[str] = None,
        fate_cmap: Optional[Dict] = None,
    ):
        
        self.__update__(locals(), public = [None])
        
        if not subset is None:
            key, val = subset
            df = self._adata.obs.copy()
            _adata = self._adata[df.loc[df[key] == val].index]
            self.__init__(_adata)
                
        import seaborn as sns
                
        cg = sns.clustermap(
            self.fate_bias,
            figsize=(3, 6),
            cmap="Blues",
            xticklabels=self.fates,
            yticklabels=False,
            row_cluster=True,
            row_colors=self.row_colors,
            col_colors=self.column_colors,
            cbar_pos=(1, 0.4, 0.05, 0.2),
            vmin=0,
            vmax=1,
        )
        cg.ax_row_dendrogram.set_visible(False)
        if title is None:
            title = "{} cells".format(self.fate_bias.shape[0])
        cg.ax_col_dendrogram.set_title(title, fontsize=10)
        
def plot_fate_bias_clustermap(
    adata: anndata.AnnData,
    subset: Tuple[str, float] = ("Time point", 2),
    fate_key: Optional[str] = "Cell type annotation",
    title: Optional[str] = None,
    fate_cmap: Optional[Dict] = None,
    *args,
    **kwargs,
) -> None:
    
    fatebias_clustermap = FateBiasClusterMap(adata = adata, fate_key = fate_key)
    fatebias_clustermap(subset=subset, title = title, fate_cmap = fate_cmap)
