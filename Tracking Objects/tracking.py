import cv2
import numpy as np

#Frame Width and Height
framewidth  , frameheight = 300,300
cap  = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)

while True:
    sucess , img  = cap.read()
    cv2.imshow("WebCam" , img)
    if cv2.waitKey(1) & 0xFF  == ord('q'):
        break
