import cv2 

img = cv2.imread("Sun.jpg") 

cv2.imshow('HW1-1', img)
print("Height :",img.shape[0])
print("Width :",img.shape[1])

cv2.waitKey(0)
cv2.destroyAllWindows()