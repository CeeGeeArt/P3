import Collision
import Laser
import Target
import Mirror
import math
import cv2


class Blocker:
    x3 = 0
    x4 = 0
    y3 = 0
    y4 = 0
    mirrorState = 0

    def __init__(self, x1, y1, x2, y2, img):
        self.x3 = x1
        self.x4 = x2
        self.y3 = y1
        self.y4 = y2
        self.mirrorState = 0
        topLCorner = (x1, y1)
        topRCorner = (x2, y1)
        bottomLCorner = (x1, y2)
        bottomRCorner = (x2, y2)

        cv2.rectangle(img, topLCorner, bottomRCorner, (255, 255, 255), 2)

    def getX3(self):
        return self.x3

    def getX4(self):
        return self.x4

    def getY3(self):
        return self.y3

    def getY4(self):
        return self.y4

    def getMirrorState(self):
        return self.mirrorState
