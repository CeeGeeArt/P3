import Mirror
import Blocker
import Target
import Laser
import math
import cv2

class Collision:

    img2 = cv2.imread('test.jpg')
    laserX1 = 0
    laserX2 = 0
    laserY1 = 0
    laserY2 = 0

    rectangleX1 = 0
    rectangleX2 = 0
    rectangleX3 = 0
    rectangleX4 = 0

    rectangleY1 = 0
    rectangleY2 = 0
    rectangleY3 = 0
    rectangleY4 = 0

    reflected = True
    blocked = False

    isMirror = 0
    topLCorner = (rectangleX1, rectangleY1)
    topRCorner = (rectangleX2, rectangleY1)
    bottomLCorner = (rectangleX1, rectangleY2)
    bottomRCorner = (rectangleX2, rectangleY2)

    def __init__(self, mirror, laser):
        self.laserX1 = laser.getX1()
        self.laserX2 = laser.getX2()
        self.laserY1 = laser.getY1()
        self.laserY2 = laser.getY2()
        self.rectangleX1 = mirror.getRectangleX1()
        self.rectangleX2 = mirror.getRectangleX2()
        self.rectangleX3 = mirror.getRectangleX3()
        self.rectangleX4 = mirror.getRectangleX4()
        self.rectangleY1 = mirror.getRectangleY1()
        self.rectangleY2 = mirror.getRectangleY2()
        self.rectangleY3 = mirror.getRectangleY3()
        self.rectangleY4 = mirror.getRectangleY4()
        self.isMirror = mirror.getMirrorState()
        self.laser = laser

    def getLaser(self):
        return self.Laser

    def collisionLeft(self, img):
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX1
        x4 = self.rectangleX2
        y3 = self.rectangleY1
        y4 = self.rectangleY2

        collisionX = 0
        collisionY = 0

        try:
            collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                            / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

            collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                            / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
        except:
            cv2.putText(img, "Please move one of the blocks", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            print("Error in col left")

        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionRight(self, img):
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX4
        x4 = self.rectangleX3
        y3 = self.rectangleY4
        y4 = self.rectangleY3
        collisionX = 0
        collisionY = 0

        try:
            collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

            collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
        except:
            cv2.putText(img, "Please move one of the blocks", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            print("Error in col right")

        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionTop(self, img):
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX1
        x4 = self.rectangleX4
        y3 = self.rectangleY1
        y4 = self.rectangleY4
        collisionX = 0
        collisionY = 0

        try:
            collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

            collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
        except:
            cv2.putText(img, "Please move one of the blocks", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            print("Error in col top")

        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionBottom(self, img):
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX2
        x4 = self.rectangleX3
        y3 = self.rectangleY2
        y4 = self.rectangleY3
        collisionX = 0
        collisionY = 0

        try:
            collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

            collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                         / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
        except:
            cv2.putText(img, "Please move one of the blocks", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            print("Error in col bottom")

        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def findSmallDistance(self, laserX1, laserY1, collisionX1, collisionY1, collisionX2, collisionY2):
        distanceToPoint1 = math.sqrt((((laserX1) - (collisionX1)) ** 2) + (((laserY1) - (collisionY1)) ** 2))
        distanceToPoint2 = math.sqrt((((laserX1) - (collisionX2)) ** 2) + (((laserY1) - (collisionY2)) ** 2))

        if distanceToPoint1 > distanceToPoint2 and self.isMirror != 0:
            return collisionX2, collisionY2
        if distanceToPoint1 < distanceToPoint2 and self.isMirror != 0:
            return collisionX1, collisionY1
        elif distanceToPoint1 > distanceToPoint2:
            return collisionX2, collisionY2
        else:
            return collisionX1, collisionY1

    def findBiggestDistance(self, laserX1, laserY1, collisionX1, collisionY1, collisionX2, collisionY2):
        distanceToPoint1 = math.sqrt((((laserX1) - (collisionX1)) ** 2) + (((laserY1) - (collisionY1)) ** 2))
        distanceToPoint2 = math.sqrt((((laserX1) - (collisionX2)) ** 2) + (((laserY1) - (collisionY2)) ** 2))

        if distanceToPoint1 > distanceToPoint2:
            return collisionX1, collisionY1
        else:
            return collisionX2, collisionY2


    def collisionDetection(self, img):
        laserX1 = self.laserX1
        laserX2 = self.laserX2
        laserY1 = self.laserY1
        laserY2 = self.laserY2

        #gets the collision point on all the sides of the cube
        topCollisionX, topCollisionY, topCollisionState = self.collisionTop(img)
        bottomCollisionX, bottomCollisionY, bottomCollisionState = self.collisionBottom(img)
        rightCollisionX, rightCollisionY, rightCollisionState = self.collisionRight(img)
        leftCollisionX, leftCollisionY, leftCollisionState = self.collisionLeft(img)

        collisionX1 = 0
        collisionY1 = 0
        collisionX2 = 0
        collisionY2 = 0

        #Checks what sides the colission happens on
        if topCollisionState == 1:
            collisionX1 = topCollisionX
            collisionY1 = topCollisionY
            if bottomCollisionState == 1:
                collisionX2 = bottomCollisionX
                collisionY2 = bottomCollisionY
            elif rightCollisionState == 1:
                collisionX2 = rightCollisionX
                collisionY2 = rightCollisionY
            elif leftCollisionState == 1:
                collisionX2 = leftCollisionX
                collisionY2 = leftCollisionY
        elif bottomCollisionState == 1:
            collisionX1 = bottomCollisionX
            collisionY1 = bottomCollisionY
            if rightCollisionState == 1:
                collisionX2 = rightCollisionX
                collisionY2 = rightCollisionY
            elif leftCollisionState == 1:
                collisionX2 = leftCollisionX
                collisionY2 = leftCollisionY
        elif rightCollisionState == 1:
            collisionX1 = rightCollisionX
            collisionY1 = rightCollisionY
            if leftCollisionState == 1:
                collisionX2 = leftCollisionX
                collisionY2 = leftCollisionY
        elif leftCollisionState == 1:
            collisionX1 = leftCollisionX
            collisionY1 = leftCollisionY

        closestCollisionX, closestCollisionY = self.findSmallDistance(laserX1, laserY1, collisionX1, collisionY1,
                                                                      collisionX2, collisionY2)

        if 0< closestCollisionX and 0<closestCollisionY and self.isMirror !=0:
            collisionLineX1 = 0
            collisionLineY1 = 0
            collisionLineX2 = 0
            collisionLineY2 = 0
            #We check what sides the collision happens on, and get the x and y of the line
            #closestCollisionX, closestCollisionY = self.findSmallDistance(laserX1, laserY1, collisionX1, collisionY1, collisionX2, collisionY2)
            #print("x n shit", closestCollisionX, topCollisionX, bottomCollisionX, rightCollisionX, leftCollisionX)
            if closestCollisionX == topCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX1, self.rectangleY1
                collisionLineX2, collisionLineY2 = self.rectangleX4, self.rectangleY4
            elif closestCollisionX == bottomCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX2, self.rectangleY2
                collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            elif closestCollisionX == rightCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX4, self.rectangleY4
                collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            elif closestCollisionX == leftCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX1, self.rectangleY1
                collisionLineX2, collisionLineY2 = self.rectangleX2, self.rectangleY2

            #print("bex shit",collisionLineX1,collisionLineY1,collisionLineX2,collisionLineY2)
            self.blocked = False

            return Mirror.angleDetermine(self.laserX1, self.laserY1, self.laserX2, self.laserY2, closestCollisionX,
                                         closestCollisionY, collisionLineX1, collisionLineY1, collisionLineX2,
                                         collisionLineY2, img)
        elif 0 < closestCollisionX and 0 < closestCollisionY:
            #print('Block')
            self.reflected = False
            self.blocked = True

            #print('self ' +str(self.reflected))
            #print(Collision.reflected)
            return Laser.Laser(self.laserX1, self.laserY1, closestCollisionX, closestCollisionY, img)
        # else:
        #     #if the laser does not hit, it colides with the screen
        #     height, width, channels = img.shape
        #     screen = Blocker.Blocker(0, 0, 0, height, width, height, width, 0, img)
        #     newLaserX2, newLaserY2 = (self.laserX2+width/2)+2, (self.laserY2+height/2)+2
        #     tempLaser = Laser.Laser(self.laserX1, self.laserY1, newLaserX2, newLaserY2, img)
        #     screenCollision = Collision(screen, tempLaser)
        #     topScreenCollisionX, topScreenCollisionY, topScreenCollisionState = screenCollision.collisionTop(img)
        #     bottomScreenCollisionX, bottomScreenCollisionY, bottomScreenCollisionState = screenCollision.collisionBottom(img)
        #     rightScreenCollisionX, rightScreenCollisionY, rightScreenCollisionState = screenCollision.collisionRight(img)
        #     leftScreenCollisionX, leftScreenCollisionY, leftScreenCollisionState = screenCollision.collisionLeft(img)
        #
        #     collisionWithScreenX1 = 0
        #     collisionWithScreenY1 = 0
        #     collisionWithScreenX2 = 0
        #     collisionWithScreenY2 = 0
        #
        #     if topCollisionState == 1:
        #         collisionWithScreenX1 = topCollisionX
        #         collisionWithScreenY1 = topCollisionY
        #         if bottomCollisionState == 1:
        #             collisionWithScreenX2 = bottomCollisionX
        #             collisionWithScreenY2 = bottomCollisionY
        #         elif rightCollisionState == 1:
        #             collisionWithScreenX2 = rightCollisionX
        #             collisionWithScreenY2 = rightCollisionY
        #         elif leftCollisionState == 1:
        #             collisionWithScreenX2 = leftCollisionX
        #             collisionWithScreenY2 = leftCollisionY
        #     elif bottomCollisionState == 1:
        #         collisionWithScreenX1 = bottomCollisionX
        #         collisionWithScreenY1 = bottomCollisionY
        #         if rightCollisionState == 1:
        #             collisionWithScreenX2 = rightCollisionX
        #             collisionWithScreenY2 = rightCollisionY
        #         elif leftCollisionState == 1:
        #             collisionWithScreenX2 = leftCollisionX
        #             collisionWithScreenY2 = leftCollisionY
        #     elif rightCollisionState == 1:
        #         collisionWithScreenX1 = rightCollisionX
        #         collisionWithScreenY1 = rightCollisionY
        #         if leftCollisionState == 1:
        #             collisionWithScreenX2 = leftCollisionX
        #             collisionWithScreenY2 = leftCollisionY
        #     elif leftCollisionState == 1:
        #         collisionWithScreenX1 = leftCollisionX
        #         collisionWithScreenY1 = leftCollisionY
        #     screenCollisionX, screenCollisionY = self.findSmallDistance(newLaserX2, newLaserY2, collisionWithScreenX1, collisionWithScreenY1,
        #                                     collisionWithScreenX2, collisionWithScreenY2)
        #     self.reflected = False
        #     return Laser.Laser(laserX1, laserY1, screenCollisionX, screenCollisionY, img)
