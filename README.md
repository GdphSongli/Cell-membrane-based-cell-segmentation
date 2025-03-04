# Cell-membrane-based-cell-segmentation
Genetic-labelling cell membranes to define cell boundaries in sequencing-based spatial transcriptomes ([==Improving Spatial Transcriptomics with Membrane-Based Boundary Definition and Enhanced Single-Cell Resolution==](https://onlinelibrary.wiley.com/doi/abs/10.1002/smtd.202401056)). The current sequencing-based spatial transcriptomics technologies typically use nuclear regions to represent a cell, but this strategy excludes the cytoplasmic regions of the cell. Furthermore, in some specific cell types, such as intestinal epithelial cells and multinucleated cells in the liver, the definition of a cell is not accurate. Therefore, using the cell membrane to define the boundaries of single cells in spatial transcriptomics is more consistent with biological definitions.

# Tool for cell segmentation
- Cellpose: This software is used for cell segmentation and can perform human-in-the-loop specificity training based on the features of your spatial transcriptomics images, enabling more accurate segmentation of cells with special morphologies.
# Software dependencies
- Cellpose:
- Stereopy:
- Tifffile:
- Scanpy:
- STAGATE:
- Pandas:
- Numpy:
- SCS:

# Case study: demonstration of multinucleated cell segmentation
Note: the repositiory will be updated in the coming days to inlclude jupyter notebooks.

# Citations
The cell membrane-based cell segmentation manuscript is published at [Small Methods](https://onlinelibrary.wiley.com/doi/abs/10.1002/smtd.202401056). If you find cell membrane-based cell segmentation beneficial for your spatial transcriptomics project, please cite our paper.\
L. Song, L. Wang, Z. He, X. Cui, C. Peng, J. Xu, Z. Yong, Y. Liu, J.-F. Fei, Improving Spatial Transcriptomics with Membrane-Based Boundary Definition and Enhanced Single-Cell Resolution. Small Methods 2025, 2401056. https://doi.org/10.1002/smtd.202401056

# Support
For questions or comments, please file a Github issue and/or email Song Li (songli7105@gdph.org.cn)
