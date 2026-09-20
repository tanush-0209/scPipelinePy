"""
Data Loading Module
Functions for loading single-cell data from various formats.
"""

import scanpy as sc
import anndata as ad
import os

def load_sc_data(data_path, format="10X", var_names='gene_symbols'):
    """
    Load single-cell RNA-seq data from various formats.
    
    Parameters
    ----------
    data_path : str
        Path to the data directory or file
    format : str, default="10X"
        Data format: "10X", "h5", "h5ad", or "csv"
    var_names : str, default='gene_symbols'
        Variable names to use. For 10X: 'gene_symbols' or 'gene_ids'
    
    Returns
    -------
    adata : AnnData
        Annotated data object with raw counts
    """
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data path not found: {data_path}")
    
    print(f"Loading data from: {data_path}")
    print(f"Format: {format}")
    
    if format == "10X":
        adata = sc.read_10x_mtx(
            data_path,
            var_names=var_names,
            cache=True
        )
        print(f"✓ Loaded 10X data: {adata.n_obs} cells × {adata.n_vars} genes")
        
    elif format == "h5":
        adata = sc.read_10x_h5(data_path)
        print(f"✓ Loaded H5 data: {adata.n_obs} cells × {adata.n_vars} genes")
        
    elif format == "h5ad":
        adata = sc.read_h5ad(data_path)
        print(f"✓ Loaded H5AD data: {adata.n_obs} cells × {adata.n_vars} genes")
        
    elif format == "csv":
        adata = sc.read_csv(data_path).T
        print(f"✓ Loaded CSV data: {adata.n_obs} cells × {adata.n_vars} genes")
        
    else:
        raise ValueError(f"Unsupported format: {format}")
    
    adata.var_names_make_unique()
    return adata


if __name__ == "__main__":
    # Test the function
    adata = load_sc_data('data/pbmc3k/filtered_gene_bc_matrices/hg19/')
    print(adata)
