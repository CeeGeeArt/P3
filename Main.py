import Mirror
import Collision
import Laser
import Blocker
import cv2


img = cv2.imread('test.jpg')
height, width, channels = img.shape

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 0
    lsY = 0
    leX = 100
    leY = 200

    testMirror = Mirror.Mirror(300, 400, 900, 1100, img)
    #testBlocker = Mirror.Mirror(1000, 400, 1100, 500, img)

    originalLaser = Laser.Laser(lsX, lsY, leX, leY, img)

    col = Collision.Collision(testMirror, originalLaser)

    outPutLaser = col.collisionDetection(img)

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
