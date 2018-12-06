import Mirror
import Blocker
import Target
import Laser
import math
import cv2

class Collision:

    img2 = cv2.imread('testSmall.jpg')
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

    reflected = False
    blocked = False

    isMirror = 0
    topLCorner = (rectangleX1, rectangleY1)
    topRCorner = (rectangleX2, rectangleY1)
    bottomLCorner = (rectangleX1, rectangleY2)
    bottomRCorner = (rectangleX2, rectangleY2)

    def __init__(self, mirror, laser):
        #Mirror variable can be both a blocker and a mirror

        #The 2 coorinates are retrieved from the laser
        self.laserX1 = laser.getX1()
        self.laserX2 = laser.getX2()
        self.laserY1 = laser.getY1()
        self.laserY2 = laser.getY2()

        #The 4 coordinates are retrieved from the rectangle
        self.rectangleX1 = mirror.getRectangleX1()
        self.rectangleX2 = mirror.getRectangleX2()
        self.rectangleX3 = mirror.getRectangleX3()
        self.rectangleX4 = mirror.getRectangleX4()
        self.rectangleY1 = mirror.getRectangleY1()
        self.rectangleY2 = mirror.getRectangleY2()
        self.rectangleY3 = mirror.getRectangleY3()
        self.rectangleY4 = mirror.getRectangleY4()

        #Collision checks if the retrieved block is a blocker or a mirror
        self.isMirror = mirror.getMirrorState()

    def collisionLeft(self, img):

    #The different coordinates from the laser and rectangle is put into the right coordinates for the equation
    #The equation for calculateing where two lines intersect can be found here: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX1
        x4 = self.rectangleX2
        y3 = self.rectangleY1
        y4 = self.rectangleY2

        #The collision of the two lines is calculated here, both X and Y
        collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))


        #The math above will return collisions that are outside the laser and rectangle area
        #These if and else return only coordiantes that fall on the line, it also returns a one if they have collided
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionRight(self, img):
        #Same as the method above, but different coordinates
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX4
        x4 = self.rectangleX3
        y3 = self.rectangleY4
        y4 = self.rectangleY3
        collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))


        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionTop(self, img):
        # Same as the method above, but different coordinates
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX1
        x4 = self.rectangleX4
        y3 = self.rectangleY1
        y4 = self.rectangleY4
        collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))


        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def collisionBottom(self, img):
        # Same as the method above, but different coordinates
        x1 = self.laserX1
        x2 = self.laserX2
        y1 = self.laserY1
        y2 = self.laserY2
        x3 = self.rectangleX2
        x4 = self.rectangleX3
        y3 = self.rectangleY2
        y4 = self.rectangleY3
        collisionX = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

        collisionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))


        if collisionY >= y3 and collisionY <= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY >= y3 and collisionY <= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x3 and collisionX >= x4:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        if collisionY <= y3 and collisionY >= y4 and collisionX <= x4 and collisionX >= x3:
            cv2.line(img, (int(collisionX), int(collisionY)), (int(collisionX), int(collisionY)),
                     (255, 0, 0), 5)
            return int(collisionX), int(collisionY), 1
        else:
            return 100000, 100000, 0

    def findSmallDistance(self, laserX1, laserY1, collisionX1, collisionY1, collisionX2, collisionY2):
        #Checks what collision is the one closest to the origin of the laser, this is the point it should collide with.
        distanceToPoint1 = math.sqrt((((laserX1) - (collisionX1)) ** 2) + (((laserY1) - (collisionY1)) ** 2))
        distanceToPoint2 = math.sqrt((((laserX1) - (collisionX2)) ** 2) + (((laserY1) - (collisionY2)) ** 2))

        #Here the program returnes the smallest of the two distances found above.
        if distanceToPoint1 > distanceToPoint2 and self.isMirror != 0:
            return collisionX2, collisionY2
        if distanceToPoint1 < distanceToPoint2 and self.isMirror != 0:
            return collisionX1, collisionY1
        elif distanceToPoint1 > distanceToPoint2:
            return collisionX2, collisionY2
        else:
            return collisionX1, collisionY1

    def findBiggestDistance(self, laserX1, laserY1, collisionX1, collisionY1, collisionX2, collisionY2):
        #Same method as above,but returnes the biggest value
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

        #gets the collision point on all the sides of the cube, and the collisionState, to check if it has even collided
        topCollisionX, topCollisionY, topCollisionState = self.collisionTop(img)
        bottomCollisionX, bottomCollisionY, bottomCollisionState = self.collisionBottom(img)
        rightCollisionX, rightCollisionY, rightCollisionState = self.collisionRight(img)
        leftCollisionX, leftCollisionY, leftCollisionState = self.collisionLeft(img)

        #Variables to store the points that acctually collides on the squares
        collisionX1 = 0
        collisionY1 = 0
        collisionX2 = 0
        collisionY2 = 0

        #Checks what sides the colission happens on, and returnes the collision coordiates
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


        #After the right collision points have been found, the point closest to the laser origin is found.
        closestCollisionX, closestCollisionY = self.findSmallDistance(laserX1, laserY1, collisionX1, collisionY1,
                                                                      collisionX2, collisionY2)

        #We check if the collision point is not bugged and in the corner of the screen.
        #We also check if the rectangle, the laser hits is a mirror.
        if 0< closestCollisionX and 0<closestCollisionY and self.isMirror != 0:
            collisionLineX1 = 0
            collisionLineY1 = 0
            collisionLineX2 = 0
            collisionLineY2 = 0
            #We check what sides the collision happens on, and get the x and y of the line, so we can pass it to the
            # reflection function
            # if closestCollisionX == topCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX1, self.rectangleY1
            #     collisionLineX2, collisionLineY2 = self.rectangleX4, self.rectangleY4
            # elif closestCollisionX == bottomCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX3, self.rectangleY3
            #     collisionLineX2, collisionLineY2 = self.rectangleX2, self.rectangleY2
            # elif closestCollisionX == rightCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX4, self.rectangleY4
            #     collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            # elif closestCollisionX == leftCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX2, self.rectangleY2
            #     collisionLineX2, collisionLineY2 = self.rectangleX1, self.rectangleY1
            #
            # ----------- Works better than above but still has problems
            # if closestCollisionX == topCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX4, self.rectangleY4
            #     collisionLineX2, collisionLineY2 = self.rectangleX1, self.rectangleY1
            # elif closestCollisionX == bottomCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX2, self.rectangleY2
            #     collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            # elif closestCollisionX == rightCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX4, self.rectangleY4
            #     collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            # elif closestCollisionX == leftCollisionX:
            #     collisionLineX1, collisionLineY1 = self.rectangleX2, self.rectangleY2
            #     collisionLineX2, collisionLineY2 = self.rectangleX1, self.rectangleY1
            #
            if closestCollisionX == topCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX4, self.rectangleY4
                collisionLineX2, collisionLineY2 = self.rectangleX1, self.rectangleY1
            elif closestCollisionX == bottomCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX2, self.rectangleY2
                collisionLineX2, collisionLineY2 = self.rectangleX3, self.rectangleY3
            elif closestCollisionX == rightCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX3, self.rectangleY3
                collisionLineX2, collisionLineY2 = self.rectangleX4, self.rectangleY4
            elif closestCollisionX == leftCollisionX:
                collisionLineX1, collisionLineY1 = self.rectangleX1, self.rectangleY1
                collisionLineX2, collisionLineY2 = self.rectangleX2, self.rectangleY2

            self.reflected = True
            self.blocked = False

            # print('Col info')
            # print(self.laserX1, closestCollisionX)

            #The right coordinates are put into the reflection function
            return Mirror.angleDetermine(self.laserX1, self.laserY1, self.laserX2, self.laserY2, closestCollisionX,
                                         closestCollisionY, collisionLineX1, collisionLineY1, collisionLineX2,
                                         collisionLineY2, img)
        elif 0 < closestCollisionX and 0 < closestCollisionY:
            #If the block is a blocker it will stop the laser at the collision point
            # print('Block')
            self.reflected = False
            self.blocked = True

            # print('Col info')
            # print(self.laserX1, closestCollisionX)
            # print(self.laserY1, closestCollisionY)

            return Laser.Laser(self.laserX1, self.laserY1, closestCollisionX, closestCollisionY)
        else:

            #If the laser does not collide with any blocker or Mirror it will return the laser again, this laser is
            # then made longer
            # print("screenCollision")
            self.reflected = False
            self.blocked = False
            return Laser.Laser(self.laserX1, self.laserY1, self.laserX2, self.laserY2)


        #     #if the laser does not hit, it colides with the screen
        #     height, width, channels = img.shape
        #     screen = Blocker.Blocker(0, 0, 0, height, width, height, width, 0, img)
        #     newLaserX2, newLaserY2 = (self.laserX2+width/2)+2, (self.laserY2+height/2)+2
        #     tempLaser = Laser.Laser(self.laserX1, self.laserY1, newLaserX2, newLaserY2)
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
        #     return Laser.Laser(laserX1, laserY1, screenCollisionX, screenCollisionY)
