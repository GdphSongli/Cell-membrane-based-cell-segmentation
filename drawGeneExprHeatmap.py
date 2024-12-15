import scanpy as sc
import matplotlib.pyplot as plt
import sys
import os
import numpy as np

infile = sys.argv[ 1 ]
outfile = sys.argv[ 2 ]
outprefix = sys.argv[ 3 ]

adata = sc.read(infile)

sc.pp.filter_cells(adata, min_genes=50)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata)

adata.raw = adata
adata = adata[:, adata.var.highly_variable]
sc.pp.scale(adata, max_value=10)

sc.tl.pca(adata, svd_solver='arpack')
sc.pp.neighbors(adata)

sc.tl.paga(adata)
sc.pl.paga(adata, plot=False)
sc.tl.umap(adata, init_pos='paga')

sc.tl.leiden(adata)

from matplotlib.colors import LinearSegmentedColormap

color1 = "#d1cdbf"
color2 = "#921752"

rgb_color1 = tuple(int(color1[i:i+2], 16) / 255.0 for i in (1, 3, 5))
rgb_color2 = tuple(int(color2[i:i+2], 16) / 255.0 for i in (1, 3, 5))

colors = [rgb_color1, rgb_color2]
cmap_name = 'custom_cmap'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=100)

sc.tl.rank_genes_groups(adata, 'leiden')

plt.figure(figsize=(4, 4))
sc.pl.rank_genes_groups_heatmap(adata, groupby='leiden', n_genes=20, cmap=custom_cmap, swap_axes=True)
plt.savefig(outfile)
