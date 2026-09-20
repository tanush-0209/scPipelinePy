"""
Clustering Module
Graph-based clustering with Leiden algorithm.
"""

import scanpy as sc

def cluster_cells(adata, resolution=0.5, random_state=42):
    """
    Cluster cells using Leiden algorithm.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    resolution : float, default=0.5
        Resolution parameter (higher = more clusters)
    random_state : int, default=42
        Random state for reproducibility
    
    Returns
    -------
    adata : AnnData
        AnnData object with cluster assignments
    """
    print(f"\nClustering cells (resolution={resolution})...")
    
    # Run Leiden clustering
    sc.tl.leiden(adata, resolution=resolution, random_state=random_state)
    
    n_clusters = len(adata.obs['leiden'].unique())
    print(f"✓ Clustering complete: {n_clusters} clusters found")
    
    # Print cluster sizes
    print("\nCluster sizes:")
    print(adata.obs['leiden'].value_counts().sort_index())
    
    return adata
