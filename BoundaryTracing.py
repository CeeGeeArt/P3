temp_coordinates = (0, 0)
temp_contour = []
previous_contours = []
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
    global counter_left
    global counter_top
    global counter_right
    global counter_bottom
    global start_y
    global start_x

    height, width = input_thresh.shape
    contours = []
    previous_contours.clear()

    # Scan the image
    for i in range(1, height-1, 10):
        for j in range(1, width-1):

            # Check if pixel == colored.
            if input_thresh[i][j] > 0:
                # Check if pixel == a part of a previously found contour and then starts tracing.
                if checkPixel(i, j):
                    temp_contour = []
                    contour = moore_control(i, j, input_thresh)
                    contours.append(contour)

    return contours


def moore_control(y, x, input_thresh):
    global temp_coordinates
    global temp_contour
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
    stop_counter = 0

    while True:
        stop_counter += 1
        if stop_counter > 2000:
            break
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

    previousContours(temp_contour)

    return temp_contour


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

    if start_y == y and start_x == x:
        counter_left += 1

    # Start tracing the boundary
    if input_thresh[y][x] > 0 and counter_left < 3:
        # Add previously found contour to array - y, x are flipped
        temp_contour.append((x, y))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            return y-1, x-1, bottom

        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            return y - 1, x, left

        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            return y - 1, x + 1, left

        elif input_thresh[y][x+1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            return y, x + 1, top

        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            return y + 1, x + 1, top

        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            return y + 1, x, right

        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
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

    if start_y == y and start_x == x:
        counter_top += 1

    # Start tracing the boundary
    if input_thresh[y][x] > 0 and counter_top < 2:
        # Add previously found contour to array - y, x are flipped
        temp_contour.append((x, y))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            return y - 1, x + 1, left

        elif input_thresh[y][x + 1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            return y, x + 1, top

        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            return y + 1, x + 1, top

        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            return y + 1, x, right

        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            return y + 1, x, right

        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            return y - 1, x - 1, bottom

        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
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

    if start_y == y and start_x == x:
        counter_right += 1

    # Start tracing the boundary
    if input_thresh[y][x] > 0 and counter_right < 2:
        # Add previously found contour to array - y, x are flipped
        temp_contour.append((x, y))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            return y + 1, x + 1, top

        elif input_thresh[y + 1][x] > 0 and y + 1 != 0 and x != 0 and y + 1 != height - 1 and x != width - 1:
            return y + 1, x, right

        elif input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            return y + 1, x - 1, right

        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            return y, x - 1, bottom

        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            return y - 1, x - 1, bottom

        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            return y - 1, x, left

        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
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

    if start_y == y and start_x == x:
        counter_bottom += 1

    # Start tracing the boundary
    if input_thresh[y][x] > 0 and counter_bottom < 2:
        # Add previously found contour to array - y, x are flipped
        temp_contour.append((x, y))

        # Check the surrounding moore neighborhood for white pixels.
        if input_thresh[y + 1][x - 1] > 0 and y + 1 != 0 and x - 1 != 0 and y + 1 != height - 1 and x - 1 != width - 1:
            return y + 1, x - 1, right

        elif input_thresh[y][x - 1] > 0 and y != 0 and x - 1 != 0 and y != height - 1 and x - 1 != width - 1:
            return y, x - 1, bottom

        elif input_thresh[y - 1][x - 1] > 0 and y - 1 != 0 and x - 1 != 0 and y - 1 != height - 1 and x - 1 != width - 1:
            return y - 1, x - 1, bottom

        elif input_thresh[y - 1][x] > 0 and y - 1 != 0 and x != 0 and y - 1 != height - 1 and x != width - 1:
            return y - 1, x, left

        elif input_thresh[y - 1][x + 1] > 0 and y - 1 != 0 and x + 1 != 0 and y - 1 != height - 1 and x + 1 != width - 1:
            return y - 1, x + 1, left

        elif input_thresh[y][x + 1] > 0 and y != 0 and x + 1 != 0 and y != height - 1 and x + 1 != width - 1:
            return y, x + 1, top

        elif input_thresh[y + 1][x + 1] > 0 and y + 1 != 0 and x + 1 != 0 and y + 1 != height - 1 and x + 1 != width - 1:
            return y + 1, x + 1, top

        else:
            print("WTF")
    else:
        return y, x, 10


def previousContours(contour):
    global previous_contours
    x_sort = []
    y_sort = []
    for i in range(len(contour)):
        y, x = contour[i]
        x_sort.append(x)
        y_sort.append(y)
    x_max = max(x_sort)
    x_min = min(x_sort)
    y_max = max(y_sort)
    y_min = min(y_sort)

    previous_contours.append((x_min, x_max, y_min, y_max))


def checkPixel(y, x):
    global previous_contours
    res = True
    for i in range(len(previous_contours)):
        x_min, x_max, y_min, y_max = previous_contours[i]

        if y_min <= y <= y_max and x_min <= x <= x_max:
            res = False
            break

    return res