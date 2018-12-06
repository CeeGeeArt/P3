import Laser
import cv2
import math


class Mirror:

    rectangleX1 = 0
    rectangleX2 = 0
    rectangleX3 = 0
    rectangleX4 = 0

    rectangleY1 = 0
    rectangleY2 = 0
    rectangleY3 = 0
    rectangleY4 = 0

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

        self.mirrorState = 1
        topLCorner = (x1, y1)
        topRCorner = (x4, y4)
        bottomLCorner = (x2, y2)
        bottomRCorner = (x3, y3)

        cv2.line(img, topLCorner, bottomLCorner, (255, 255, 255), 5)
        cv2.line(img, topRCorner, bottomRCorner, (255, 255, 255), 5)
        cv2.line(img, topLCorner, topRCorner, (255, 255, 255), 5)
        cv2.line(img, bottomLCorner, bottomRCorner, (255, 255, 255), 5)



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


def angleDetermine(laserX1, laserY1, laserX2, laserY2, closestCollisionX, closestCollisionY, collisionLineX1,
                   collisionLineY1, collisionLineX2, collisionLineY2, img):

    #The normal for the rectangles line is calulated here
    normalY = collisionLineX2 - collisionLineX1
    normalX = collisionLineY1 - collisionLineY2
    temp = ((collisionLineX2 - collisionLineX1) ** 2) + ((collisionLineY2 - collisionLineY1) ** 2)
    normalLength = math.sqrt(temp)
    normalX = normalX / normalLength
    normalY = normalY / normalLength

    #If the vector is too short, so it can not be properly reflected it will be made longer here
    if laserX2 < collisionLineX1 or laserY1 < collisionLineY1:
        laserVectorX = laserX2-laserX1
        laserVectorY = laserY2-laserY1

        laserX2 = laserVectorX + closestCollisionX
        laserY2 = laserVectorY + closestCollisionY
    else:
        laserX2 = laserX2
        laserY2 = laserY2

    #The vector that goes byound the rectangle side, is found, so it can be reflected in the normal from above.
    rayX = laserX2 - closestCollisionX
    rayY = laserY2 - closestCollisionY

    #The normal is moved to the end of the laser that goes into the rectangle
    dotProduct = (rayX * normalX)+(rayY*normalY)
    dotNormalX = dotProduct*normalX
    dotNormalY = dotProduct*normalY

    #The end of the reflection is found
    reflectionEndX = laserX2 - (dotNormalX * 2)
    reflectionEndY = laserY2 - (dotNormalY * 2)
    #cv2.line(img, (laserX1,laserY1), (closestCollisionX, closestCollisionY), (0, 0, 255), 5)
    return Laser.Laser(closestCollisionX, closestCollisionY, int(reflectionEndX), int(reflectionEndY))

