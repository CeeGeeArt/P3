import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img,(0, 0), (511, 511), (255, 0, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)