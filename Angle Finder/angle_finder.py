from cmath import atan
import cv2
import numpy as np
import math
path_img = "Resources/shape2.png"
img  = cv2.imread(path_img)

pointsList = []
def mousePoints(event, x,y, flags , params):
    if event == cv2.EVENT_LBUTTONDOWN: 
        size = len(pointsList) 
        if size !=0 and (size%3) != 0:
            cv2.line(img ,tuple(pointsList[round(((size-1)/3)*3)]) , (x,y), (0,255,0), 2)
        pointsList.append([x,y])
        cv2.circle(img, (x,y), 7, (0,255,0), -1)
        print(pointsList)

def get_angle(m1, m2):
    tanR  = math.atan((m1-m2)/(1+m1*m2) ) 
    tanD  = round(math.degrees(tanR))
    # print("angle :", tanD)
    return tanD

def get_slope(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    return m

angle = 0
while True:
    
    if (len(pointsList) % 3 ) == 0 and len(pointsList) != 0:
        m1 = get_slope(pointsList[0][0],pointsList[0][1],pointsList[1][0],pointsList[1][1])
        m2 = get_slope(pointsList[1][0],pointsList[1][1],pointsList[2][0],pointsList[2][1])
        angle = get_angle(m1,m2)
        cv2.putText(img, "angle :" + str(angle), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if len(pointsList) <4:
        cv2.imshow("Shape" , img)
        cv2.setMouseCallback("Shape" , mousePoints) # set mouse callback on window Image, call mousePoints 
        cv2.waitKey(1)
        # reset pointlist and image
        if cv2.waitKey(1) &  0xFF == ord('r'):
            pointsList = []
            img  = cv2.imread(path_img)
    else:
        break
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
