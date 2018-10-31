import math
import cv2
import numpy as np



def masking(frame, lower, upper):
    mask = cv2.inRange(frame, lower, upper)
    # res is for testing. It allows us to see the colors
    #res = cv2.bitwise_and(frame, frame, mask=mask)
    return mask


def edgeDetection(frame):
    # Identify edges. 1. blur 2. use closing 3. detect edges
    blur = cv2.GaussianBlur(frame, (3, 3), 0)
    kernel = np.ones((9, 9), np.uint8)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)
    edges = cv2.Canny(closing, 50, 150, apertureSize=3)
    return edges

def houghLines(frame):
    lines = cv2.HoughLines(frame, 1, math.pi / 180.0, 130, np.array([]), 0, 0)

    if (lines is None or len(lines) == 0):
        print("No lines found")
        return (0,0), (0,0)
    else:
        a, b, c = lines.shape
        for i in range(a):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0, y0 = a * rho, b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            return pt1, pt2

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()

    # Red
    lower_red = np.array([0, 0, 150])
    upper_red = np.array([100, 100, 255])
    mask_red = masking(frame, lower_red, upper_red)

    # Blue
    lower_blue = np.array([150, 0, 0])
    upper_blue = np.array([255, 130, 130])
    mask_blue = masking(frame, lower_blue, upper_blue)

    # Edge detection on a mask of the red colors
    edges = edgeDetection(mask_red)

    # Houghlines on edges
    pt1, pt2 = houghLines(edges)
    cv2.line(frame, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)


    # params = cv2.SimpleBlobDetector_Params()
    # params.filterByCircularity = True
    # params.minCircularity = 0.7
    # params.maxCircularity = 0.8
    #
    # detector = cv2.SimpleBlobDetector_create(params)
    #
    # keypoints = detector.detect(frame)
    #
    # im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255),
    #                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('Original', frame)
    cv2.imshow('red1', mask_red)
    #cv2.imshow('red2', res_red)
    #cv2.imshow('blue1', mask_blue)
    #cv2.imshow('blue2', res_blue)
    #cv2.imshow('edgeblur', blur)
    #cv2.imshow('closing', closing)
    cv2.imshow('edge', edges)
    #cv2.imshow('blob', im_with_keypoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
