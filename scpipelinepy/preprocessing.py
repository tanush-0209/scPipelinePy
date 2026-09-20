"""
Preprocessing Module
Normalization, feature selection, scaling.
"""

import scanpy as sc
import numpy as np

def normalize_data(adata, target_sum=1e4):
    """
    Normalize and log-transform data.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    target_sum : float, default=1e4
        Target sum for normalization
    
    Returns
    -------
    adata : AnnData
        Normalized AnnData object
    """
    print("Normalizing data...")
    
    # Normalize to target sum
    sc.pp.normalize_total(adata, target_sum=target_sum)
    
    # Log transform
    sc.pp.log1p(adata)
    
    print(f"✓ Data normalized and log-transformed")
    return adata

def find_variable_genes(adata, n_top_genes=2000):
    """
    Find highly variable genes.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    n_top_genes : int, default=2000
        Number of variable genes to select
    
    Returns
    -------
    adata : AnnData
        AnnData object with variable genes identified
    """
    print(f"\nFinding {n_top_genes} highly variable genes...")
    
    sc.pp.highly_variable_genes(adata, n_top_genes=n_top_genes)
    
    n_hvg = adata.var['highly_variable'].sum()
    print(f"✓ Found {n_hvg} variable genes")
    
    return adata

def scale_data(adata):
    """
    Scale data to unit variance.
    
    Parameters
    ----------
    adata : AnnData
        Annotated data object
    
    Returns
    -------
    adata : AnnData
        Scaled AnnData object
    """
    print("\nScaling data...")
    
    sc.pp.scale(adata, max_value=10)
    
    print(f"✓ Data scaled")
    return adata
