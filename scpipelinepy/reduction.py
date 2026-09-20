"""
Dimensionality Reduction Module
PCA and UMAP.
"""

import scanpy as sc

def run_pca(adata, n_pcs=50):
    """
    Run PCA dimensionality reduction.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    n_pcs : int, default=50
        Number of principal components
    
    Returns
    -------
    adata : AnnData
        AnnData object with PCA
    """
    print(f"Running PCA ({n_pcs} components)...")
    
    sc.tl.pca(adata, n_comps=n_pcs)
    
    print(f"✓ PCA complete")
    return adata

def run_umap(adata, n_neighbors=15, min_dist=0.1, n_pcs=50):
    """
    Run UMAP dimensionality reduction.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    n_neighbors : int, default=15
        Number of neighbors for UMAP
    min_dist : float, default=0.1
        Minimum distance for UMAP
    n_pcs : int, default=50
        Number of PCs to use
    
    Returns
    -------
    adata : AnnData
        AnnData object with UMAP
    """
    print(f"\nRunning UMAP...")
    
    # Build neighbor graph
    sc.pp.neighbors(adata, n_neighbors=n_neighbors, n_pcs=n_pcs)
    
    # Run UMAP
    sc.tl.umap(adata, min_dist=min_dist)
    
    print(f"✓ UMAP complete")
    return adata
