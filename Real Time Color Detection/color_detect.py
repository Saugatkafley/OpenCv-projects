import cv2
import numpy as np

cap  = cv2.VideoCapture(0)

while True:
    sucess , img  = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    
    cv2.imshow('WebCam', img)
    cv2.imshow('WebCam HSV', imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break