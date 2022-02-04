import cv2 
import numpy as np
img = cv2.imread("SQUARE-01.png") 

resize = cv2.resize(img, (256,256))

M = np.float32([[1, 0, 0], [0, 1, 60]])
translation = cv2.warpAffine(resize, M, (400, 300))

rotMat = cv2.getRotationMatrix2D((128,128), 10, 0.5)
ro = cv2.warpAffine(translation, rotMat, (400,300))

a = np.float32([[50,50],[200,50],[50,200]])
b = np.float32([[10,100],[200,50],[100,250]])

m = cv2.getAffineTransform(a,b)
sh = cv2.warpAffine(ro, m, (400,300))
cv2.imshow('HW4-4', sh)

cv2.waitKey(0)
cv2.destroyAllWindows()
