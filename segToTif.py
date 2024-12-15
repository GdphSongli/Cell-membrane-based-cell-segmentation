import numpy as np
import matplotlib.pyplot as plt
from cellpose import models
from cellpose.io import imread
import cellpose
from cellpose import plot, io
from cellpose import plot, utils
from PIL import Image
import cv2
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

dat = np.load(infile, allow_pickle=True).item()

Masks = utils.remove_edge_masks(dat['masks'])
Outlines = utils.masks_to_outlines(Masks)
outY, outX = np.nonzero(Outlines)

imgout = dat['img']
imgout[outY, outX, 1] = 65535
io.imsave(outfile, imgout)
