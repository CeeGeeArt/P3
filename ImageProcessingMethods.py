# Contains various image processing methods like blur,
import numpy as np
import cv2

# Median blur with 3x3 kernel
def ourMedianBlur(img):
    height, width, channels = img.shape
    color = [(0, 0)] * 9
    newimg = np.zeros((height, width, 3), np.uint8)
    for i in range(height - 1):
        for j in range(width-1):
            if j == 0:
                color[0] = img[i - 1][j - 1][0]
                color[1] = img[i - 1][j][0]
                color[2] = img[i - 1][j + 1][0]
                color[3] = img[i][j - 1][0]
                color[4] = img[i][j][0]
                color[5] = img[i][j + 1][0]
                color[6] = img[i + 1][j - 1][0]
                color[7] = img[i + 1][j][0]
                color[8] = img[i + 1][j + 1][0]
            elif j % 2 == 0:
                color[1] = img[i - 1][j + 1][0]
                color[4] = img[i][j + 1][0]
                color[7] = img[i + 1][j + 1][0]
            elif j % 1 == 0:
                color[0] = img[i - 1][j + 1][0]
                color[3] = img[i][j + 1][0]
                color[6] = img[i + 1][j + 1][0]
            else:
                color[2] = img[i - 1][j + 1][0]
                color[5] = img[i][j + 1][0]
                color[8] = img[i + 1][j + 1][0]

            mySort = color
            mySort.sort()

            newimg[i][j] = (mySort[4], img[i][j][1], img[i][j][2])
    return newimg
