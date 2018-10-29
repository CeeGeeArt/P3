import math
import cv2
import numpy as np

class detection:
    cap = cv2.VideoCapture(0)

    while (1):

        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        
        edges = cv2.Canny(frame, 100, 200)

        cv2.imshow('Original', frame)
        cv2.imshow('redthresh', edges)
        cv2.imshow('bluethresh', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()
