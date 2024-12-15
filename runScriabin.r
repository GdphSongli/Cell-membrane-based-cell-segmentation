library(Seurat)
library(SeuratData)
library(scriabin)
library(tidyverse)
library(ComplexHeatmap)
library(cowplot)
library(magrittr)

opt = commandArgs(T)
rdsFile = opt[1]
outFile = opt[2]
rdsFile
outFile

rds = readRDS(rdsFile)
rds = SCTransform(rds)

rds = RunPCA(rds)
rds = RunUMAP(rds, dims = 1:30)

rds.ccim = GenerateCCIM(rds, senders = colnames(rds), receivers = colnames(rds))
saveRDS(rds.ccim, outFile)
