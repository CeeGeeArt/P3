import cv2
import numpy as np

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

while(True):
    height = frame.shape[0]
    width = frame.shape[1]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_redH = np.array([0])
    upper_redH = np.array([5])
    lower_redS = np.array([120])
    upper_redS = np.array([255])
    lower_redV = np.array([150])
    upper_redV = np.array([255])


    newImg = threshold(frame, lower_redH, upper_redH, lower_redS, upper_redS, lower_redV, upper_redV)

