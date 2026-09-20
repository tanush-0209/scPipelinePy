from scpipelinepy.load_data import load_sc_data
from scpipelinepy.qc import calculate_qc_metrics, filter_cells

print("Step 1: Loading data...")
adata = load_sc_data('data/pbmc3k/filtered_gene_bc_matrices/hg19/')

print("Step 2: Calculating QC metrics...")
adata = calculate_qc_metrics(adata)

print("Step 3: Filtering cells...")
adata = filter_cells(adata)

print("\n✓ QC complete!")
print(adata)
