import cv2
import numpy as np
import math


cap = cv2.VideoCapture(0)

def ourInRange(frame, lowerValueH, upperValueH, lowerValueS, upperValueS, lowerValueV, upperValueV):
    newImg = np.zeros((height, width))
    for i in range(height - 1):
        for j in range(width - 1):
            b = frame[i, j][0]
            g = frame[i, j][1]
            r = frame[i, j][2]

            #print("round")
#
            #print(b)
            #print(g)
            #print(r)
            #print(upperValueV)
            #print(lowerValueV)

            if upperValueH > b > lowerValueH and upperValueS > g > lowerValueS and upperValueV > r > lowerValueV:
                newImg[i, j] = 255
                print("yo")
            else:
                newImg[i, j] = 0

    print(newImg)
    return newImg

while(True):
    ret, frame = cap.read()
    height = frame.shape[0]
    width = frame.shape[1]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('before', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    lower_redH = np.array([0])
    upper_redH = np.array([5])
    lower_redS = np.array([120])
    upper_redS = np.array([255])
    lower_redV = np.array([150])
    upper_redV = np.array([255])


    newImg = ourInRange(frame, lower_redH, upper_redH, lower_redS, upper_redS, lower_redV, upper_redV)

    cv2.imshow('frame', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

