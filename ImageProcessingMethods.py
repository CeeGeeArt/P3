# Contains various image processing methods like blur, thresholding
import numpy as np


# Median blur with 3x3 kernel
def ourMedianBlur(img):
    height, width, channels = img.shape
    hue = [0] * 9
    sat = [0] * 9
    val = [0] * 9
    newImg = np.zeros((height, width, 3), np.uint8)
    for i in range(height - 1):
        for j in range(width-1):
            if j == 0:
                hue[0], sat[0], val[0] = img[i - 1][j - 1]
                hue[1], sat[1], val[1] = img[i - 1][j]
                hue[2], sat[2], val[2] = img[i - 1][j + 1]
                hue[3], sat[3], val[3] = img[i][j - 1]
                hue[4], sat[4], val[4] = img[i][j]
                hue[5], sat[5], val[5] = img[i][j + 1]
                hue[6], sat[6], val[6] = img[i + 1][j - 1]
                hue[7], sat[7], val[7] = img[i + 1][j]
                hue[8], sat[8], val[8] = img[i + 1][j + 1]
            elif j % 3 == 0:
                hue[2], sat[2], val[2] = img[i - 1][j + 1]
                hue[5], sat[5], val[5] = img[i][j + 1]
                hue[8], sat[8], val[8] = img[i + 1][j + 1]
            elif j % 2 == 0:
                hue[1], sat[1], val[1] = img[i - 1][j + 1]
                hue[4], sat[4], val[4] = img[i][j + 1]
                hue[7], sat[7], val[7] = img[i + 1][j + 1]
            else:
                hue[0], sat[0], val[0] = img[i - 1][j + 1]
                hue[3], sat[3], val[3] = img[i][j + 1]
                hue[6], sat[6], val[6] = img[i + 1][j + 1]

            mySortHue = hue
            mySortHue.sort()

            mySortSat = sat
            mySortSat.sort()

            mySortVal = val
            mySortVal.sort()

            newImg[i][j] = (mySortHue[4], mySortSat[4], mySortVal[4])
    return newImg


# Method that applies thresholding to a HSV image
def threshold(frame, lowerValueH, upperValueH, lowerValueS, upperValueS, lowerValueV, upperValueV):
    # Retrieves the size of the image and then makes an output image in the right dimensions
    height = frame.shape[0]
    width = frame.shape[1]
    newImg = np.zeros((height, width), np.uint8)

    # Loops through all the pixels in the the image, to apply the threshold
    for i in range(height - 1):
        for j in range(width - 1):
            # Gets the color values of the image
            h, s, v = frame[i, j]
            # Checks i the color value is within the threshold, and makes the pixel white if it is
            if upperValueH > h > lowerValueH and upperValueS > s > lowerValueS and upperValueV > v > lowerValueV:
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0
    return newImg

# Dilation with a 5 x 5 kernel
def dilation(img):
    # Retrieves the size of the image and then makes an output image in the right dimensions
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 25
    newImg = np.zeros((height, width), np.uint8)
    # Loops through all the pixels in the the image, to apply the dilation
    for i in range(height - 2):
        for j in range(width-2):
            # The kernel is applied to the current pixel. Only changing parts of the kernel are updated.
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

            # If one of the pixels in the kernel is white, the current pixel is made white, else it will be black
            if any(color):
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0

    return newImg


# Erosion with a 5 x 5 kernel
def erosion(img):
    # Retrieves the size of the image and then makes an output image in the right dimensions
    height = img.shape[0]
    width = img.shape[1]
    color = [0] * 25
    newImg = np.zeros((height, width, 1), np.uint8)
    # Loops through all the pixels in the the image, to apply the erosion
    for i in range(height - 2):
        for j in range(width - 2):
            # The kernel is applied to the current pixel. Only changing parts of the kernel are updated.
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

            # If all of the pixels in the kernel is white, the current pixel is made white, else it will be black
            if all(color):
                newImg[i, j] = 255
            else:
                newImg[i, j] = 0

    return newImg


def closing(img):
    # The dilation and erosion is applied to close the image
    dilatedIMG = dilation(img)
    newIMG = erosion(dilatedIMG)

    return newIMG

def opening(img):
    # The erosion and dilation is applied to close the image
    erodedIMG = erosion(img)
    newIMG = dilation(erodedIMG)

    return newIMG