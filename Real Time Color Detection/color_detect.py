import cv2
import numpy as np

width ,height  = 600 , 480

def nothing(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 600,240)
cv2.createTrackbar("Hue Min", "HSV",   0,   179, nothing)
cv2.createTrackbar("Hue Max", "HSV",   179, 179, nothing)
cv2.createTrackbar("SAT Min", "HSV",   0,   255, nothing)
cv2.createTrackbar("SAT Max", "HSV",   255, 255, nothing)
cv2.createTrackbar("Value Min", "HSV", 0,   255, nothing)
cv2.createTrackbar("Value Max", "HSV", 255,   255, nothing)
cap  = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

while True:
    sucess , img  = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    h_min =cv2.getTrackbarPos("Hue Min","HSV")
    h_max =cv2.getTrackbarPos("Hue Max","HSV")
    s_min =cv2.getTrackbarPos("SAT Min","HSV")
    s_max =cv2.getTrackbarPos("SAT Max","HSV")
    v_min =cv2.getTrackbarPos("Value Min","HSV")
    v_max =cv2.getTrackbarPos("Value Max","HSV")
    
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask  =cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img , img, mask = mask)
    
    cv2.imshow('WebCam', img)
    # cv2.imshow('WebCam HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break