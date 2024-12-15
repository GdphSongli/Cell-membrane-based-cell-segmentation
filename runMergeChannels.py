import numpy as np
import cv2
import sys
import tifffile

memFile  = sys.argv[1]
dapiFile = sys.argv[2]
outFile  = sys.argv[3]

mem = cv2.imread(memFile, cv2.IMREAD_UNCHANGED)
dapi = cv2.imread(dapiFile, cv2.IMREAD_UNCHANGED)

zeros = np.zeros(mem.shape, dtype="uint16")

img = cv2.merge([mem, zeros, dapi])
tifffile.imwrite(outFile, img)
