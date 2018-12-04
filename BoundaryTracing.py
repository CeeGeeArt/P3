import math
import cv2
import numpy as np

temp_coordinates = (0, 0)
temp_contour = []
contours = []
counter_left = 0
counter_top = 0
counter_right = 0
counter_bottom = 0
start_y = None
start_x = None
left = 0
top = 1
right = 2
bottom = 3


def boundaryTracing(input_thresh):
    global temp_contour
    global contours
    global counter_left
    global counter_top
    global counter_right
    global counter_bottom
    global start_y
    global start_x
    height, width = input_thresh.shape

    contours.clear()

    print(height)
    print(width)

    # Scan the image
    for i in range(1, height-1, 10):
        for j in range(1, width-1):

            # Check if pixel == colored.
            if input_thresh[i][j] > 0:
                # Check if pixel == a part of a previously found contour and then starts tracing.
                if checkPixel(i, j):
                    print("Contour found")
                    temp_contour.clear()
                    moore_control(i, j, input_thresh)
                    print("something")

                    contours.append(temp_contour)
                    print("contours added")

    print("Exiting Boundary tracing")
    return contours


def moore_control(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
    global contours
    global counter_left
    global counter_top
    global counter_right
    global counter_bottom
    global start_y
    global start_x
    global left
    global top
    global right
    global bottom

    case = left
    start_y = y
    start_x = x
    counter_left = 0
    counter_top = 0
    counter_right = 0
    counter_bottom = 0

    print("while starting -----------")
    while True:
        if case == left:
            # from left
            y, x, case = moore_left(y, x, input_thresh)
        elif case == top:
            # from top
            y, x, case = moore_top(y, x, input_thresh)
        elif case == right:
            # from right
            y, x, case = moore_right(y, x, input_thresh)
        elif case == bottom:
            # from bottom
            y, x, case = moore_bottom(y, x, input_thresh)
        else:
            break
    print("while ending -----------")
    contours.append(temp_contour)


def moore_left(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
    global counter_left
    global start_y
    global start_x
    global left
    global top
    global right
    global bottom
    height, width = input_thresh.shape
    print("coordinates in left")
    print(input_thresh[start_y][start_x])
    print(start_y, start_x)
    print(y, x)
    print(counter_left)
    print(counter_top)
    print(counter_right)
    print(counter_bottom)
    if start_y == y and start_x == x:
        counter_left += 1

    if input_thresh[y][x] > 0 and counter_left < 3:
        # Start tracing the boundary
        temp_contour.append((y, x))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            # moore_bottom(y - 1, x - 1, input_thresh)
            return y-1, x-1, bottom
        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            # moore_left(y - 1, x, input_thresh)
            return y - 1, x, left
        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            # moore_left(y - 1, x + 1, input_thresh)
            return y - 1, x + 1, left
        elif input_thresh[y][x+1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            # moore_top(y, x + 1, input_thresh)
            return y, x + 1, top
        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            # moore_top(y + 1, x + 1, input_thresh)
            return y + 1, x + 1, top
        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            # moore_right(y + 1, x, input_thresh)
            return y + 1, x, right
        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            # moore_right(y + 1, x - 1, input_thresh)
            return y + 1, x - 1, right
        else:
            print("WTF")
    else:
        return y, x, 10


def moore_top(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
    global counter_top
    global left
    global top
    global right
    global bottom
    height, width = input_thresh.shape

    print("coordinates in top")
    print(start_y, start_x)
    print(y, x)
    print(counter_left)
    print(counter_top)
    print(counter_right)
    print(counter_bottom)

    if start_y == y and start_x == x:
        counter_top += 1

    if input_thresh[y][x] > 0 and counter_top < 2:
        # Start tracing the boundary
        temp_contour.append((y, x))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            # moore_left(y - 1, x + 1, input_thresh)
            return y - 1, x + 1, left
        elif input_thresh[y][x + 1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            # moore_top(y, x + 1, input_thresh)
            return y, x + 1, top
        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            # moore_top(y + 1, x + 1, input_thresh)
            return y + 1, x + 1, top
        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            # moore_right(y + 1, x, input_thresh)
            return y + 1, x, right
        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            # moore_right(
            return y + 1, x, right
        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            # moore_bottom(y, x - 1, input_thresh)
            return y - 1, x - 1, bottom
        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            # moore_bottom(y - 1, x - 1, input_thresh)
            return y - 1, x - 1, bottom
        else:
            print("WTF")
    else:
        return y, x, 10


def moore_right(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
    global counter_right
    global left
    global top
    global right
    global bottom
    height, width = input_thresh.shape

    print("coordinates in right")
    print(start_y, start_x)
    print(y, x)
    print(counter_left)
    print(counter_top)
    print(counter_right)
    print(counter_bottom)

    if start_y == y and start_x == x:
        counter_right += 1

    if input_thresh[y][x] > 0 and counter_right < 2:
        # Start tracing the boundary
        temp_contour.append((y, x))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            # moore_top(y + 1, x + 1, input_thresh)
            return y + 1, x + 1, top
        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            # moore_right(y + 1, x, input_thresh)
            return y + 1, x, right
        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            # moore_right(y + 1, x - 1, input_thresh)
            return y + 1, x - 1, right
        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            # moore_bottom(y, x - 1, input_thresh)
            return y, x - 1, bottom
        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            # moore_bottom(y - 1, x - 1, input_thresh)
            return y - 1, x - 1, bottom
        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            # moore_left(y - 1, x, input_thresh)
            return y - 1, x, left
        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            # moore_left(y - 1, x + 1, input_thresh)
            return y - 1, x + 1, left
        else:
            print("WTF")
    else:
        return y, x, 10

def moore_bottom(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
    global counter_bottom
    global left
    global top
    global right
    global bottom
    height, width = input_thresh.shape

    print("coordinates in bottom")
    print(start_y, start_x)
    print(y, x)
    print(counter_left)
    print(counter_top)
    print(counter_right)
    print(counter_bottom)

    if start_y == y and start_x == x:
        counter_bottom += 1

    if input_thresh[y][x] > 0 and counter_bottom < 2:
        # Start tracing the boundary
        temp_contour.append((y, x))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            # moore_right(y + 1, x - 1, input_thresh)
            return y + 1, x - 1, right
        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            # moore_bottom(y, x - 1, input_thresh)
            return y, x - 1, bottom
        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            # moore_bottom(y - 1, x - 1, input_thresh)
            return y - 1, x - 1, bottom
        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            # moore_left(y - 1, x, input_thresh)
            return y - 1, x, left
        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            # moore_left(y - 1, x + 1, input_thresh)
            return y - 1, x + 1, left
        elif input_thresh[y][x + 1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            # moore_top(y, x + 1, input_thresh)
            return y, x + 1, top
        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            # moore_top(y + 1, x + 1, input_thresh)
            return y + 1, x + 1, top
        else:
            print("WTF")
    else:
        return y, x, 10


def checkPixel(y, x):
    global contours
    res = True
    x_sort = []
    y_sort = []

    for i in range(len(contours)):
        for j in range(len(contours[i])):
            y, x = contours[i][j]
            x_sort.append(x)
            y_sort.append(y)

        x_max = max(x_sort)
        x_min = min(x_sort)
        y_max = max(y_sort)
        y_min = min(y_sort)

        if y_min <= y <= y_max and x_min <= x <= x_max:
            res = False

    return res