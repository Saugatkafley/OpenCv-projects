import cv2
import numpy as np
import sys
sys.path.append('Others')
from Utils import *     # Thanks to Co-Pilot

frameWidth = 480
frameHeight = 480


cap  = cv2.VideoCapture(1)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

def empty(a):
    pass

#Parameters for the contour detection
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters" , frameWidth , 80)
cv2.createTrackbar("Threshold1", "Parameters" , 131 , 255 , empty) # 131 is the base value
cv2.createTrackbar("Threshold2", "Parameters" , 202 , 255 , empty) # 202 is the base value

def getContours(img , imgContour):

    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContour , contours , -1 , (255,0,0) , 3)
while True:
    sucess ,img = cap.read()
    img_blur  = cv2.GaussianBlur(img,(7,7),1)
    img_gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    
    img_canny  = cv2.Canny(img_gray , threshold1 , threshold2)
    kernel    = np.ones((5,5))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=1)
    
    getContours(img_dilate, img)
    output = stackImages(  ( [img , img_canny , img_dilate] ,[img_dilate , img_canny , img_blur]), scale=0.5)
    # cv2.imshow("WebCam" , img)
    # cv2.imshow("WebCam Blur" , img_blur)
    # cv2.imshow("WebCam Gray" , img_gray)

    cv2.imshow("WebCam Stacked" , output)
    # cv2.resizeWindow("WebCam Stacked" , frameWidth , frameWidth)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break