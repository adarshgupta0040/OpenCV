import cv2
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)



img = cv2.imread('Resources/joker.jpg')
cv2.imshow("Original Image ", img)
cv2.setMouseCallback("Original Image ", mousePoints)
cv2.waitKey(0)