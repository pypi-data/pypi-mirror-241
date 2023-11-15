
import anndata

def downsample(adata: anndata.AnnData, N: int = 2_000):
    
    """
    Downsample adata and reformat index for downstream compatibility.
    
    Parameters
    ----------
    adata: anndata.AnnData
    
    N: int, default = 2_000
    
    Returns
    -------
    adata_subset: anndata.AnnData
    """
    
    idx = adata.obs.sample(N).index
    
    adata_subset = adata[idx].copy()
    adata_subset.obs = adata_subset.obs.reset_index()
    adata_subset.obs.index = adata_subset.obs.index.astype(str)
    
    return adata_subset