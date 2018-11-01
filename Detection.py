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
def houghLines(pFrame):
    edges = cv2.Canny(pFrame, 50, 150, apertureSize=3)
    cv2.imshow('edge', edges)
    #lines = cv2.HoughLines(edges, 1, math.pi / 180.0, 60, np.array([]), 0, 0)

    minLineLength = 1
    maxLineGap = 20
    lines = cv2.HoughLinesP(edges, 1, math.pi / 180, 100, 0, minLineLength, maxLineGap)

    print("lines" + str(lines))
    if (lines is None or len(lines) == 0):
            print("No lines found")
            return (0,0), (0,0)
    else:
        temp_pt1 = []
        temp_pt2 = []
        N = lines.shape[0]
        for i in range(N):
            x1 = lines[i][0][0]
            x2 = lines[i][0][1]
            y1 = lines[i][0][2]
            y2 = lines[i][0][3]
            pt1 = (x1, y1)
            pt2 = (x2, y2)
            temp_pt1.append(pt1)
            temp_pt2.append(pt2)
        print("temp_pt1 " + str(temp_pt1))
        return temp_pt1, temp_pt2


    # if (lines is None or len(lines) == 0):
    #     print("No lines found")
    #     return (0,0), (0,0)
    # else:
    #     a, b, c = lines.shape
    #     temp_pt1 = []
    #     temp_pt2 = []
    #     for i in range(a):
    #         rho = lines[i][0][0]
    #         theta = lines[i][0][1]
    #         a = math.cos(theta)
    #         b = math.sin(theta)
    #         x0, y0 = a * rho, b * rho
    #         pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
    #         pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
    #         temp_pt1.append(pt1)
    #         temp_pt2.append(pt2)
    #     print("pt lenght " + str(len(temp_pt1)))
    #     return temp_pt1, temp_pt2


def blobDetection(mask, frame):
    params = cv2.SimpleBlobDetector_Params()

    # Filter by circularity
    params.filterByCircularity = True
    params.minCircularity = 0.7
    params.maxCircularity = 0.8

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 150
    params.maxArea = 150000

    detector = cv2.SimpleBlobDetector_create(params)

    ret, new_mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY_INV)
    keypoints = detector.detect(new_mask)

    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 255, 0),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return im_with_keypoints, keypoints


def createMask(keypoints):
    # Create masks for individual blobs
    temp_arrayHolder = []
    for i in range(len(keypoints)):
        x = keypoints[i].pt[0]
        y = keypoints[i].pt[1]
        temp_array = np.zeros(shape=mask_red.shape)
        for x1 in range(-75, 75):
            # Prevents out of bounds when the keypoint is close to the edge of the screen.
            if(x1+x < temp_array.shape[1] and x1+x >= 0):
                for y1 in range(-75, 75):
                    # Prevents out of bounds when the keypoint is close to the edge of the screen.
                    if(y1+y < temp_array.shape[0] and y1+y >= 0):
                        y_f = int(y + y1)
                        x_f = int(x + x1)
                        temp_array[y_f, x_f] = 255
        temp_arrayHolder.append(temp_array)
    return temp_arrayHolder


cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()

    print("New Iteration")
    # Red
    lower_red = np.array([0, 0, 150])
    upper_red = np.array([100, 100, 255])
    mask_red = masking(frame, lower_red, upper_red)

    # Blue
    lower_blue = np.array([150, 0, 0])
    upper_blue = np.array([255, 130, 130])
    mask_blue = masking(frame, lower_blue, upper_blue)

    # Detect blobs
    keypoint_image, keypoints = blobDetection(mask_red, frame)

    # Create list of masks for individual blobs
    maskList = createMask(keypoints)

    # Use maskList to separate BLOBS in the picture.
    if len(maskList) < 1:
        print("no mask")
    else:
        masked = cv2.inRange(maskList[0], 150, 255)
        red1 = cv2.bitwise_and(mask_red, mask_red, mask=masked)
        # Houghlines on edges. Returns two arrays of points.
        pt1, pt2 = houghLines(red1)
        # Draw lines based on points
        if type(pt1[0]) is tuple:
            for i in range(len(pt1)):
                cv2.line(frame, pt1[i], pt2[i], (0, 0, 255), 2, cv2.LINE_AA)

    if len(maskList) < 2:
        print("no mask")
    else:
        masked2 = cv2.inRange(maskList[0], 150, 255)
        red2 = cv2.bitwise_and(mask_red, mask_red, mask=masked2)
        # Houghlines on edges
        #pt1, pt2 = houghLines(red1)
        #cv2.line(frame, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    # Display stuff
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
    if len(maskList) < 1:
        print("no mask")
    else:
        cv2.imshow('createdMask1', red1)
    if len(maskList) < 2:
        print("no mask")
    else:
        cv2.imshow('createdMask2', red2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
