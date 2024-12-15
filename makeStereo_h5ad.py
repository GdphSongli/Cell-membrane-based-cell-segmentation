import stereo as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import anndata
import sys

gemFile = sys.argv[ 1 ]
seuratOut = sys.argv[ 2 ]
scanpyOut = sys.argv[ 3 ]

data = st.io.read_gem(gemFile, bin_type='cell_bins')
data.tl.cal_qc()

data.tl.filter_cells(min_gene=50)
data.tl.filter_genes(min_cell=3)

data.tl.raw_checkpoint()

data.tl.normalize_total()
data.tl.log1p()

data.tl.pca(use_highly_genes=False, n_pcs=50, svd_solver='arpack')
data.tl.gaussian_smooth(n_neighbors=20, smooth_threshold=90)

data.tl.normalize_total(target_sum=10000)
data.tl.log1p()

data.tl.pca(use_highly_genes=False, n_pcs=50, svd_solver='arpack')
data.tl.neighbors(pca_res_key='pca', n_pcs=15, res_key='neighbors')
data.tl.leiden(neighbors_res_key='neighbors', res_key='leiden')
data.tl.umap(pca_res_key='pca', neighbors_res_key='neighbors', res_key='umap')

seuratOut_poly = seuratOut + "_polygen.xls"
adata = st.io.stereo_to_anndata(data,flavor='seurat')
tmp = adata.obs.cell_point
tmp.to_csv(seuratOut_poly,sep="\t")
adata.obs = adata.obs.drop("cell_point",axis=1)
seuratOut_h5ad = seuratOut + ".h5ad"
adata.write_h5ad(seuratOut_h5ad)

scanpyOut_poly = scanpyOut + "_polygen.xls"
adata = st.io.stereo_to_anndata(data,flavor='scanpy')
tmp = adata.obs.cell_point
tmp.to_csv(scanpyOut_poly,sep="\t")
adata.obs = adata.obs.drop("cell_point",axis=1)
scanpyOut_h5ad = scanpyOut + ".h5ad"
adata.write_h5ad(scanpyOut_h5ad)
