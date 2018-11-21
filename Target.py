import cv2
import numpy as np



class Target:
    doublePoints = False
    positionX = 0
    positionY = 0
    radius = 50
    color = np.array([255, 255, 255])

    def __init__(self, doublePoints, positionX, positionY):
        self.doublePoints = doublePoints
        self.positionX = positionX
        self.positionY = positionY

    # Checks collision between the target and all lines. Should also check which team the laser belongs to.
    def targetCollision(self, laserArray):
        for i in range(len(laserArray)):  # No laserArray exists at this moment.
            x1 = laserArray[i].getX1()
            y1 = laserArray[i].getY1()
            p1 = x1, y1
            x2 = laserArray[i].getX2()
            y2 = laserArray[i].getY2()
            p2 = x2, y2
            print('Point 1', p1, 'Point 2', p2)
            if Target.intersect_lc(p1, p2, self.positionX, self.positionY, self.radius):
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
        dotProduct = (((cx - x1) * (x2 - x1)) + ((cy - y1) * (y2 - y1))) / pow(lineLength, 2)

        # Find the closest point on the line.
        closestX = x1 + (dotProduct * (x2 - x1))
        closestY = y1 + (dotProduct * (y2 - y1))
        closestP = (closestX, closestY)

        # Check if point is on the line.
        onSegment = Target.pointOnLine(p1, p2, closestP)
        if not onSegment:
            return False

        distX = closestX - cx
        distY = closestY - cy
        distance = np.sqrt((distX * distX) + (distY * distY))

        if distance <= r:
            return True
        return False

    # Checks if a point is inside of a circle.
    @staticmethod
    def inside_pc(px, py, cx, cy, r):
        print("-----------------------------------------------------------------------")
        print(px)
        print(type(px))
        print(cx)
        print(type(cx))
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
        # Get distance from point two the ends of the line
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)
        d1 = np.linalg.norm(p3 - p1)
        d2 = np.linalg.norm(p3 - p2)

        # get the length of the line
        lineLen = np.linalg.norm(p1 - p2)

        # Buffer since collision can be iffy with the minute accuracy of floats.
        buffer = 0.1  # higher number = less accurate

        # Resolves to true if the length of the line is equal to
        # the sum of the two distances.
        if d1 + d2 >= lineLen - buffer and d1 + d2 <= lineLen + buffer:
            return True
        return False