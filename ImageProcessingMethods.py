# Contains various image processing methods like blur, thresholding
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


def dilation(img):
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 13
    newImg = np.zeros((height, width), np.uint8)
    for i in range(height - 2):
        for j in range(width-2):
            color[0] = img[i - 2][j]

            color[1] = img[i - 1][j - 1]
            color[2] = img[i - 1][j]
            color[3] = img[i - 1][j + 1]
            color[4] = img[i][j - 2]
            color[5] = img[i][j - 1]
            color[6] = img[i][j]
            color[7] = img[i][j + 1]
            color[8] = img[i][j + 2]
            color[9] = img[i + 1][j - 1]
            color[10] = img[i + 1][j]
            color[11] = img[i + 1][j + 1]
            color[12] = img[i + 2][j]
            #print(color)

            if color[0] or color[1] or color[2] or color[3] or color[4] or color[5] or color[6] or color[7] or color[8] \
                    or color[9] or color[10] or color[11] or color[12]:
                newImg[i,j] = 255
                #print('True')
            else:
                newImg[i,j] = 0
                #print('falsk')

    return newImg

def erotion(img):
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 13
    newImg = np.zeros((height, width), np.uint8)
    for i in range(height - 2):
        for j in range(width - 2):

            color[0] = img[i - 2][j]
            color[1] = img[i - 1][j - 1]
            color[2] = img[i - 1][j]
            color[3] = img[i - 1][j + 1]
            color[4] = img[i][j - 2]
            color[5] = img[i][j - 1]
            color[6] = img[i][j]
            color[7] = img[i][j + 1]
            color[8] = img[i][j + 2]
            color[9] = img[i + 1][j - 1]
            color[10] = img[i + 1][j]
            color[11] = img[i + 1][j + 1]
            color[12] = img[i + 2][j]

            #print(color)

            if color[0] and color[1] and color[2] and color[3] and color[4] and color[5] and color[6] and color[7] and color[8] \
                    and color[9] and color[10] and color[11] and color[12]:
                newImg[i,j] = 255
                #print('True')
            else:
                newImg[i,j] = 0
                #print('falsk')

    return newImg

def closing(img):
    dilatedIMG = dilation(img)
    newIMG = erotion(dilatedIMG)

    return newIMG

def opening(img):
    erodedIMG = erotion(img)
    newIMG = dilation(erodedIMG)

    return newIMG