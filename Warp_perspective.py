import cv2
import numpy as np

img=cv2.imread("Resources/joker.jpg")

width,height=250,350
pt1=np.float32([[189,58],[539,38],[229,610],[584,580]])
# print(pt1)
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pt1,pt2)
output=cv2.warpPerspective(img,matrix,(width,height))

for i in range(0,4):
    cv2.circle(img,(int(pt1[i][0]),int(pt1[i][1])),25,(0,255,0),cv2.FILLED)

cv2.imshow("original img",img)
cv2.imshow("output image",output)
cv2.waitKey(0)
