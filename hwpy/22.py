import numpy as np
import cv2

img = cv2.imread('Lenna_whiteNoise.jpg')
blur_image = cv2.bilateralFilter(img, 9, 90, 90)

cv2.imshow('HW2-2', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

