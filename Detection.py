# This can be deleted in the final implementation when no more testing is necessary.
import math
import cv2
import numpy as np


# Creates a mask based on the colors specified in the boundaries.
def masking(input_frame, lower, upper):
    mask = cv2.inRange(input_frame, lower, upper)
    #blur = cv2.GaussianBlur(mask, (3, 3), 0)
    kernel = np.ones((11, 11), np.uint8)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # res is for testing. It allows us to see the colors
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    return closing


# Calculates two points that can be used to draw a line.
def myHoughLines(pFrame):
    edges = cv2.Canny(pFrame, 50, 150, apertureSize=3)

    #cv2.imshow('edge', edges)

    # Houghlines function
    minLineLength = 2
    maxLineGap = 20
    lines = cv2.HoughLinesP(edges, 1, math.pi / 180, 40, np.array([]), minLineLength, maxLineGap)

    # Use the lines returned by HoughLinesP to create two arrays of points that can be returned.
    if (lines is None or len(lines) == 0):
        print("No lines found")
        return (0, 0), (0, 0)
    else:
        temp_pt1 = []
        temp_pt2 = []
        N = lines.shape[0]
        for i in range(N):
            x1 = lines[i][0][0]
            y1 = lines[i][0][1]
            x2 = lines[i][0][2]
            y2 = lines[i][0][3]
            pt1 = (x1, y1)
            pt2 = (x2, y2)
            temp_pt1.append(pt1)
            temp_pt2.append(pt2)
        return temp_pt1, temp_pt2


def blobDetection(mask, input_frame):
    params = cv2.SimpleBlobDetector_Params()

    # Filter by circularity
    params.filterByCircularity = True
    params.minCircularity = 0.2
    params.maxCircularity = 0.8

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 150
    params.maxArea = 150000

    detector = cv2.SimpleBlobDetector_create(params)

    # Create an inverted mask to BLOB detect on.
    ret, new_mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY_INV)

    # BLOB detect
    keypoints = detector.detect(new_mask)

    # Create an image with circles around the detected BLOBs
    im_with_keypoints = cv2.drawKeypoints(input_frame, keypoints, np.array([]), (0, 255, 0),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return im_with_keypoints, keypoints


def createMask(keypoints, mask):
    # Create masks for individual blobs
    temp_arrayHolder = []
    maskSize = 50
    for i in range(len(keypoints)):
        x = keypoints[i].pt[0]
        y = keypoints[i].pt[1]
        temp_array = np.zeros(shape=mask.shape)
        for x1 in range(-maskSize, maskSize):
            # Prevents out of bounds when the keypoint is close to the edge of the screen.
            if x1 + x < temp_array.shape[1] and x1 + x >= 0:
                for y1 in range(-maskSize, maskSize):
                    # Prevents out of bounds when the keypoint is close to the edge of the screen.
                    if y1 + y < temp_array.shape[0] and y1 + y >= 0:
                        y_f = int(y + y1)
                        x_f = int(x + x1)
                        temp_array[y_f, x_f] = 255
        temp_arrayHolder.append(temp_array)
    return temp_arrayHolder


def retrieveLines(inputList, mask):
    if len(inputList) < 1:
        print("no mask")
    else:
        # loop this to draw multiple outputs of lines.
        for i in range(0, len(inputList)):
            masked = cv2.inRange(inputList[i], 150, 255)
            red1 = cv2.bitwise_and(mask, mask, mask=masked)
            # Houghlines on edges. Returns two arrays of points.
            pt1, pt2 = myHoughLines(red1)
            # Draw lines based on points
            if type(pt1[0]) is tuple:
                for i in range(len(pt1)):
                    cv2.line(frame, pt1[i], pt2[i], (0, 0, 255), 2, cv2.LINE_AA)


def box_from_contours(input_mask):
    # Close and open to remove noise and holes in contours.
    kernel = np.ones((17, 17), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(input_mask, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel2)

    # find contours and then find the corners of a rotated bounding rectangle.
    temp_box = []
    im2, contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        rect = cv2.minAreaRect(cnt)
        contourArea = cv2.contourArea(cnt)
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        circArea = radius * radius * np.pi
        rectArea = rect[1][0]*rect[1][1]
        relationship_cc = contourArea / circArea
        relationship_cr = contourArea / rectArea

        # Checks if the area of the contour matches with a circle or a rectangle.
        # Runs if it matches with a rectangle and is above a minimum.
        if (contourArea > 150 and relationship_cc < 0.8 and relationship_cr > 0.8):
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            temp_box.append(box)
    return temp_box

def detectionRed(clean_frame):
    # Red
    lower_red = np.array([0, 0, 140])
    upper_red = np.array([90, 90, 255])
    mask_red = masking(clean_frame, lower_red, upper_red)

    # Detect blobs
    #keypoint_image, keypoints = blobDetection(mask_red, clean_frame)

    # Create list of masks for individual blobs
    #maskList = createMask(keypoints, mask_red)

    # Use maskList to separate the first BLOB and then retrieve the points for each line
    # Draw lines by using the points provided by the the mask
    #retrieveLines(maskList, mask_red)

    # Find contours
    box = box_from_contours(mask_red)

    return box

def detectionBlue(clean_frame):
    # Blue
    hsv = cv2.cvtColor(clean_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 90, 90])
    upper_blue = np.array([130, 255, 255])
    mask_blue = masking(hsv, lower_blue, upper_blue)

    # Find contours
    box = box_from_contours(mask_blue)

    return box

# ----- Code for testing purposes below.

# cap = cv2.VideoCapture(0)
#
# while (1):
#     _, frame = cap.read()
#
#     print("New Iteration")
#
#     # Run the code
#     boxes = detectionRed(frame)
#
#     # Draw contour boxes.
#     for i in range(len(boxes)):
#         cv2.drawContours(frame, [boxes[i]], 0, (0, 0, 255), 2)
#
#     # Display stuff
#     cv2.imshow('Original', frame)
#
#     # Wait until q is pressed to exit loop.
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cap.release()
