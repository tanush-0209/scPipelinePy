"""
scPipelinePy: Modular Single-Cell RNA-seq Analysis Pipeline
"""

__version__ = "0.2.0"
__author__ = "Tanush Parasam Harish"

from .load_data import load_sc_data
from .qc import calculate_qc_metrics, filter_cells

__all__ = [
    'load_sc_data',
    'calculate_qc_metrics',
    'filter_cells'
]
