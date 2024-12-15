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
import tifffile

infile = sys.argv[1]
outfile = sys.argv[2]
imgFile = sys.argv[3]

dat = np.load(infile, allow_pickle=True).item()

Masks = utils.remove_edge_masks(dat['masks'])
Outlines = utils.masks_to_outlines(Masks)
outY, outX = np.nonzero(Outlines)

dapi = cv2.imread(imgFile, cv2.IMREAD_UNCHANGED)
zeros = np.zeros(dapi.shape, dtype="uint16")

imgout = cv2.merge([zeros, zeros, dapi])

imgout[outY, outX] = np.array([0,65535,0])
io.imsave(outfile, imgout)
