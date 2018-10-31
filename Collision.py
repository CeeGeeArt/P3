import sys

import Mirror
import Blocker
import Target
import Laser
import math
import cv2


class Collision:

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    x3 = 0
    x4 = 0
    y3 = 0
    y4 = 0

    def __init__(self, mirror, laser):
        self.x1 = laser.getX1()
        self.x2 = laser.getX2()
        self.y1 = laser.getY1()
        self.y2 = laser.getY2()
        self.x3 = mirror.getX3()
        self.x4 = mirror.getX4()
        self.y3 = mirror.getY3()
        self.y4 = mirror.getY4()

    def __init__(self, blocker, laser):
        self.x1 = laser.getX1()
        self.x2 = laser.getX2()
        self.y1 = laser.getY1()
        self.y2 = laser.getY2()
        self.x3 = blocker.getX3()
        self.x4 = blocker.getX4()
        self.y3 = blocker.getY3()
        self.y4 = blocker.getY4()

    def collisionLeft(self, img):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        x3 = self.x3
        x4 = self.x3
        y3 = self.y3
        y4 = self.y4
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)),
                     (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000, 100000, 0

    def collisionRight(self, img):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        x3 = self.x4
        x4 = self.x4
        y3 = self.y3
        y4 = self.y4
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)),
                     (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000, 100000, 0

    def collisionTop(self, img):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        x3 = self.x3
        x4 = self.x4
        y3 = self.y3
        y4 = self.y3
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)),
                     (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000, 100000, 0

    def collisionBottom(self, img):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        x3 = self.x3
        x4 = self.x4
        y3 = self.y4
        y4 = self.y4
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)),
                     (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000, 100000, 0

    def findSmallDistance(self, x1, y1, cx1, cy1, cx2, cy2):
        distanceToPoint1 = math.sqrt((((x1) - (cx1)) ** 2) + (((y1) - (cy1)) ** 2))
        distanceToPoint2 = math.sqrt((((x1) - (cx2)) ** 2) + (((y1) - (cy2)) ** 2))

        if distanceToPoint1 > distanceToPoint2:
            return cx2, cy2
        else:
            return cx1, cy1

    def findBiggestDistance(self, x1, y1, cx1, cy1, cx2, cy2):
        distanceToPoint1 = math.sqrt((((x1) - (cx1)) ** 2) + (((y1) - (cy1)) ** 2))
        distanceToPoint2 = math.sqrt((((x1) - (cx2)) ** 2) + (((y1) - (cy2)) ** 2))

        if distanceToPoint1 > distanceToPoint2:
            return cx1, cy1
        else:
            return cx2, cy2


    def collisionDetection(self, img):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        topX, topY, topState = self.collisionTop(img)
        bottomX, bottomY, bottomState = self.collisionBottom(img)
        rightX, rightY, rightState = self.collisionRight(img)
        leftX, leftY, leftState = self.collisionLeft(img)

        cx1 = 0
        cy1 = 0
        cx2 = 0
        cy2 = 0

        if topState == 1:
            cx1 = topX
            cy1 = topY
            if bottomState == 1:
                cx2 = bottomX
                cy2 = bottomY
            elif rightState == 1:
                cx2 = rightX
                cy2 = rightY
            elif leftState == 1:
                cx2 = leftX
                cy2 = leftY
        elif bottomState == 1:
            cx1 = bottomX
            cy1 = bottomY
            if rightState == 1:
                cx2 = rightX
                cy2 = rightY
            elif leftState == 1:
                cx2 = leftX
                cy2 = leftY
        elif rightState == 1:
            cx1 = rightX
            cy1 = rightY
            if leftState == 1:
                cx2 = leftX
                cy2 = leftY
        elif leftState == 1:
            cx1 = leftX
            cy1 = leftY

        dX, dY = self.findSmallDistance(x1, y1, cx1, cy1, cx2, cy2)

        if 0 < dX and 0 < dY:
            return self.findSmallDistance(x1, y1, cx1, cy1, cx2, cy2)
        else:
            height, width, channels = img.shape
            screen = Blocker.Blocker(0, 0, width, height, img)
            tempLaser = Laser.Laser(self.x1, self.y1, self.x2, self.y2, img)
            tempCol = Collision(screen, tempLaser)
            topX, topY, topState = tempCol.collisionTop(img)
            bottomX, bottomY, bottomState = tempCol.collisionBottom(img)
            rightX, rightY, rightState = tempCol.collisionRight(img)
            leftX, leftY, leftState = tempCol.collisionLeft(img)

            cx1 = 0
            cy1 = 0
            cx2 = 0
            cy2 = 0

            if topState == 1:
                cx1 = topX
                cy1 = topY
                if bottomState == 1:
                    cx2 = bottomX
                    cy2 = bottomY
                elif rightState == 1:
                    cx2 = rightX
                    cy2 = rightY
                elif leftState == 1:
                    cx2 = leftX
                    cy2 = leftY
            elif bottomState == 1:
                cx1 = bottomX
                cy1 = bottomY
                if rightState == 1:
                    cx2 = rightX
                    cy2 = rightY
                elif leftState == 1:
                    cx2 = leftX
                    cy2 = leftY
            elif rightState == 1:
                cx1 = rightX
                cy1 = rightY
                if leftState == 1:
                    cx2 = leftX
                    cy2 = leftY
            elif leftState == 1:
                cx1 = leftX
                cy1 = leftY
            return self.findBiggestDistance(x1, y1, cx1, cy1, cx2, cy2)
