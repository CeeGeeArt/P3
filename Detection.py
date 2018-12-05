# This can be deleted in the final implementation when no more testing is necessary.
import math
import cv2
import numpy as np
import BoundaryTracing
import ImageProcessingMethods


def morphOp(input):
    # Close and open to remove noise and holes in contours.
    kernel = np.ones((17, 17), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(input, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel2)

    return opening


# find contours and then return the corners of a rotated bounding rectangle.
def box_from_contours(input_mask):
    temp_box = []

    # Boundary tracing
    #im2, contours, hierarchy = cv2.findContours(input_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = BoundaryTracing.boundaryTracing(input_mask)
    contours_f = []

    # Swap x and y
    for i in range(len(contours)):
        contour = []
        for j in range(len(contours[i])):
            y, x = contours[i][j]
            contour.append((x, y))
        contours_f.append(contour)

    # contours_f = contours

    # Convert to numpy array
    contours_f = np.array(contours_f)
    for i in range(len(contours_f)):
        contours_f[i] = np.array(contours_f[i])

    # Find 4 points from a contour
    for i in range(len(contours_f)):
        cnt = contours_f[i]
        rect = cv2.minAreaRect(cnt)
        # contourArea = cv2.contourArea(cnt)
        # rectArea = rect[1][0]*rect[1][1]
        # relationship_cr = contourArea / rectArea
        # print(contourArea)
        # print(rectArea)
        # print(relationship_cr)

        box = cv2.boxPoints(rect)
        box = np.int0(box)
        temp_box.append(box)



        # Checks if the area of the contour matches with a circle or a rectangle.
        # Runs if it matches with a rectangle and is above a minimum.
        # if contourArea > 10 and relationship_cr < 1.4 and relationship_cr > 0.6:
        #     print("drawing contour")
        #     box = cv2.boxPoints(rect)
        #     box = np.int0(box)
        #     temp_box.append(box)
        # else:
        #     print("Not correct contour")

    return temp_box


def detectionRed(clean_frame):
    # blur = cv2.medianBlur(clean_frame, 5)

    # HSV and blur
    hsv = cv2.cvtColor(clean_frame, cv2.COLOR_BGR2HSV)
    blur = ImageProcessingMethods.ourMedianBlur(hsv)

    # Red
    lower_red = np.array([0, 150, 120])
    upper_red = np.array([5, 255, 255])
    mask_red = cv2.inRange(blur, lower_red, upper_red)

    # Morphological operations
    processed = morphOp(mask_red)

    cv2.imshow('thresh_red', processed)
    # Find contours
    box = box_from_contours(processed)

    return box


def detectionBlue(clean_frame):
    # blur = cv2.medianBlur(clean_frame, 15)

    # Hsv and blur
    hsv = cv2.cvtColor(clean_frame, cv2.COLOR_BGR2HSV)
    blur = ImageProcessingMethods.ourMedianBlur(hsv)

    # Blue
    lower_blue = np.array([100, 90, 90])
    upper_blue = np.array([115, 255, 255])
    mask_blue = cv2.inRange(blur, lower_blue, upper_blue)

    # Morphological operations
    processed = morphOp(mask_blue)

    # Find contours
    box = box_from_contours(processed)

    return box