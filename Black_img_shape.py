import cv2
import numpy as np

# img=np.zeros((512,512))  #black Image

img=np.zeros((512,512,3),np.uint8)
print(img.shape)
# img[:]=255,0,0    #img[height, width]  blue color
# img[20:30,60:100]=255,0,0


# cv2.line(img,(0,0),(100,100),(0,255,0),1)  #draw line(img,startpt,endpt,color)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),50,(254,0,0),3)
cv2.putText(img,"Draw Shape",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1 )


cv2.imshow("image_name",img)
cv2.waitKey(0)