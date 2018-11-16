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
    #testBlock1 = Mirror.Mirror(200,400,300,400,300,800,200,800 , img)
    testBlocker = Mirror.Mirror(500, 150, 500, 350, 400, 350, 400, 150, img)

    mirrorBLockerList = [testBlock,testBlocker]
    #laserList = []
    finalLaserList = []

    laserList = Laser.Laser(lsX, lsY, leX, leY, img)
    print("start while loop")
    while(True):
        colBool = []
        print("start for loops")
        for i in range(len(mirrorBLockerList)):
            colBool.append(True)
        #for i in range(len(laserList)):
        for j in range(len(mirrorBLockerList)):
            col = Collision.Collision(mirrorBLockerList[j], laserList)
            #print('før' + str(Collision.Collision.reflected))
            tempLaser = col.collisionDetection(img)
            #print('efter' + str(col.reflected))
            colBool[j] = col.reflected
            if colBool[j] is True:
                finalLaserList.append(tempLaser)
                laserList = tempLaser

            #print("i = " + str(i))
            print("j = " + str(j))
            print(colBool[j])

        #print(len(laserList))
        if colBool[1] is True:
            break


    #print('hey')
    for i in range(len(finalLaserList)):
        finalLaserList[i].drawLaser()



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
