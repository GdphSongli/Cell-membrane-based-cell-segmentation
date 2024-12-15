from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()

import sys
sys.path.append("/full/path/to/SCS")

from src import scs

bin_file = sys.argv[ 1 ]
image_file = sys.argv[ 2 ]
scs.segment_cells(bin_file, image_file, align='rigid', patch_size=1200)
