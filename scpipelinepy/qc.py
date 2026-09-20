"""
Quality Control Module
"""

import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_qc_metrics(adata):
    """Calculate quality control metrics for cells."""
    print("Calculating QC metrics...")
    
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
    
    print(f"✓ QC metrics calculated")
    print(f"  Mean genes/cell: {adata.obs['n_genes_by_counts'].mean():.0f}")
    print(f"  Mean UMIs/cell: {adata.obs['total_counts'].mean():.0f}")
    print(f"  Mean MT%: {adata.obs['pct_counts_mt'].mean():.2f}%")
    
    return adata

def filter_cells(adata, min_genes=200, max_genes=2500, max_mito=5):
    """Filter cells based on QC thresholds."""
    print(f"\nFiltering cells...")
    n_cells_before = adata.n_obs
    
    adata = adata[
        (adata.obs['n_genes_by_counts'] >= min_genes) &
        (adata.obs['n_genes_by_counts'] <= max_genes) &
        (adata.obs['pct_counts_mt'] <= max_mito)
    ]
    
    n_cells_after = adata.n_obs
    n_cells_removed = n_cells_before - n_cells_after
    pct_removed = (n_cells_removed / n_cells_before) * 100
    
    print(f"✓ Filtering complete")
    print(f"  Cells before: {n_cells_before}")
    print(f"  Cells after: {n_cells_after}")
    print(f"  Cells removed: {n_cells_removed} ({pct_removed:.1f}%)")
    
    return adata
