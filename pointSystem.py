import cv2
import numpy as np

player1Point = 0
player2Point = 0

rectX1 = 490
rectY1 = 310
rectX2 = 640
rectY2 = 460
img = np.zeros((462, 642, 3), np.uint8)

rectangle = cv2.rectangle(img, (rectX1, rectY1), (rectX2, rectY2), (150, 150, 150), 4)
line1 = cv2.line(img, (0, 350), (510, 350), (255, 0, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

