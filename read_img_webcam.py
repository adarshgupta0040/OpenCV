import cv2
# img=cv2.imread("Resources/Acorn_PNG739.png")
# cv2.imshow("Lena",img)
# cv2.waitKey(1000)


frameWidth=640
frameHeight=380
cap=cv2.VideoCapture(0)  #for default Camera its 0
#cap=cv2.VideoCapture("Resource/video.mp4")  any video in this folder
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)


while True:
    sucess,img=cap.read()
    img=cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("vdio",img)
    if cv2.waitKey(1) & 0xFF == ord('c'):  #1 for live cam and 0 for pause cam
      break
