import Mirror
import Collision
import Laser
import Blocker
import cv2

img = cv2.imread('test.jpg')
height, width, channels = img.shape

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
    x1 = 600
    x2 = leX
    x3 = x1
    x4 = x2
    y1 = 450
    y2 = leY
    y3 = y1 - 150
    y4 = y2- 150

    screenBoarderCollision = Blocker.Blocker(0, 0, width, height, img)
    testBlocker = Mirror.Mirror(400, 400, 500, 500, img)

    originalLaser = Laser.Laser(lsX, lsY, leX, leY, img)

    col = Collision.Collision(testBlocker, originalLaser)

    col.collisionDetection(img)

    leX , leY = col.collisionDetection(img)

    print("original", leX, leY)

    outPutLaser = Laser.Laser(lsX, lsY, leX, leY, img)
    outPutLaser.drawLaser()




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
