import cv2

path="Resources/Acorn_PNG739.png"
img=cv2.imread(path)
print(img.shape)

width,hieght=400,400
img_resize=cv2.resize(img,(width,hieght))
print(img_resize.shape)

imgCropped=img[300:540,0:900]    #height,width
imgCropResize=cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
print(imgCropResize)



cv2.imshow("Road",img)
cv2.imshow("Road_resize",img_resize)
cv2.imshow("Road_Croppedresize",imgCropResize)
cv2.waitKey(0)