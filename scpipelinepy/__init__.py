"""
scPipelinePy: Modular Single-Cell RNA-seq Analysis Pipeline
"""

__version__ = "1.0.0"
__author__ = "Tanush Parasam Harish"

from .load_data import load_sc_data
from .qc import calculate_qc_metrics, filter_cells
from .preprocessing import normalize_data, find_variable_genes, scale_data
from .reduction import run_pca, run_umap
from .clustering import cluster_cells
from .pipeline import run_full_pipeline

__all__ = [
    "load_sc_data",
    "calculate_qc_metrics",
    "filter_cells",
    "normalize_data",
    "find_variable_genes",
    "scale_data",
    "run_pca",
    "run_umap",
    "cluster_cells",
    "run_full_pipeline"
]
