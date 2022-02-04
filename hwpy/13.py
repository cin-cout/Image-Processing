import numpy as np
import cv2 

img = cv2.imread("Sun.jpg") 

Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('I1', Gray)

B,G,R = cv2.split(img)
Z = B/3+G/3+R/3
Z = np.uint8(Z)
cv2.imshow('I2', Z)


cv2.waitKey(0)
cv2.destroyAllWindows()