import math
import cv2
import numpy as np

class Detection:
    cap = cv2.VideoCapture(0)

    while (1):

        _, frame = cap.read()
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red
        lower_red = np.array([0, 0, 150])
        upper_red = np.array([100, 100, 255])
        mask_red = cv2.inRange(frame, lower_red, upper_red)
        res_red = cv2.bitwise_and(frame, frame, mask= mask_red)

        # Blue
        lower_blue = np.array([150, 0, 0])
        upper_blue = np.array([255, 130, 130])
        mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
        res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

        edges = cv2.Canny(res_red, 100, 200)


        params = cv2.SimpleBlobDetector_Params()
        params.filterByCircularity = True
        params.minCircularity = 0.7
        params.maxCircularity = 0.8

        detector = cv2.SimpleBlobDetector_create(params)

        keypoints = detector.detect(frame)

        im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow('Original', frame)
        #cv2.imshow('red1', mask_red)
        cv2.imshow('red2', res_red)
        #cv2.imshow('blue1', mask_blue)
        cv2.imshow('blue2', res_blue)
        cv2.imshow('edge', edges)
        cv2.imshow('blob', im_with_keypoints)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()
