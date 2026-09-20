"""
Main Pipeline
Complete end-to-end workflow.
"""

from .load_data import load_sc_data
from .qc import calculate_qc_metrics, filter_cells
from .preprocessing import normalize_data, find_variable_genes, scale_data
from .reduction import run_pca, run_umap
from .clustering import cluster_cells

def run_full_pipeline(data_path, output_dir='output/', min_genes=200, max_genes=2500, 
                      max_mito=5, n_top_genes=2000, resolution=0.5):
    """
    Run complete single-cell analysis pipeline.
    
    Parameters
    ----------
    data_path : str
        Path to 10X data directory
    output_dir : str, default='output/'
        Output directory
    min_genes : int, default=200
        Minimum genes per cell
    max_genes : int, default=2500
        Maximum genes per cell
    max_mito : float, default=5
        Maximum mitochondrial percentage
    n_top_genes : int, default=2000
        Number of variable genes
    resolution : float, default=0.5
        Clustering resolution
    
    Returns
    -------
    adata : AnnData
        Processed and analyzed AnnData object
    """
    
    print("="*60)
    print("scPipelinePy: Complete Single-Cell Analysis Pipeline")
    print("="*60)
    
    # Step 1: Load
    print("\n[1/7] LOADING DATA")
    adata = load_sc_data(data_path)
    
    # Step 2: QC Metrics
    print("\n[2/7] QUALITY CONTROL - METRICS")
    adata = calculate_qc_metrics(adata)
    
    # Step 3: QC Filter
    print("\n[3/7] QUALITY CONTROL - FILTERING")
    adata = filter_cells(adata, min_genes=min_genes, max_genes=max_genes, max_mito=max_mito)
    
    # Step 4: Normalize
    print("\n[4/7] NORMALIZATION")
    adata = normalize_data(adata)
    adata = find_variable_genes(adata, n_top_genes=n_top_genes)
    adata = scale_data(adata)
    
    # Step 5: Dimensionality Reduction
    print("\n[5/7] DIMENSIONALITY REDUCTION")
    adata = run_pca(adata)
    adata = run_umap(adata)
    
    # Step 6: Clustering
    print("\n[6/7] CLUSTERING")
    adata = cluster_cells(adata, resolution=resolution)
    
    # Step 7: Summary
    print("\n[7/7] PIPELINE COMPLETE")
    print("="*60)
    print(f"Final result: {adata.n_obs} cells × {adata.n_vars} genes")
    print(f"Clusters: {len(adata.obs['leiden'].unique())}")
    print("="*60)
    
    return adata
