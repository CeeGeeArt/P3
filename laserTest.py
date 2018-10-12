import numpy as np
import cv2
import time

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    laserVerPos = vRow / 2
    laserVerPos = int(laserVerPos)
    laserPosDiv = vCol / totLaserPos
    laserPosDiv = int(laserPosDiv)
    laserPos = [0]
    for i in range(totLaserPos - 1):
        laserPos.append(laserPosDiv * (i + 1))
    laserTime = [0.0]
    for t in range(totLaserPos - 1):
        laserTime.append(timePerPos * (t + 1))

    #Here is the attempted loop for the laser
    for i in range(totLaserPos):
        for x in range(100):
            if time.clock() >= laserTime[i] + timePerPos:
                break
            elif time.clock() >= laserTime[i]:
                drawLaser = cv2.line(videoFeed, (laserPos[i], laserVerPos), \
                    (laserPos[i] + 40, laserVerPos), (0,0,255), 5)

cap = cv2.VideoCapture(0)

ret, last_frame = cap.read()

if last_frame is None:
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()

    if frame is None:
        exit()

    laserFire(frame,8,0.2) #Call to laser function
    cv2.imshow('frame', frame)

    if cv2.waitKey(33) >= 0:
        break

    last_frame = frame

cap.release()
cv2.destroyAllWindows()