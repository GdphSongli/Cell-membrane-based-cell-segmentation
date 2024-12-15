import stereo as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

polyGenFile = sys.argv[ 1 ]
color_file  = sys.argv[ 2 ]
ST_domainFile = sys.argv[ 3 ]
outfile = sys.argv[ 4 ]

cell_points = pd.read_table(polyGenFile, header=0, index_col=0)


import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random
import pandas as pd
import scanpy as sc
from shapely.wkt import loads


def str_to_polygon(polygon_str):
    return loads(polygon_str)


polygon_cells = cell_points['cell_point'].apply(str_to_polygon)

print(polygon_cells)

df = pd.read_table(ST_domainFile, header=0, index_col=0)

polygon_cells.index.equals(df.index)

fig, ax = plt.subplots( figsize=(8, 8) )


col_df = pd.read_table(color_file, header=None)
col_df.columns = ["id", "color"]

myColors = col_df.set_index('id')['color'].to_dict()

print(myColors[1])

for i, polygon in enumerate(polygon_cells):
    tmp_df = pd.DataFrame(polygon.boundary.coords.xy)
    tmp_array = tmp_df.T.to_numpy()

    cluster = df.iloc[i,0]
    color = myColors[cluster]

    tmp_array[:,1] *= -1
    tmp_array[:,1] = tmp_array[:,1] + 26460
    poly = Polygon(tmp_array, closed=True, facecolor=color)
    ax.add_patch(poly)


ax.set_xlim(0, 26460)
ax.set_ylim(0, 26460)

plt.savefig(outfile)
