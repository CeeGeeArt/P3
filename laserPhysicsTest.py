import numpy as np
import cv2
import time

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 100
    lsY = int(vRow/2)
    leX = int(vCol-50)
    leY = int(vRow/2)+200
    osX = int(vCol/2)
    osY = int(vRow/2)-100
    oeX = vCol-100
    oeY = int(vRow/2)+100
    drawObj = cv2.rectangle(videoFeed, (osX,osY), (oeX, oeY), (0, 255, 0), 2)
    if osX<leX or osY<leY or oeY>leY:
        leX = osX
        leY = oeY
        drawLaser = cv2.line(videoFeed, (lsX, lsY), (leX, leY), (0, 0, 255, 127), 5)
    else:
        drawLaser = cv2.line(videoFeed, (lsX, lsY), (leX, leY), (0, 0, 255, 127), 5)


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

    if cv2.waitKey(33) >= 0:
        break

    last_frame = frame

cap.release()
cv2.destroyAllWindows()