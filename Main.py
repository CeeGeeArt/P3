import Mirror
import Collision
import Laser
import Blocker
import math
import cv2
#import Queue


img = cv2.imread('test.jpg')
height, width, channels = img.shape

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 500
    lsY = 0
    leX = 0
    leY = vRow

    testBlock = Mirror.Mirror(299, 100, 299, 290, 200, 290, 200, 100, img)
    testBlocker = Mirror.Mirror(499, 125, 499, 900, 400, 900, 400, 125, img)
    testBlock1 = Mirror.Mirror(199, 350, 199, 900, 180, 900, 180, 350, img)
    print(testBlock.getMirrorState(), testBlocker.getMirrorState(), testBlock1.getMirrorState())

    testBlock2 = Mirror.Mirror(151, 450, 150, 900, 130, 900, 130, 450, img)
    testBlock3 = Mirror.Mirror(240, 500, 242, 900, 300, 900, 300, 500, img)

    #testBlocker2 = Mirror.Mirror(150, 50, 150, 300, 100, 300, 100, 50, img)
    #testBlocker3 = Mirror.Mirror(720, 90, 680, 300, 625, 300, 600, 50, img)
    #testBlocker4 = Mirror.Mirror(900, 50, 860, 300, 800, 300, 800, 50, img)
    #testBlocker2 = Blocker.Blocker(5, 5, 5, height-5, width-5, height-5, width-5, 5, img)

    mirrorBLockerList = [testBlock, testBlocker, testBlock1]
    finalLaser = None
    finalPointList = [(lsX, lsY)]
    prevReflect = None
    newReflect = None
    x3 = None
    y3 = None

    current_laser = Laser.Laser(lsX, lsY, leX, leY, img)
    print("start while loop")
    while True:
        currentReflect = []
        prevReflect = newReflect
        colBool = []
        tempLaser = None
        reflectArray = []
        reflectArray2 = []

        print("start for loops")
        for i in range(len(mirrorBLockerList)):
            colBool.append(True)

        compareLaser = current_laser
        print(compareLaser.getX1(), compareLaser.getY1(), compareLaser.getX2(), compareLaser.getY2())
        for j in range(len(mirrorBLockerList)):
            col = Collision.Collision(mirrorBLockerList[j], compareLaser)
            tempLaser = col.collisionDetection(img)
            colBool[j] = col.reflected

            if colBool[j] is True and j is not prevReflect:
                x = tempLaser.getX1()
                y = tempLaser.getY1()
                point = (x, y)
                reflectArray.append(point)
                end_x = tempLaser.getX2()
                end_y = tempLaser.getY2()
                end_point = (end_x, end_y)
                reflectArray2.append(end_point)

                # Calculate the final laserPoint
                x2 = tempLaser.getX2()
                y2 = tempLaser.getY2()
                lenAB = math.sqrt(pow(x - x2, 2.0) + pow(y - y2, 2.0))
                x3 = int(x2 + (x2 - x) / lenAB * 10000)
                y3 = int(y2 + (y2 - y) / lenAB * 10000)

                current_laser = tempLaser
                currentReflect.append(j)

            #print("j = " + str(j))
            print(colBool[j])

        print("reflectArray: " + str(reflectArray))
        # Check which laser is the shortest
        print("start compare loop")
        startX, startY = finalPointList[len(finalPointList) - 1]
        compare = None
        ekstra_compare = None
        if len(reflectArray) > 1:
            print("BBC")
            for i in range(len(reflectArray)-1):
                x, y = reflectArray[i]
                x2, y2 = reflectArray[i+1]
                distanceToPoint1 = math.sqrt((((startX) - (x)) ** 2) + (((startY) - (y)) ** 2))
                distanceToPoint2 = math.sqrt((((startX) - (x2)) ** 2) + (((startY) - (y2)) ** 2))
                if distanceToPoint1 < distanceToPoint2:
                    compare = reflectArray[i]
                    ekstra_compare = reflectArray2[i]
                    newReflect = currentReflect[i]
                else:
                    compare = reflectArray[i+1]
                    ekstra_compare = reflectArray2[i+1]
                    newReflect = currentReflect[i+1]
            finalPointList.append(compare)
            x, y = compare
            x2, y2 = ekstra_compare
            current_laser = Laser.Laser(x, y, x2, y2, img)

        elif len(reflectArray) > 0:
            print("BBB")
            finalPointList.append(reflectArray[0])
            newReflect = currentReflect[0]
            x, y = reflectArray[0]
            x2, y2 = reflectArray2[0]
            current_laser = Laser.Laser(x, y, x2, y2, img)

        else:
            print("No reflections")

        # Manages the break statement
        breaking = False
        for i in range(len(mirrorBLockerList)):
            if i is not prevReflect:
                if colBool[i] is True:
                    breaking = False
                    break
                else:
                    breaking = True
        if breaking is True:
            point = (x3, y3)
            finalPointList.append(point)
            break


    #print('hey')
    # Draws the lasers from a list of points.
    for i in range(len(finalPointList)-1):
        if i is 3:
            color = (255, 0, 0)
            weight = 10
        else:
            color = (0, 255, 0)
            weight = 5
        cv2.line(img, finalPointList[i], finalPointList[i+1], color, weight)

    # draws the lasers from a list of laser.
    #finalLaser.drawLaser()
    #for i in range(len(finalLaserList)):
     #   finalLaserList[i].drawLaser()



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

# tempVectorX = tempLaser.getX2 - tempLaser.getX1
#
# tempVectorY = tempLaser.getY2 - tempLaser.getY1
#
# if tempVectorX > 0 and tempVectorY > 0:
#     #do stuff to but right laser
# elif tempVectorX < 0 and tempVectorY < 0:
#     #do some other stuff
# elif tempVectorX < 0 and tempVectorY > 0:
#     #do stuff
# elif tempVectorX > 0 and tempVectorY < 0:
#     #last stuff to do
# else:
#     #Do other stuff just incase
