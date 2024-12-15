import numpy as np
import matplotlib.pyplot as plt
from cellpose import models
from cellpose.io import imread
import cellpose
from cellpose import plot, io
import cv2
import sys
from cellpose import io, utils

infile = sys.argv[ 1 ]
outfile = sys.argv[ 2 ]
outdir = sys.argv[ 3 ]
trained_model = sys.argv[ 4 ]

img = imread(infile)

model = models.CellposeModel(pretrained_model=trained_model, gpu=False)

# replace it by your trained model.
diam = 32.71

masks, flows, styles = model.eval(img, diameter = diam, channels=[1,3])

ofile = outdir + "/" + outfile

io.masks_flows_to_seg(img, masks, flows, diam, ofile, channels=[1,3])
