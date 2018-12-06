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
            h, s, v = frame[i, j]

            if upperValueH > h > lowerValueH and upperValueS > s > lowerValueS and upperValueV > v > lowerValueV:
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0
    return newImg

def ourMinAreaRect(contour):
    polygon = []
    x_max = np.argmax(contour[:][1])
    x_min = np.argmin(contour[:][1])
    y_max = np.argmax(contour[:][0])
    y_min = np.argmin(contour[:][0])

    print(x_max)
    print(contour[1])
    print(x_min)
    print(contour[0])
    print(y_max)
    print(y_min)

    polygon.append(contour.index(y_min))




