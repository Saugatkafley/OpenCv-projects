import cv2
import numpy as np
import sys
#For windows
# sys.path.append("Others")
sys.path.append("/media/saugat/4ACAC96DCAC955BB/Machine Learning/Murtaza OpenCv/Others") # For Linux
from Utils import *
frameWidth = 480
frameHeight = 480

cap  = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

def empty(a):
    pass

#Parameters for the contour detection
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters" , frameWidth , 80)
cv2.createTrackbar("Threshold1", "Parameters" , 131 , 255 , empty) # 131 is the base value
cv2.createTrackbar("Threshold2", "Parameters" , 202 , 255 , empty) # 202 is the base value
cv2.createTrackbar("Area", "Parameters" , 1000 , 10000 , empty) # 1000 is the base value
def getContours(img , imgContour):
    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area  = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour , cnt , -1 , (255,0,0) , 5)
            #perimenter 
            peri = cv2.arcLength(cnt , True)
            approx = cv2.approxPolyDP(cnt , 0.02 * peri , True) # 0.02 is the accuracy , True is closed contour , False is open contour
            
            print(approx)
            print ("Points approx :" , len(approx))
            x , y , w , h = cv2.boundingRect(approx) # x , y is the top left corner , w , h is the width and height
            # Text markers
            cv2.rectangle(imgContour , (x , y) , (x + w , y + h) , (0,255,0) , 2)
            cv2.putText(imgContour ,"Points"+ str(len(approx)) , (x , y) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255) , 2)
            cv2.putText(imgContour ,"Area"+ str(area) , (x , y+50) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255) , 2)
while True:
    sucess ,img = cap.read()
    img_blur  = cv2.GaussianBlur(img , (5,5) , 1)
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