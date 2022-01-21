import cv2
import numpy as np

path_img = "Resources/shape1.png"
img  = cv2.imread(path_img)

pointsList = []
def mousePoints(event, x,y, flags , params):
    if event == cv2.EVENT_LBUTTONDOWN: 
        pointsList.append([x,y])
        cv2.circle(img, (x,y), 5, (0,0,255), -1)
        print(pointsList)

def get_angle():
    print("angle")

while True:
    
    if (len(pointsList) % 3 ) == 0 and len(pointsList) != 0:
        get_angle()
    if len(pointsList) <4:
        cv2.imshow("Shape" , img)
        cv2.setMouseCallback("Shape" , mousePoints) # set mouse callback on window Image, call mousePoints 
        cv2.waitKey(1)
        # reset pointlist and image
        if cv2.waitKey(1) &  0xFF == ord('q'):
            pointsList = []
            img  = cv2.imread(path_img)
    else:
        break
