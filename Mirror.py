#import Collision
#import Laser
#import Target
#import Blocker
import cv2
import math


class Mirror:
    x3 = 0
    x4 = 0
    y3 = 0
    y4 = 0

    def __init__(self, x1, y1, x2, y2, img):
        self.x3 = x1
        self.x4 = x2
        self.y3 = y1
        self.y4 = y2
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

def angleDetermine(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ax = ax2 - ax1
    ay = ay2 - ay1
    bx = bx2 - bx1
    by = by2 - by1

    VECa = (ax, ay)
    VECb = (bx, by)
    MAGa = int(math.sqrt(math.pow(ax, 2) + math.pow(ay,2)))
    MAGb = int(math.sqrt(math.pow(bx, 2) + math.pow(by, 2)))

    cosAngle = (VECa * VECb)/(MAGa * MAGb)

    angle = math.acos(cosAngle)

    x1 = ax1
    y1 = ay1
    x2 = x1 + VECa * math.cos(angle)
    y2 = y1 + VECa * math.sin(angle)

    return x2, y2


line = (50, 50, 70, 70)
line2 = (150, 100, 150, 300)

angleDetermine(50, 50, 70, 70, 150, 100, 150, 300)
