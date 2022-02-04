import cv2 
import numpy as np

src1 = cv2.imread("Dog_Strong.jpg")
src2 = cv2.imread("Dog_Weak.jpg")

def on_change(x): 
    pass

img = np.zeros((532,799,3),np.uint8)
cv2.namedWindow('HW1-4')
cv2.createTrackbar('a', 'HW1-4', 0, 100, on_change)

while(1):
    cv2.imshow('HW1-4', img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
       break
            
    r = cv2.getTrackbarPos('a', 'HW1-4')
    r =  float(r)/100.0
    img = cv2.addWeighted(src1,r,src2,(1.0-r),0)
    
cv2.waitKey(0) 
cv2.destroyAllWindows()