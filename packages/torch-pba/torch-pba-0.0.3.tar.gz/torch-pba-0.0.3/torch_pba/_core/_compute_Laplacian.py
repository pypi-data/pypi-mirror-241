
import numpy as np
import ABCParse
from licorice_font import font_format
note = font_format("NOTE", ["BLUE"])
import anndata

class Laplacian(ABCParse.ABCParse):
    def __init__(
        self,
        adata: anndata.AnnData,
        adjacency_key: str = "adjacency",
    ):

        """
        adata: anndata.AnnData
        
        adjacency_key: str, default = "adjacency"
        """
        
        self.__parse__(locals(), public = [None])
        
    @property
    def n_cells(self):
        return self._adata.shape[0]
        
    @property
    def A(self):
        return self._adata.obsp[self._adjacency_key]

    def _configure_identity_matrix(self):
        if not hasattr(self, "_identity_matrix"):
            print(" - [{}] | Configuring identity matrix".format(note))
            self._identity_matrix = np.identity(self.n_cells)

    @property
    def identity_matrix(self):
        self._configure_identity_matrix()
        return self._identity_matrix

    def row_sum_normalize(self, A):

        print(" - [{}] | Computing row sum normalization of adjacency matrix".format(note))
        return A / A.sum(axis=1, keepdims=True)
    
    def __call__(self):
        return self.identity_matrix - self.row_sum_normalize(self.A)
    
def compute_Laplacian(
    adata: anndata.AnnData,
    adjacency_key: str = "adjacency",
    key_added: str = "Laplacian",
):
    
    """
    adata: anndata.AnnData
    adjacency_key: str = "adjacency"
    key_added: str = "Laplacian"
    """
    
    L = Laplacian(adata = adata, adjacency_key = adjacency_key)
    adata.obsp[key_added] = L()
    