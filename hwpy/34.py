import cv2 
import numpy as np
import math
img = cv2.imread("House.jpg") 

Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ans = np.copy(Gray)

G = [[0.045,0.122,0.045],[0.122,0.332,0.122],[0.045,0.122,0.045]]

for i in range(349):
    for j in range(598):
        if (i != 0) & (i != 348) & (j!=0) & (j!=597):
            ans[i][j] = Gray[i-1][j-1]*G[0][0] + Gray[i-1][j]*G[0][1]+ Gray[i-1][j+1]*G[0][2] + Gray[i][j-1]*G[1][0]+ Gray[i][j]*G[1][1] + Gray[i][j+1]*G[1][2] + Gray[i+1][j-1]*G[2][0] + Gray[i+1][j]*G[2][1] + Gray[i+1][j+1]*G[2][2]

ans2 = np.copy(ans)
for i in range(349):
    for j in range(598):
        if (i != 0) & (i != 348) & (j!=0) & (j!=597):
            a = abs(ans[i-1][j-1]*(-1)+ ans[i-1][j+1]*1 + ans[i][j-1]*(-2)  + ans[i][j+1]*2 + ans[i+1][j-1]*(-1)  + ans[i+1][j+1]*(1))
            b = abs(ans[i-1][j-1]*(1) + ans[i-1][j]*2 + ans[i-1][j+1]*1 + ans[i+1][j-1]*(-1) + ans[i+1][j]*(-2) + ans[i+1][j+1]*(-1))
            ans2[i][j] = math.sqrt(a ** 2 + b ** 2)
        else:
            ans2[i][j] = 0

cv2.imshow('HW3-2', ans2)
cv2.waitKey(0) 
cv2.destroyAllWindows()

