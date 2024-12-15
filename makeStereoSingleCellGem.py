import tifffile
import cv2
import numpy as np
import sys

maskFile = sys.argv[ 1 ]
gemFile  = sys.argv[ 2 ]
outfile  = sys.argv[ 3 ]

mask = tifffile.imread(maskFile)

outf = open(outfile, "w")

with open(gemFile, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("#"):
            outline = line + "\n"
            outf.write(outline)
            continue
        if line.startswith("geneID"):
            outline = line + "\tCellID\n"
            outf.write(outline)
            continue
        gene, x, y, mid, exon = line.split("\t")
        xid = int(x)
        yid = int(y)
        label = mask[yid, xid]
        if label != 0:
            outline = line + "\t" + str(label) + "\n"
            outf.write(outline)

outf.close()
