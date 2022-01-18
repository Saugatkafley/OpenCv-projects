import cv2
import numpy as np

#Frame Width and Height
framewidth  , frameheight = 500 , 500
cap  = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)

# tracker = cv2.TrackerMOSSE_create()
tracker  = cv2.TrackerCSRT_create()
sucess , img = cap.read()
bounding_box = cv2.selectROI("WebCam" , img, False)
tracker.init(img, bounding_box)

def drawBox(img, bounding_box):
    x,y,w,h = int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
    cv2.putText(img, "Tracking", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
    
while True:
    timer  = cv2.getTickCount()
    sucess , img  = cap.read()
    fps   = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, "fps" +str(int (fps)) , (10,50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 2)
    
    sucess , bounding_box = tracker.update(img)
    
    if sucess :
        drawBox(img,bounding_box)
    else:
        cv2.putText(img, "Lost" , (10,80) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 2)
    cv2.imshow("WebCam" , img)
    if cv2.waitKey(2) & 0xFF  == ord('q'):
        break
