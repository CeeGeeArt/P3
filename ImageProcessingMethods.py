# Contains various image processing methods like blur,
import numpy as np
import cv2


# Median blur with 3x3 kernel
def ourMedianBlur(img):
    height, width, channels = img.shape
    color = [(0, 0)] * 9
    newImg = np.zeros((height, width, 3), np.uint8)
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

            newImg[i][j] = (mySort[4], img[i][j][1], img[i][j][2])
    return newImg

def threshold(frame, lowerValueH, upperValueH, lowerValueS, upperValueS, lowerValueV, upperValueV):
    height = frame.shape[0]
    width = frame.shape[1]
    newImg = np.zeros((height, width))
    for i in range(height - 1):
        for j in range(width - 1):
            b = frame[i, j][0]
            g = frame[i, j][1]
            r = frame[i, j][2]

            if upperValueH > b > lowerValueH and upperValueS > g > lowerValueS and upperValueV > r > lowerValueV:
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0
    return newImg