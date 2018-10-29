import math

import numpy as np
import cv2
import time

img = cv2.imread('test.jpg')

class rectangle:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    def __init__(self, x1, y1, x2, y2, img):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        topLCorner = (x1, y1)
        topRCorner = (x2, y1)
        bottomLCorner = (x1, y2)
        bottomRCorner = (x2, y2)

        cv2.rectangle(img, topLCorner, bottomRCorner, (255, 255, 255), 2)


    def collisionLeft(self, x1, y1, x2, y2, img):
        x3 = self.x1
        x4 = self.x1
        y3 = self.y1
        y4 = self.y2
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)), (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000,100000 , 0

    def collisionRight(self, x1, y1, x2, y2, img):
        x3 = self.x2
        x4 = self.x2
        y3 = self.y1
        y4 = self.y2
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)), (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000,100000, 0

    def collisionTop(self, x1, y1, x2, y2, img):
        x3 = self.x1
        x4 = self.x2
        y3 = self.y1
        y4 = self.y1
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)), (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000,100000, 0

    def collisionBottom(self, x1, y1, x2, y2, img):
        x3 = self.x1
        x4 = self.x2
        y3 = self.y2
        y4 = self.y2
        intersectionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        if intersectionY >= y3 and intersectionY <= y4 and intersectionX >= x3 and intersectionX <= x4:
            cv2.line(img, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)), (255, 0, 0), 5)
            return int(intersectionX), int(intersectionY), 1
        else:
            return 100000,100000, 0

    def findSmallDistance(self, x1, y1, cx1, cy1, cx2, cy2):
        distanceToPoint1 = math.sqrt((((x1) - (cx1)) ** 2) + (((y1) - (cy1)) ** 2))
        distanceToPoint2 = math.sqrt((((x1) - (cx2)) ** 2) + (((y1) - (cy2)) ** 2))

        if distanceToPoint1 > distanceToPoint2:
            return cx2, cy2
            print('2')
        else:
            return cx1, cy1
            print('1')


    # 1 remove 2 with true/false for colision
    # 2 Measure distance from start point to both col
    # 3 find smallest distance and make that new end point

    def collisionDetection(self, x1, y1, x2, y2, img):
        topX, topY, topState = self.collisionTop(x1, y1, x2, y2, img)
        bottomX, bottomY, bottomState = self.collisionBottom(x1, y1, x2, y2, img)
        rightX, rightY, rightState = self.collisionRight(x1, y1, x2, y2, img)
        leftX, leftY, leftState = self.collisionLeft(x1, y1, x2, y2, img)

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
            return x2, y2






def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 100
    lsY = int(vRow/2)
    leX = int(vCol-50)
    leY = int(vRow/2)+200
    osX = int(vCol/3)
    osY = int(vRow/2)-100
    oeX = vCol-100
    oeY = int(vRow/2)+100
    x1 = lsX
    x2 = leX
    x3 = x1
    x4 = x2
    y1 = lsY
    y2 = leY
    y3 = y1 - 150
    y4 = y2- 150

    testRect = rectangle(100, 100, 200, 200, img)
    testRect2 = rectangle(osX, osY, oeX, oeY, img)

    cv2.line(videoFeed, (lsX, lsY), (leX, leY), (0, 255, 0), 5)

    testRect.collisionDetection(x1,y1,x2,y2, img)

    leX, leY = testRect2.collisionDetection(x1,y1,x2,y2, img)

    cv2.line(img, (lsX, lsY), (leX, leY), (0, 0, 255), 5)


cap = cv2.VideoCapture(0)

ret, last_frame = cap.read()

if last_frame is None:
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()

    if frame is None:
        exit()

    laserFire(frame,20,0.2) #Call to laser function
    cv2.imshow('frame', frame)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", img)

    if cv2.waitKey(33) >= 0:
        break

    last_frame = frame

cap.release()
cv2.destroyAllWindows()