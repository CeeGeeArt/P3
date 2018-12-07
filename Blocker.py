import Collision
import Laser
import Target
import Mirror
import math
import cv2


class Blocker:
    rectangleX1 = 0
    rectangleX2 = 0
    rectangleX3 = 0
    rectangleX4 = 0

    rectangleY1 = 0
    rectangleY2 = 0
    rectangleY3 = 0
    rectangleY4 = 0

    topLCorner = (0, 0)
    topRCorner = (0, 0)
    bottomLCorner = (0, 0)
    bottomRCorner = (0, 0)

    mirrorState = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, img):
        self.rectangleX1 = x1
        self.rectangleX2 = x2
        self.rectangleX3 = x3
        self.rectangleX4 = x4

        self.rectangleY1 = y1
        self.rectangleY2 = y2
        self.rectangleY3 = y3
        self.rectangleY4 = y4

        self.mirrorState = 0

        self.topLCorner = (x1, y1)
        self.topRCorner = (x4, y4)
        self.bottomLCorner = (x2, y2)
        self.bottomRCorner = (x3, y3)

    def drawBlocker(self, img):
        cv2.line(img, self.topLCorner, self.bottomLCorner, (0, 0, 255), 2)
        cv2.line(img, self.topRCorner, self.bottomRCorner, (0, 0, 255), 2)
        cv2.line(img, self.topLCorner, self.topRCorner, (0, 0, 255), 2)
        cv2.line(img, self.bottomLCorner, self.bottomRCorner, (0, 0, 255), 2)

    def getRectangleX1(self):
        return self.rectangleX1

    def getRectangleX2(self):
        return self.rectangleX2

    def getRectangleX3(self):
        return self.rectangleX3

    def getRectangleX4(self):
        return self.rectangleX4

    def getRectangleY1(self):
        return self.rectangleY1

    def getRectangleY2(self):
        return self.rectangleY2

    def getRectangleY3(self):
        return self.rectangleY3

    def getRectangleY4(self):
        return self.rectangleY4

    def getMirrorState(self):
        return self.mirrorState
