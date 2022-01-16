import cv2
import numpy as np
import sys
sys.path.append('Others')
from Utils import *     # Thanks to Co-Pilot

frameWidth = 640
frameHeight = 480


cap  = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

#Parameters for the contour detection
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters" , frameWidth , 80)
cv2.createTrackbar("Threshold1", "Parameters" , 150 , 255 , empty)
cv2.createTrackbar("Threshold2", "Parameters" , 255 , 255 , empty)

while True:
    sucess ,img = cap.read()
    img_blur  = cv2.GaussianBlur(img,(7,7),1)
    img_gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    
    
    img_canny  = cv2.Canny(img_gray , threshold1 , threshold2)
    output = stackImages(  ( [img , img_canny , img_gray] ,[img , img_canny , img_blur]), scale=0.1) 
    # cv2.imshow("WebCam" , img)
    # cv2.imshow("WebCam Blur" , img_blur)
    # cv2.imshow("WebCam Gray" , img_gray)

    cv2.imshow("WebCam Stacked" , output)
    # cv2.resizeWindow("WebCam Stacked" , frameWidth , frameWidth)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break