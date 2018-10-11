import numpy as np
import cv2


img = np.zeros((1000, 1000, 3), np.uint8)

cv2.line(img, (250, 0), (250, 750), (0, 255, 0), 5)
cv2.line(img, (250, 750), (750, 750), (0, 255, 0), 5)
cv2.line(img, (750, 750), (750, 0), (0, 255, 0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
