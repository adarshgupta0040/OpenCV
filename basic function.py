import cv2

import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)


path="Resources/Acorn_PNG739.png"
img=cv2.imread(path)

#img=cv2.imread(path,0)  0 for making img gray/black-white or below too can do same
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(7,7),0)
img_canny=cv2.Canny(img,100,200)
img_dilation=cv2.dilate(img_canny,kernel,iterations=1)
img_eroded=cv2.erode(img_dilation,kernel,iterations=2)

cv2.imshow("GrayImg",img_gray)    #black_white img
cv2.imshow("lena",img)              #original img
cv2.imshow("blured",img_blur)
cv2.imshow("Canny",img_canny)
cv2.imshow("img_dilation",img_dilation)
cv2.imshow("img_eroded",img_eroded)
cv2.waitKey(0)