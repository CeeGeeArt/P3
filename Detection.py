# This can be deleted in the final implementation when no more testing is necessary.
import math
import cv2
import numpy as np
import BoundaryTracing


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
    im2, contours, hierarchy = cv2.findContours(input_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours = BoundaryTracing.boundaryTracing(input_mask)
    #print(contours)
    #contours = np.array(contours)
    #print(contours)
    print(len(contours))
    for i in range(len(contours)):
        cnt = contours[i]
        rect = cv2.minAreaRect(cnt)
        contourArea = cv2.contourArea(cnt)
        rectArea = rect[1][0]*rect[1][1]
        relationship_cr = contourArea / rectArea

        # Checks if the area of the contour matches with a circle or a rectangle.
        # Runs if it matches with a rectangle and is above a minimum.
        if contourArea > 150 and relationship_cr < 1.2 and relationship_cr > 0.8:
            print("drawing contour")
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            temp_box.append(box)
        else:
            print("Not correct contour")
    return temp_box


def detectionRed(clean_frame):
    blur = cv2.GaussianBlur(clean_frame, (11, 11), 0)

    # Red
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 90])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # Morphological operations
    processed = morphOp(mask_red)

    # Find contours
    box = box_from_contours(processed)

    return box


def detectionBlue(clean_frame):
    blur = cv2.GaussianBlur(clean_frame, (11, 11), 0)

    # Blue
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 90, 90])
    upper_blue = np.array([115, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Morphological operations
    processed = morphOp(mask_blue)

    # Find contours
    box = box_from_contours(processed)

    return box