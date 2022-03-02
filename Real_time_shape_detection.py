import cv2 as cv
import numpy as np

frameWidth = 100
frameHeight = 100
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv.namedWindow("Parameter")
cv.resizeWindow("Parameter",200,150)
cv.createTrackbar("Threshold_1","Parameter",101,255,empty)
cv.createTrackbar("Threshold_2","Parameter",77,255,empty)
cv.createTrackbar("Area","Parameter",5000,30000,empty)

def stackImages(imgArray,scale,lables=[]):
    sizeW= imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv.FILLED)
                cv.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def get_contours(img,img_contour):
    contour,heirarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    for cnt in contour:
        area = cv.contourArea(cnt)
        areaMin = cv.getTrackbarPos("Area", "Parameter")
        if area > areaMin:
            cv.drawContours(img_contour,contour,-1,(255,0,255),5)
            peri=cv.arcLength(cnt,True)
            approx=cv.approxPolyDP(cnt,0.02 * peri,True)
            print(len(approx))
            x,y,w,h=cv.boundingRect(approx)
            cv.rectangle(img_contour,(x,y),(x+w,y+h),(0,255,0),5)
            cv.putText(img_contour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv.putText(img_contour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)



while True:
    success,img=cap.read()
    img_Contour=img.copy()

    img_blur=cv.GaussianBlur(img,(7,7),1)
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    Threshold_1=cv.getTrackbarPos("Threshold_1","Parameter")
    Threshold_2=cv.getTrackbarPos("Threshold_2","Parameter")
    img_canny=cv.Canny(img_gray,Threshold_1,Threshold_2)
    kernel=np.ones((5,5))
    img_dilation=cv.dilate(img_canny,kernel,iterations=1)

    get_contours(img_dilation,img_Contour)

    StackedImages = stackImages(([img, img_gray,img_Contour],
                                 [img_canny,img_dilation,img_Contour]), 0.6)
    # StackedImages = stackImages(([img],
    #                              [img_Contour]), 0.6)
    cv.imshow("Staked Images", StackedImages)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
