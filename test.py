import numpy as np
import cv2

img = cv2.imread('food.jpg')
img = cv2.line(img, (0,0), (255,255), (0,0,255), 10 )
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
