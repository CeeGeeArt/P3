#import Collision
import Laser
#import Target
#import Blocker
import cv2
import math
import numpy as np


class Mirror:

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    x3 = 0
    x4 = 0
    y4 = 0
    mirrorState = 0

    def __init__(self, x1, y1, x2, y2, img):
        self.x3 = x1
        self.x4 = x2
        self.y3 = y1
        self.y4 = y2
        self.mirrorState = 1
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


def angleDetermine(ax1, ay1, ax2, ay2, cx, cy, bx1, by1, bx2, by2, img):
    normalY = bx2 - bx1
    normalX = by1 - by2
    temp = ((bx2-bx1)**2) + ((by2 - by1)**2)
    normalLength = math.sqrt(temp)
    normalX = normalX/normalLength
    normalY = normalY/normalLength

    rayX = ax2 - cx
    rayY = ay2 - cy

    dotProduct = (rayX * normalX)+(rayY*normalY)

    dotNormalX = dotProduct*normalX
    dotNormalY = dotProduct*normalY

    reflectionEndX = ax2 - (dotNormalX * 2)
    reflectionEndY = ay2 - (dotNormalY * 2)

    #cv2.line(img, (cx, cy), (int(reflectionEndX), int(reflectionEndY)), (255, 255, 0), 5)
    return Laser.Laser(cx, cy, int(reflectionEndX), int(reflectionEndY), img), 0


def angleDetermineStillBad(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, img):
    vectorAx = ax2 - ax1
    vectorAy = ay2 - ay1
    vectorBx = bx2 - bx1
    vectorBy = by2 - by1
    vectorCx = vectorAx
    vectorCy = vectorAy

    vectorA = [vectorAx, vectorAy]
    vectorB = [vectorBx, vectorBy]
    vectorB90deg = [-vectorBy, vectorBx]
    normalVectorToBx1= ax2
    normalVectorToBx2= ax2+vectorB90deg[0]
    normalVectorToBy1= ay2
    normalVectorToBy2= ay2+vectorB90deg[1]
    normalVectorToBx = normalVectorToBx2-normalVectorToBx1
    normalVectorToBy= normalVectorToBy2-normalVectorToBy1
    cv2.line(img, (ax2, ay2), (ax2+vectorCx, ay2+vectorCy), (255, 255, 0), 5)
    magnitudeOfA = int(math.sqrt(math.pow(vectorAx, 2) + math.pow(vectorAy, 2))) #POP POP!!! #https://www.youtube.com/watch?v=dyp9Qw12boI&ab_channel=Jalkie
    magnitudeOfB = int(math.sqrt(math.pow(vectorBx, 2) + math.pow(vectorBy, 2)))
    #magnitudeOfnormalB = int(math.sqrt(math.pow(normalVectorToBx, 2) + math.pow(normalVectorToBy, 2)))
    #normOfnormalVectorToBx = normalVectorToBx/magnitudeOfnormalB
    #normOfnormalVectorToBy = normalVectorToBy/magnitudeOfnormalB

    #dotProductOfStuff = (ax2*normalVectorToBx)+(ay2*normalVectorToBy)

    #rLx = vectorAx-2*(dotProductOfStuff)*normOfnormalVectorToBx
    #rLy = vectorAy - 2 * (dotProductOfStuff) * normOfnormalVectorToBy



    vectorProduct = (vectorAx*vectorBx) + (vectorAy*vectorBy)
    magnitudeProduct = (magnitudeOfA * magnitudeOfB)



def angleDetermineBad(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, img):
    vectorAx = ax2 - ax1
    vectorAy = ay2 - ay1
    vectorBx = bx2 - bx1
    vectorBy = by2 - by1

    vectorA = [vectorAx, vectorAy]
    vectorB = [vectorBx, vectorBy]
    magnitudeOfA = int(math.sqrt(math.pow(vectorAx, 2) + math.pow(vectorAy, 2))) #POP POP!!! #https://www.youtube.com/watch?v=dyp9Qw12boI&ab_channel=Jalkie
    magnitudeOfB = int(math.sqrt(math.pow(vectorBx, 2) + math.pow(vectorBy, 2)))

    print(vectorAx, vectorAy, vectorBx, vectorBy, magnitudeOfA, magnitudeOfB)

    vectorProduct = (vectorAx*vectorBx) + (vectorAy*vectorBy)
    magnitudeProduct = (magnitudeOfA * magnitudeOfB)
    print(vectorProduct, magnitudeProduct)

    cosAngle = vectorProduct/magnitudeProduct
    print("cos",cosAngle)
    Angle = math.degrees(math.acos(cosAngle))
    print("A",Angle)

    print(vectorA, vectorB)
    cross = np.cross(vectorA, vectorB)
    print("cross", cross)

    x1 = ax2
    y1 = ay2
    rLx2 = x1 + (magnitudeOfA * math.cos(Angle))
    rLy2 = y1 + (magnitudeOfA * math.sin(Angle))
    print("rLx2", rLx2)
    print("rLy2", rLy2)

    print("final shit",ax2, ay2, rLx2, rLy2)
    cv2.line(img, (-vectorBy, vectorBx), (vectorBy, -vectorBx), (0, 255, 0), 5)
    cv2.line(img, (int(ax2), int(ay2)), (int(rLx2), int(rLy2)), (0, 255, 0), 5)
    #Laser.Laser
5