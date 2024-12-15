import cv2
import numpy as np
import os
import tifffile
import sys

pic_path = sys.argv[ 1 ]
pic_target = sys.argv[ 2 ]

if not os.path.exists(pic_target):
    os.makedirs(pic_target)

cut_width = 4000
cut_length = 4000

picture = tifffile.imread(pic_path)
(width, length) = picture.shape
print(width, length)

pic = np.zeros((cut_width, cut_length), dtype="uint16")

num_width = int(width / cut_width)
num_length = int(length / cut_length)

for i in range(0, num_width):
    for j in range(0, num_length):
        pic = picture[i*cut_width : (i+1)*cut_width, j*cut_length : (j+1)*cut_length]      
        result_path = pic_target + '{}_{}.tif'.format(i+1, j+1)
        tifffile.imwrite(result_path, pic)

for j in range(0, num_length):
    tmp_cut_width = width - cut_width * num_width
    tmp_cut_length = cut_length
    print(tmp_cut_width, tmp_cut_length)
    tmp_pic = np.zeros((tmp_cut_width, tmp_cut_length), dtype="uint16")
    tmp_pic = picture[num_width*cut_width : num_width*cut_width + tmp_cut_width, j*cut_length : (j+1)*cut_length]
    result_path = pic_target + '{}_{}.tif'.format(num_width+1, j+1)
    tifffile.imwrite(result_path, tmp_pic)


for i in range(0, num_width):
    tmp_cut_width = cut_width
    tmp_cut_length = length - cut_length * num_length
    print(tmp_cut_width, tmp_cut_length)
    tmp_pic = np.zeros((tmp_cut_width, tmp_cut_length), dtype="uint16")
    tmp_pic = picture[i*cut_width : (i+1)*cut_width, num_length*cut_length : num_length*cut_length + tmp_cut_length]
    result_path = pic_target + '{}_{}.tif'.format(i+1, num_length+1)
    tifffile.imwrite(result_path, tmp_pic)


tmp_cut_width = width - cut_width * num_width
tmp_cut_length = length - cut_length * num_length
tmp_pic = np.zeros((tmp_cut_width, tmp_cut_length), dtype="uint16")
tmp_pic = picture[num_width*cut_width : num_width*cut_width + tmp_cut_width, num_length*cut_length : num_length*cut_length + tmp_cut_length]
result_path = pic_target + '{}_{}.tif'.format(num_width+1, num_length+1)
tifffile.imwrite(result_path, tmp_pic)
