import Mirror
import Collision
import Laser
import Blocker
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

    testBlock = Mirror.Mirror(300, 100, 300, 300, 200, 300, 200, 100, img)
    testBlock1 = Mirror.Mirror(200, 350, 201, 900, 160, 900, 160, 350, img)
    testBlocker = Mirror.Mirror(500, 125, 500, 900, 400, 900, 400, 125, img)
    #testBlocker2 = Mirror.Mirror(150, 50, 150, 300, 100, 300, 100, 50, img)
    #testBlocker3 = Mirror.Mirror(720, 90, 680, 300, 625, 300, 600, 50, img)
    #testBlocker4 = Mirror.Mirror(900, 50, 860, 300, 800, 300, 800, 50, img)
    testBlocker2 = Blocker.Blocker(5, 5, 5, height-5, width-5, height-5, width-5, 5, img)

    mirrorBLockerList = [testBlock, testBlocker, testBlock1, testBlocker2]
    #laserList = []
    finalLaser = None
    finalPointList = []
    prevReflect = None
    currentReflect = None
    x2 = None
    y2 = None

    laserList = Laser.Laser(lsX, lsY, leX, leY, img)
    print("start while loop")
    while(True):
        prevReflect = currentReflect
        colBool = []
        blockBool = []
        tempLaser = None

        print("start for loops")
        for i in range(len(mirrorBLockerList)):
            colBool.append(True)
            blockBool.append(False)

        compareLaser = laserList
        for j in range(len(mirrorBLockerList)):
            col = Collision.Collision(mirrorBLockerList[j], compareLaser)
            tempLaser = col.collisionDetection(img)
            colBool[j] = col.reflected
            blockBool[j] = col.blocked

            if blockBool[j] is True:
                finalLaser = tempLaser

            if colBool[j] is True and j is not prevReflect:
                x = tempLaser.getX1()
                y = tempLaser.getY1()
                x2 = tempLaser.getX2()
                y2 = tempLaser.getY2()
                point = (x, y)
                finalPointList.append(point)
                laserList = tempLaser
                currentReflect = j

            print("j = " + str(j))
            print(colBool[j])


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
            point = (x2, y2)
            finalPointList.append(point)
            break


    #print('hey')
    # Draws the lasers from a list of points.
    for i in range(len(finalPointList)-1):
        if i is 1:
            color = (255, 0, 0)
            weight = 10
        else:
            color = (0, 0, 255)
            weight = 5
        #cv2.line(img, finalPointList[i], finalPointList[i+1], color, weight)

    # draws the lasers from a list of laser.
    finalLaser.drawLaser()
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
