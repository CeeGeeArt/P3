import cv2


class Laser:

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    lineStart = (x1, y1)
    lineEnd = (x2, y2)

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.lineStart = (x1, y1)
        self.lineEnd = (x2, y2)

    def drawLaser(self, color, img):

        cv2.line(img, self.lineStart, self.lineEnd, color, 2)

    def getX1(self):
        return self.x1

    def getX2(self):
        return self.x2

    def getY1(self):
        return self.y1

    def getY2(self):
        return self.y2
