import cv2
import numpy as np
import os
import tifffile
import sys

pic_path = sys.argv[ 1 ]
pic_target = sys.argv[ 2 ]
outfile = sys.argv[ 3 ]

num_width_list = []
num_lenght_list = []

picture_names =  os.listdir(pic_path)
if len(picture_names)==0:
    print("No file")
 
else:
    img_1_1 = cv2.imread(pic_path + '1_1.tif', cv2.IMREAD_UNCHANGED)
    (width, length, depth) = img_1_1.shape
    print(width, length, depth)
    for picture_name in picture_names:
        num_width_list.append(int(picture_name.split("_")[0]))
        num_lenght_list.append(int((picture_name.split("_")[-1]).split(".")[0]))
    
    num_width = max(num_width_list)
    num_length = max(num_lenght_list)
    print( num_width, num_length )

    total_width = 0
    total_length = 0

    for i in range(1, num_width+1):
        tmp_img = cv2.imread(pic_path + '{}_{}.tif'.format(i, 1), cv2.IMREAD_UNCHANGED)
        (tmp_width, tmp_length, tmp_depth) = tmp_img.shape
        total_width = total_width + tmp_width


    for i in range(1, num_length+1):
        tmp_img = cv2.imread(pic_path + '{}_{}.tif'.format(1, i), cv2.IMREAD_UNCHANGED)
        (tmp_width, tmp_length, tmp_depth) = tmp_img.shape
        print(tmp_width, tmp_length, tmp_depth)
        total_length = total_length + tmp_length

    print(total_width, total_length, depth)
    splicing_pic = np.zeros((total_width, total_length, depth), dtype="uint16")
    
    for i in range(1, num_width):
        for j in range(1, num_length):
            img_part = cv2.imread(pic_path + '{}_{}.tif'.format(i, j), cv2.IMREAD_UNCHANGED)
            splicing_pic[width*(i-1) : width*i, length*(j-1) : length*j, :] = img_part
    


    for i in range(1, num_width):
        tmp_img = cv2.imread(pic_path + '{}_{}.tif'.format(i, num_length), cv2.IMREAD_UNCHANGED)
        (tmp_width, tmp_length, tmp_depth) = tmp_img.shape
        print(tmp_width, tmp_length, tmp_depth)
        splicing_pic[width*(i-1) : width*i, length*(num_length-1) : length*(num_length-1) + tmp_length, :] = tmp_img



    for j in range(1, num_length):
        tmp_img = cv2.imread(pic_path + '{}_{}.tif'.format(num_width, j), cv2.IMREAD_UNCHANGED)
        (tmp_width, tmp_length, tmp_depth) = tmp_img.shape
        print(tmp_width, tmp_length, tmp_depth)
        splicing_pic[width*(num_width-1) : width*(num_width-1) + tmp_width, length*(j-1) : length*j, :] = tmp_img


    tmp_img = cv2.imread(pic_path + '{}_{}.tif'.format(num_width, num_length), cv2.IMREAD_UNCHANGED)
    (tmp_width, tmp_length, tmp_depth) = tmp_img.shape
    print(tmp_width, tmp_length, tmp_depth)
    splicing_pic[width*(num_width-1) : width*(num_width-1) + tmp_width, length*(num_length-1) : length*(num_length-1) + tmp_length, :] = tmp_img


    print(splicing_pic.shape)
    tifffile.imwrite(pic_target + outfile, splicing_pic)
