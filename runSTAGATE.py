import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import scanpy as sc
import matplotlib.pyplot as plt
import os
import sys

import STAGATE

import tensorflow as tf

tf.compat.v1.disable_eager_execution()


infile = sys.argv[ 1 ]
prefix = sys.argv[ 2 ]

adata = sc.read_h5ad(infile)

sc.pp.filter_cells(adata, min_genes=50)
sc.pp.filter_genes(adata, min_cells=3)


sc.pp.highly_variable_genes(adata, flavor="seurat_v3", n_top_genes=3000)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

STAGATE.Cal_Spatial_Net(adata, rad_cutoff=50)
STAGATE.Stats_Spatial_Net(adata)

adata = STAGATE.train_STAGATE(adata, alpha=0)

sc.pp.neighbors(adata, use_rep='STAGATE')
sc.tl.umap(adata)

sc.tl.leiden(adata, resolution=1.0, key_added = "leiden_ST")

adata.write_h5ad(prefix + "_STAGATE.h5ad")
