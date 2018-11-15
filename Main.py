import Mirror
import Collision
import Laser
import Blocker
import cv2
import Queue


img = cv2.imread('test.jpg')
height, width, channels = img.shape

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 500
    lsY = 0
    leX = 0
    leY = vRow

    testBlock = Blocker.Blocker(300, 100, 300, 300, 200, 300, 200, 100, img)
    testBlocker = Blocker.Blocker(500, 150, 500, 350, 400, 350, 400, 150, img)

    mirrorBLockerList = [testBlock, testBlocker]
    laserList = []
    finalLaserList = []

    laserList.append(Laser.Laser(lsX, lsY, leX, leY, img))
    print(Collision.Collision.reflected)
    while(True):
        colBool = True
        #print(len(laserList))
        for i in range(len(laserList)):
            for j in range(len(mirrorBLockerList)):

                col = Collision.Collision(mirrorBLockerList[j], laserList[i])
                print('før' + str(Collision.Collision.reflected))
                tempLaser = col.collisionDetection(img)
                print('efter' + str(col.reflected))
                finalLaserList.append(tempLaser)
                colBool = col.reflected
        if colBool is False:
            break


    print('hey')
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
