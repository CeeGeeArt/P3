# Contains various image processing methods like blur,
import numpy as np
import cv2
import ImageProcessingMethods

img = cv2.imread('binTest.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# New
def dilation(img):
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 25
    newImg = np.zeros((height, width), np.uint8)
    for i in range(height - 2):
        for j in range(width-2):
            if j == 0:
                color[0] = img[i - 2][j - 2]
                color[1] = img[i - 2][j - 1]
                color[2] = img[i - 2][j]
                color[3] = img[i - 2][j + 1]
                color[4] = img[i - 2][j + 2]

                color[5] = img[i - 1][j - 2]
                color[6] = img[i - 1][j - 1]
                color[7] = img[i - 1][j]
                color[8] = img[i - 1][j + 1]
                color[9] = img[i - 1][j + 2]

                color[10] = img[i][j - 2]
                color[11] = img[i][j - 1]
                color[12] = img[i][j]
                color[13] = img[i][j + 1]
                color[14] = img[i][j + 2]

                color[15] = img[i + 1][j - 2]
                color[16] = img[i + 1][j - 1]
                color[17] = img[i + 1][j]
                color[18] = img[i + 1][j + 1]
                color[19] = img[i + 1][j + 2]

                color[20] = img[i + 2][j - 2]
                color[21] = img[i + 2][j - 1]
                color[22] = img[i + 2][j]
                color[23] = img[i + 2][j + 1]
                color[24] = img[i + 2][j + 2]

            elif j % 5 == 0:
                color[4] = img[i - 2][j + 2]
                color[9] = img[i - 1][j + 2]
                color[14] = img[i][j + 2]
                color[19] = img[i + 1][j + 2]
                color[24] = img[i + 2][j + 2]

            elif j % 4 == 0:
                color[3] = img[i - 2][j + 1]
                color[8] = img[i - 1][j + 1]
                color[13] = img[i][j + 1]
                color[18] = img[i + 1][j + 1]
                color[23] = img[i + 2][j + 1]

            elif j % 3 == 0:
                color[2] = img[i - 2][j]
                color[7] = img[i - 1][j]
                color[12] = img[i][j]
                color[17] = img[i + 1][j]
                color[22] = img[i + 2][j]

            elif j % 2 == 0:
                color[1] = img[i - 2][j - 1]
                color[6] = img[i - 1][j - 1]
                color[11] = img[i][j - 1]
                color[16] = img[i + 1][j - 1]
                color[21] = img[i + 2][j - 1]

            else:
                color[0] = img[i - 2][j - 2]
                color[5] = img[i - 1][j - 2]
                color[10] = img[i][j - 2]
                color[15] = img[i + 1][j - 2]
                color[20] = img[i + 2][j - 2]

            if any(color):
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0

    return newImg

def erotion(img):
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 25
    newImg = np.zeros((height, width, 1), np.uint8)
    for i in range(height - 2):
        for j in range(width - 2):
            if j == 0:
                color[0] = img[i - 2][j - 2]
                color[1] = img[i - 2][j - 1]
                color[2] = img[i - 2][j]
                color[3] = img[i - 2][j + 1]
                color[4] = img[i - 2][j + 2]

                color[5] = img[i - 1][j - 2]
                color[6] = img[i - 1][j - 1]
                color[7] = img[i - 1][j]
                color[8] = img[i - 1][j + 1]
                color[9] = img[i - 1][j + 2]

                color[10] = img[i][j - 2]
                color[11] = img[i][j - 1]
                color[12] = img[i][j]
                color[13] = img[i][j + 1]
                color[14] = img[i][j + 2]

                color[15] = img[i + 1][j - 2]
                color[16] = img[i + 1][j - 1]
                color[17] = img[i + 1][j]
                color[18] = img[i + 1][j + 1]
                color[19] = img[i + 1][j + 2]

                color[20] = img[i + 2][j - 2]
                color[21] = img[i + 2][j - 1]
                color[22] = img[i + 2][j]
                color[23] = img[i + 2][j + 1]
                color[24] = img[i + 2][j + 2]

            elif j % 5 == 0:
                color[4] = img[i - 2][j + 2]
                color[9] = img[i - 1][j + 2]
                color[14] = img[i][j + 2]
                color[19] = img[i + 1][j + 2]
                color[24] = img[i + 2][j + 2]

            elif j % 4 == 0:
                color[3] = img[i - 2][j + 1]
                color[8] = img[i - 1][j + 1]
                color[13] = img[i][j + 1]
                color[18] = img[i + 1][j + 1]
                color[23] = img[i + 2][j + 1]

            elif j % 3 == 0:
                color[2] = img[i - 2][j]
                color[7] = img[i - 1][j]
                color[12] = img[i][j]
                color[17] = img[i + 1][j]
                color[22] = img[i + 2][j]

            elif j % 2 == 0:
                color[1] = img[i - 2][j - 1]
                color[6] = img[i - 1][j - 1]
                color[11] = img[i][j - 1]
                color[16] = img[i + 1][j - 1]
                color[21] = img[i + 2][j - 1]

            else:
                color[0] = img[i - 2][j - 2]
                color[5] = img[i - 1][j - 2]
                color[10] = img[i][j - 2]
                color[15] = img[i + 1][j - 2]
                color[20] = img[i + 2][j - 2]

            if all(color):
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0

    return newImg


def closing(img):
    dilatedIMG = dilation(img)
    newIMG = erotion(dilatedIMG)

    return newIMG


def opening(img):
    erodedIMG = erotion(img)
    newIMG = dilation(erodedIMG)

    return newIMG

closedImg = closing(img)
newImg = opening(closedImg)
cv2.imshow('swag', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()