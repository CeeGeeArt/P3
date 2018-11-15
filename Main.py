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
    lsX = 0
    lsY = 0
    leX = 100
    leY = 200

    #testMirror = Mirror.Mirror(300, 1000, 900, 1100, img)
    #testBlocker = Mirror.Mirror(1000, 400, 1100, 500, img)
    #originalLaser = Laser.Laser(leX, leY, lsX, lsY, img)
    #col = Collision.Collision(testMirror, originalLaser)
    #outPutLaser = col.collisionDetection(img)
    #outPutLaser.drawLaser()

    #col2 = Collision.Collision(testBlocker, outPutLaser)
    #reflectedLaser = col2.collisionDetection(img)
    #reflectedLaser.drawLaser()
    #col3 = Collision.Collision(testMirror, reflectedLaser)
    #reflectedLaser2 = col3.collisionDetection(img)
    #col4 = Collision.Collision(testBlocker, reflectedLaser2)
    #reflectedLaser3 = col4.collisionDetection(img)
    #reflectedLaser3.drawLaser()


    testMirror = Mirror.Mirror(300, 400, 900, 1100, img)
    #testMirror2 = Mirror.Mirror(100, 600, 200, 900, img)
    #testBlocker = Mirror.Mirror(1000, 400, 1100, 500, img)

    originalLaser = Laser.Laser(lsX, lsY, leX, leY, img)

    col = Collision.Collision(testMirror, originalLaser)

    outPutLaser = col.collisionDetection(img)
    #
    outPutLaser.drawLaser()

#     laserArray = []
#     colidedLasers = []
#     blockerMirrorArray = [testMirror2, testMirror]
#     laserArray = [Laser.Laser(lsX, lsY, leX, leY, img)]
#     laserCollisionState = 1
#     collidedLasers = []
#
#
#     for i in range(len(laserArray)):
#         for j in range(len(blockerMirrorArray)):
#             col = Collision.Collision(blockerMirrorArray[j], laserArray[i])
#             tempLaser, collissionState = col.collisionDetection(img)
#             if collissionState == 1:
#                 laserArray.append(tempLaser)
#                 colidedLasers.append(tempLaser)
#
#     # if prevArrayLength<len(laserArray):
#     #     for i in range(1):
#     #         for j in range(len(blockerMirrorArray)):
#     #             col = Collision.Collision(blockerMirrorArray[1], laserArray[i])
#     #             tempLaser, collissionState = col.collisionDetection(img)
#     #             if collissionState == 1:
#     #                 laserArray.append(tempLaser)
#     #                 colidedLasers.append(tempLaser)
#     #                 print(len(laserArray))
#     # for i in range(len(colidedLasers)):
#     #     colidedLasers[i].drawLaser()
#
#     # for laser in laserArray:
#     #     for Blocker in blockerMirrorArray:
#     #         col = Collision.Collision(Blocker, laser)
#     #         tempLaser, colState = col.collisionDetection(img)
#     #         laserArray.append(tempLaser)
#     #         if colState == 1:
#     #             colidedLasers.append(tempLaser)
#     #
#     # for laser in colidedLasers:
#     #     laser.drawLaser()
#
#     # laserArray = []
#     # colidedLasers = []
#     # blockerMirrorArray = [testMirror2, testMirror]
#     # laserArray = [Laser.Laser(lsX, lsY, leX, leY, img)]
#     # laserCollisionState = 1
#     #
#     # while(laserCollisionState == 1):
#     #     for i in range(len(laserArray)):
#     #         for j in range(len(blockerMirrorArray)):
#     #             col = Collision.Collision(blockerMirrorArray[1], laserArray[i])
#     #             tempLaser, laserCollisionState = col.collisionDetection(img)
#     #             if laserCollisionState == 1:
#     #                 laserArray.append(tempLaser)
#     #                 colidedLasers.append(tempLaser)
#
#
#     originalLaser = Laser.Laser(0,0,200,200,img)
#     blockerMirrorArray = [testMirror2, testMirror]
#     laserQueue = Queue.Queue()
#     laserQueue.put(originalLaser)
#     collidedLasers = []
#
#
#     while not laserQueue.empty():
#         laser = laserQueue.get(False)
#         for blocker in blockerMirrorArray:
#             col = Collision.Collision(blockerMirrorArray[1], laser)
#             tempLaser, collissionState = col.collisionDetection(img)
#             if collissionState == 1:
#                 laserQueue.put(tempLaser)
#                 collidedLasers.append(tempLaser)
#
# # for i in range(1):
# #     for j in range(len(blockerMirrorArray)):
# #         col = Collision.Collision(blockerMirrorArray[1], laserArray[i])
# #         tempLaser, collissionState = col.collisionDetection(img)
# #         if collissionState == 1:
# #             laserArray.append(tempLaser)
# #             colidedLasers.append(tempLaser)

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
