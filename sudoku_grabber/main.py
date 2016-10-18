# SuDoKu Grabber in OpenCV
# http://aishack.in/tutorials/sudoku-grabber-opencv-detection/
# Converting c++ to python

import numpy as np
import cv2

# Mat sudoku = imread("sudoku.jpg", 0);
src = cv2.imread('sudoku.jpg', 0)   # Load an color image in grayscale

# Mat outerBox = Mat(sudoku.size(), CV_8UC1);
height = len(src)
width = len(src[0])
outer_box = np.zeros((height, width), np.uint8)

# GaussianBlur(sudoku, sudoku, Size(11,11), 0);
src = cv2.GaussianBlur(src, (11, 11), 0)

# adaptiveThreshold(sudoku, outerBox, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 5, 2);
outer_box = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)

# bitwise_not(outerBox, outerBox);
outer_box = cv2.bitwise_not(outer_box);

# Mat kernel = (Mat_<uchar>(3,3) << 0,1,0,1,1,1,0,1,0);
kernel = np.array([(0, 1, 0), (1, 1, 1), (0, 1, 0)], dtype=np.uint8)
# dilate(outerBox, outerBox, kernel);
outer_box = cv2.dilate(outer_box, kernel)

cv2.imshow('image', outer_box)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('sudoku2.png', img)
    cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
