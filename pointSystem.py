import cv2
import numpy as np

player1Point = 0
player2Point = 0

rectX1 = 490
rectY1 = 310
rectX2 = 640
rectY2 = 460

line1X1 = 0
line1Y1 = 231
line1X2 = 510
line1Y2 = 350

line2X1 = 642
line2Y1 = 231
line2X2 = 400
line2Y2 = 200

img = np.zeros((462, 642, 3), np.uint8)

rectangle = cv2.rectangle(img, (rectX1, rectY1), (rectX2, rectY2), (150, 150, 150), 4)
line1 = cv2.line(img, (line1X1, line1Y1), (line1X2, line1Y2), (255, 0, 0), 3)
line2 = cv2.line(img, (line2X1, line2Y1), (line2X2, line2Y2), (0, 0, 255), 3)

if all([line1X2 >= rectX1, line1X2 <= rectX2, line1Y2 >= rectY1, line1Y2 <= rectY2]):
    player1Point = player1Point + 1
    line1X2 = 321
    line1Y2 = 231
    line2X2 = 321
    line2Y2 = 231
    img = np.zeros((462, 642, 3), np.uint8)
    rectangle = cv2.rectangle(img, (rectX1, rectY1), (rectX2, rectY2), (150, 150, 150), 4)
    line1 = cv2.line(img, (line1X1, line1Y1), (line1X2, line1Y2), (255, 0, 0), 3)
    line2 = cv2.line(img, (line2X1, line2Y1), (line2X2, line2Y2), (0, 0, 255), 3)
if all([line2X2 >= rectX1, line2X2 <= rectX2, line2Y2 >= rectY1, line2Y2 <= rectY2]):
    player2Point = player2Point + 1
    line1X2 = 321
    line1Y2 = 231
    line2X2 = 321
    line2Y2 = 231
    img = np.zeros((462, 642, 3), np.uint8)
    rectangle = cv2.rectangle(img, (rectX1, rectY1), (rectX2, rectY2), (150, 150, 150), 4)
    line1 = cv2.line(img, (line1X1, line1Y1), (line1X2, line1Y2), (255, 0, 0), 3)
    line2 = cv2.line(img, (line2X1, line2Y1), (line2X2, line2Y2), (0, 0, 255), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, str(player1Point), (50, 100), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(img, str(player2Point), (550, 100), font, 2, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

