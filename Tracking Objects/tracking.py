import cv2
import numpy as np

#Frame Width and Height
framewidth  , frameheight = 400,400
cap  = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)

tracker = cv2.TrackerMOSSE_create()

while True:
    timer  = cv2.getTickCount()
    sucess , img  = cap.read()
    fps   = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int (fps)) , (10,50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 2)
    cv2.imshow("WebCam" , img)
    if cv2.waitKey(2) & 0xFF  == ord('q'):
        break
