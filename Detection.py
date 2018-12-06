# This can be deleted in the final implementation when no more testing is necessary.
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

    #closing = ImageProcessingMethods.closing(input)
    #opening = ImageProcessingMethods.opening(closing)

    return opening


# find contours and then return the corners of a rotated bounding rectangle.
def box_from_contours(input_mask):
    temp_box = []

    # Boundary tracing
    # im2, contours, hierarchy = cv2.findContours(input_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = BoundaryTracing.boundaryTracing(input_mask)
    contours_f = contours

    # Convert to numpy array
    contours_f = np.array(contours_f)
    for i in range(len(contours_f)):
        contours_f[i] = np.array(contours_f[i])

    # # Comment our while using our boundary tracing method
    # contours_f = contours

    # Find 4 points from a contour
    for i in range(len(contours_f)):
        cnt = contours_f[i]
        rect = cv2.minAreaRect(cnt)
        rectArea = rect[1][0]*rect[1][1]
        # contourArea = cv2.contourArea(cnt)
        # relationship_cr = contourArea / rectArea

        # Checks if the area of the rectangle meets a minimum
        if rectArea > 100:
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            temp_box.append(box)

    return temp_box


def detectionRed(clean_frame):
    # Red
    # lower_redH = np.array([0])
    # upper_redH = np.array([5])
    # lower_redS = np.array([120])
    # upper_redS = np.array([255])
    # lower_redV = np.array([150])
    # upper_redV = np.array([255])
    # mask_red = ImageProcessingMethods.threshold(clean_frame, lower_redH, upper_redH, lower_redS, upper_redS, lower_redV, upper_redV)

    lower_red = np.array([0, 120, 150])
    upper_red = np.array([8, 255, 255])
    mask_red = cv2.inRange(clean_frame, lower_red, upper_red)

    # Morphological operations
    processed = morphOp(mask_red)

    cv2.imshow('thresh_red', processed)
    # Find contours
    box = box_from_contours(processed)

    return box


def detectionBlue(clean_frame):
    # Blue
    # lower_blueH = np.array([100])
    # upper_blueH = np.array([115])
    # lower_blueS = np.array([90])
    # upper_blueS = np.array([255])
    # lower_blueV = np.array([90])
    # upper_blueV = np.array([255])
    # mask_blue = ImageProcessingMethods.threshold(clean_frame, lower_blueH, upper_blueH, lower_blueS, upper_blueS, lower_blueV, upper_blueV)

    lower_blue = np.array([100, 120, 150])
    upper_blue = np.array([115, 255, 255])
    mask_blue = cv2.inRange(clean_frame, lower_blue, upper_blue)

    # Morphological operations
    processed = morphOp(mask_blue)

    # Find contours
    box = box_from_contours(processed)

    return box
