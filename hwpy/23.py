import numpy as np
import cv2

img = cv2.imread('Lenna_pepperSalt.jpg')
blur_image1 = cv2.medianBlur(img, 3)
blur_image2 = cv2.medianBlur(img, 5)
cv2.imshow('HW2-2.1', blur_image1)
cv2.imshow('HW2-2.2', blur_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
