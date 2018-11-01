import math
import cv2
import numpy as np

# Creates a maskv based on the colors specified in the boundaries.
def masking(frame, lower, upper):
    mask = cv2.inRange(frame, lower, upper)
    blur = cv2.GaussianBlur(mask, (3, 3), 0)
    kernel = np.ones((9, 9), np.uint8)
    closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)

    # res is for testing. It allows us to see the colors
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    return closing

# Calculates two points that can be used to draw a line. Input should be a canny image.
def houghLines(frame):
    edges = cv2.Canny(frame, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, math.pi / 180.0, 130, np.array([]), 0, 0)

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

def blobDetection(mask, frame):
    params = cv2.SimpleBlobDetector_Params()

    # Filter by circularity
    params.filterByCircularity = True
    params.minCircularity = 0.7
    params.maxCircularity = 0.8

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 150

    detector = cv2.SimpleBlobDetector_create(params)

    ret, new_mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY_INV)
    keypoints = detector.detect(new_mask)

    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 255, 0),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return im_with_keypoints, keypoints

def createMask(keypoints):
    # Create masks for individual blobs
    for i in range(len(keypoints)):
        x = keypoints[i].pt[0];
        y = keypoints[i].pt[1];
        temp_array = np.zeros(shape=mask_red.shape)
        for x1 in range(-75, 75):
            for y1 in range(-75, 75):
                y_f = int(y + y1)
                x_f = int(x + x1)
                # this will throw an out of bounds error when the detected object gets close to the edge of the screen.
                temp_array[y_f, x_f] = 255
        return temp_array

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

    # Houghlines on edges
    pt1, pt2 = houghLines(mask_red)
    cv2.line(frame, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    # Detect blobs
    keypoint_image, keypoints = blobDetection(mask_red, frame)

    print(keypoints)
    # Create masks for individual blobs
    mask = createMask(keypoints)
    print(mask)
    cv2.imshow('Original', frame)
    #cv2.imshow('red1', mask_red)
    #cv2.imshow('inverted', new_mask)
    #cv2.imshow('red2', res_red)
    #cv2.imshow('blue1', mask_blue)
    #cv2.imshow('blue2', res_blue)
    #cv2.imshow('edgeblur', blur)
    #cv2.imshow('closing', closing)
    #cv2.imshow('edge', edges)
    cv2.imshow('blob', keypoint_image)
    if (mask is None):
        print("no mask")
    else:
        cv2.imshow('createdMask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
