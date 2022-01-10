from typing import Counter
import cv2
import numpy as np

img_path = 'Resources/Cards.png'
img_path1  = 'Resources/embeded_cover.jpg'
# Circles to store the coordinates of the detected circles
Circles = np.float32([[0,0],[0,0],[0,0],[0,0]])
points = 0

width , height = 250,350 # width, height ratio of card is 2.5:3.5.
pts1 = np.float32([   [0,0] ,
                    [width,0] ,
                    [0,height] ,
                    [width,height] ])

def MousePoints(events , x,y ,flags , params):
    global points   # Global variable
    global pts1
    if events == cv2.EVENT_LBUTTONDOWN:
        # if points <4: # 4 points are required to warp the image    
        Circles[points][0] = x
        Circles[points][1] = y
        points+= 1
        print(Circles)
    
    


img = cv2.imread(img_path1)
# width , height = img.shape [1] , img.shape [0]
img  = cv2.resize(img, (500,500))

while True :
    
    if points == 4 : 
        matrix  = cv2. getPerspectiveTransform(Circles,pts1)
        output  = cv2.warpPerspective(img , matrix,(width,height))
        # output = cv2.resize(output,(width , height))
        cv2.imshow("Warped Cards", output)
        for i in Circles:
            cv2.circle(img ,(int(i[0]) , int(i[1])), 5, (0,0,255), cv2.FILLED)
        
    cv2.imshow("Original", img)
    cv2.setMouseCallback("Original", MousePoints)

    if cv2.waitKey(0) & 0xFF == ord('q'):
            break
