import numpy as np
import cv2 

img = cv2.imread("Sun.jpg") 

B,G,R = cv2.split(img)

zero = np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow('B channel', cv2.merge([B,zero,zero]))
cv2.imshow('G channel', cv2.merge([zero,G,zero]))
cv2.imshow('R channel', cv2.merge([zero,zero,R]))

cv2.waitKey(0)
cv2.destroyAllWindows()