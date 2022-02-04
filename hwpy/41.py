import cv2 

img = cv2.imread("SQUARE-01.png") 
resize = cv2.resize(img, (256,256))


cv2.imshow('HW4-1', resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

