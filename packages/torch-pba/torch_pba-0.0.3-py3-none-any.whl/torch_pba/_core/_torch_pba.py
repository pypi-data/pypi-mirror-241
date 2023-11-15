
import anndata
import ABCParse
import annoyance
from autodevice import AutoDevice

from ._compute_distance_matrix import compute_distance_matrix
from ._construct_kNN_graph import construct_kNN_graph
from ._compute_adjacency_matrix import compute_adjacency_matrix
from ._compute_Laplacian import compute_Laplacian
from ._compute_potential import compute_potential
from ._compute_fate_bias import compute_fate_bias
from ._compute_mean_first_passage_time import compute_mean_first_passage_time
from ._configure_s import configure_S


class PBA(ABCParse.ABCParse):
    def __init__(self, adata: anndata.AnnData):

        self.__parse__(locals())

    def build_kNN(self, graph_idx=None, use_key: str = "X_pca", k: int = 10, key_added: str = "edges"):

        construct_kNN_graph(self.adata, graph_idx=graph_idx, k=k, key_added=key_added, use_key="X_pca")

    def compute_Laplacian(
        self,
        edges_key: str = "edges",
        adjacency_key: str = "adjacency",
        key_added: str = "Laplacian",
    ):

        compute_adjacency_matrix(self.adata, edges_key=edges_key)
        compute_Laplacian(self.adata, key_added=key_added)

    def compute_potential(self, key_added: str = "V"):
        
        compute_potential(self.adata, key_added=key_added)
        
    def compute_fate_bias(self, D=1.0, adjacency_key="adjacency", potential_key="V", S_key="S"):
        
        compute_fate_bias(self.adata, D=D, adjacency_key=adjacency_key, potential_key=potential_key, S_key=S_key)

    def compute_mean_first_passage_time(self, D=1.0, R_key="R", adjacency_key="adjacency", device=AutoDevice()):
        
        compute_mean_first_passage_time(self.adata, D=D, R_key=R_key, adjacency_key=adjacency_key, device=device)

    @property
    def graph_idx(self):
        if not hasattr(self, "_graph"):
            self._graph = annoyance.kNN(self.adata)
            self._graph.build()
        return self._graph.idx
            
    def __call__(self, *args, **kwargs):
        
        
        self.build_kNN(graph_idx=self.graph_idx)
        self.compute_Laplacian()
        self.compute_potential()
        configure_S(adata=self.adata)
        self.compute_fate_bias()
