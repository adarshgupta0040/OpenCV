import cv2 as cv
import numpy as np

framewidth=440
frameheight=380
cap=cv.VideoCapture(0)
cap.set(3,framewidth)                   #change Resulution
cap.set(4,frameheight)

def empty():
    pass
cv.namedWindow("HSV")
cv.resizeWindow("HSV",500,200)
cv.createTrackbar("Min Hue","HSV",0,179,empty)    #min is 0 and max is 179
cv.createTrackbar("Max Hue","HSV",179,179,empty)
cv.createTrackbar("Min Sat","HSV",0,255,empty)    #min is 0 and max is 255
cv.createTrackbar("Max Sat","HSV",255,255,empty)
cv.createTrackbar("Value Min","HSV",0,255,empty)
cv.createTrackbar("Value Max","HSV",255,255,empty)


while True:
    success , img = cap.read()
    imgHSV=cv.cvtColor(img,cv.COLOR_RGB2HSV)

    h_min = cv.getTrackbarPos("Min Hue","HSV")
    h_max = cv.getTrackbarPos("Max Hue", "HSV")
    s_min = cv.getTrackbarPos("Min Sat", "HSV")
    s_max = cv.getTrackbarPos("Max Sat", "HSV")
    v_min = cv.getTrackbarPos("Value Min", "HSV")
    v_max = cv.getTrackbarPos("Value Max", "HSV")
    print(h_min)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv.inRange(imgHSV,lower,upper)
    result=cv.bitwise_and(img,img,mask=mask)

    # mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,result])

    # cv.imshow("original", img)
    # # cv.imshow("HSV color Space", imgHSV)
    # cv.imshow("mask", mask)
    cv.imshow("Horizontal", hstack)
    if cv.waitKey(1) & 0xFF == ord('c'):  # 1 for live cam and 0 for pause cam
        break

cap.release()
cv.destroyAllWindows()
