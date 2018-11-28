import cv2
import numpy as np
import turtle


class Target:
    doublePoints = False
    positionX = 0
    positionY = 0
    radius = 25
    color = (80, 250, 250)

    def __init__(self, doublePoints, positionX, positionY):
        self.doublePoints = doublePoints
        self.positionX = positionX
        self.positionY = positionY

    def drawCircle(self, img):
        cv2.circle(img, (self.positionX, self.positionY), self.radius, self.color, thickness=-1, lineType=8, shift=0)

    # Checks collision between the target and all lines. Should also check which team the laser belongs to.
    def targetCollision(self, laserArray):
        print(len(laserArray))
        target_col = []
        for i in range(len(laserArray)):
            print("New laser check ------------------------"+ str(i))
            x1 = laserArray[i].getX1()
            y1 = laserArray[i].getY1()
            p1 = x1, y1
            x2 = laserArray[i].getX2()
            y2 = laserArray[i].getY2()
            p2 = x2, y2
            print('Point 1', p1, 'Point 2', p2)
            if Target.intersect_lc(p1, p2, self.positionX, self.positionY, self.radius):
                print(" Target Collision -----------------------------------------")
                target_col.append(True)
        for i in range(len(target_col)):
            if target_col[i]:
                return True, self.doublePoints
        return False, False

    # Checks if there is an intersection between a line and a circle
    @staticmethod
    def intersect_lc(p1, p2, cx, cy, r):
        x1, y1 = p1
        x2, y2 = p2

        # Checks if an endpoint of the line is within the circle
        inside1 = Target.inside_pc(x1, y1, cx, cy, r)
        inside2 = Target.inside_pc(x2, y2, cx, cy, r)
        if inside1 or inside2:
            return True

        # Find the length of the line.
        distX = x1 - x2
        distY = y1 - y2
        lineLength = np.sqrt((distX * distX) + (distY * distY))

        # Calculate the dot product.
        dotProduct = (((cx - x1) * (x2 - x1)) + ((cy - y1) * (y2 - y1))) / (lineLength * lineLength)

        # Find the closest point on the line.
        closestX = x1 + (dotProduct * (x2 - x1))
        closestY = y1 + (dotProduct * (y2 - y1))
        closestP = (closestX, closestY)

        # Check if point is on the line.
        onSegment = Target.pointOnLine(p1, p2, closestP)
        if not onSegment:
            print("OnSegment ---------------------------------")
            return False

        distX = closestX - cx
        distY = closestY - cy
        distance = np.sqrt((distX * distX) + (distY * distY))

        print(distance)
        if distance <= r:
            return True
        print("The end ----------------------------------------")
        return False

    # Checks if a point is inside of a circle.
    @staticmethod
    def inside_pc(px, py, cx, cy, r):
        distX = px - cx
        distY = py - cy
        distance = np.sqrt((distX * distX) + (distY * distY))
        # if the distance is less than the circle's
        # radius the point is inside!
        if distance <= r:
            return True
        return False

    # Checks if a point is on a line.
    @staticmethod
    def pointOnLine(p1, p2, p3):
        # Get distance from point to the ends of the line
        print("Points")
        print(p1)
        print(p2)
        print(p3)
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)
        d1 = np.linalg.norm(p3 - p1)
        d2 = np.linalg.norm(p3 - p2)

        # get the length of the lines
        lineLen = np.linalg.norm(p1 - p2)
        calc_len = d1+d2
        print("Line lengths")
        print(lineLen)
        print(d1)
        print(d2)
        print(d1+d2)

        # Buffer since collision can be iffy with the minute accuracy of floats.
        buffer = 1  # higher number = less accurate

        # Resolves to true if the length of the line is equal to
        # the sum of the two distances.
        if d1 + d2 >= lineLen - buffer and d1 + d2 <= lineLen + buffer:
            return True
        return False
