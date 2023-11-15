
import numpy as np
import anndata

from .._utils import row_sum_normalize
import ABCParse

# ignoring warnings because there are div. by zeros which are expected.
import warnings
warnings.filterwarnings("ignore")


class FateBias(ABCParse.ABCParse):
    def __init__(
        self,
        adata: anndata.AnnData,
        D: float = 1.0,
        adjacency_key: str = "adjacency",
        potential_key: str = "V",
        S_key: str = "S"
    ) -> None:
        """
        Parameters
        ----------
        
        Returns
        -------
        None
        """

        self.__parse__(locals(), private=["adjacency_key", "potential_key", "S_key"])

    def _configure_adjacency(self):
        if not hasattr(self, "_A"):
            self._A = self.adata.obsp[self._adjacency_key]

    def _configure_potential(self):

        if not hasattr(self, "_V"):
            self._V = self.adata.obs[self._potential_key]
            self._V = self._V / self.D

    @property
    def n_cells(self):
        return self.adata.shape[0]

    @property
    def n_fates(self):
        return self.S.shape[1]

    @property
    def A(self):
        self._configure_adjacency()
        return self._A

    @property
    def V(self):
        self._configure_potential()
        return self._V

    @property
    def S(self):
        return self.adata.obsm[self._S_key]

    def _compute_P(self):

        if not hasattr(self, "_P"):
            Vx, Vy = np.meshgrid(self.V, self.V)
            self._P = self.A * np.exp(np.minimum(Vy - Vx, 400))

    @property
    def P(self):
        self._compute_P()
        return self._P

    @property
    def fate_by_cell(self):
        return np.zeros((self.n_fates, self.n_cells))

    @property
    def fate_identity(self):
        return np.identity(self.n_fates)

    @property
    def fate_init(self):
        return np.hstack((self.fate_by_cell, self.fate_identity))

    @property
    def PS(self):
        return np.hstack((self.P, self.S))

    def __call__(self):
        bigP = row_sum_normalize(np.vstack((self.PS, self.fate_init)))
        Q = bigP[: self.n_cells, : self.n_cells]
        RR = bigP[: self.n_cells, self.n_cells :]
        return np.linalg.solve(np.identity(Q.shape[0]) - Q, RR)  # B


def compute_fate_bias(
    adata: anndata.AnnData,
    D: float = 1.0,
    adjacency_key: str = "adjacency",
    potential_key: str = "V",
    S_key: str = "S",
    key_added: str = "fate_bias",
) -> None:

    """
    Compute per-cell fate bias and add to adata.obsm.
    
    Parameters
    ----------
    adata: anndata.AnnData

    D: float, default = 1.0

    adjacency_key: str, default = "adjacency"

    potential_key: str, default = "V"

    S_key: str, default = "S"
    
    Returns
    -------
    None, updates passed adata.
    """

    fb = FateBias(
        adata,
        D=D,
        adjacency_key=adjacency_key,
        potential_key=potential_key,
        S_key=S_key,
    )
    adata.obsm[key_added] = fb()
