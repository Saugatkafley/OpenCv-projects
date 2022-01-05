import numpy as np
import cv2

img  = cv2.imread('Resources/Cards.png')
width, height = 250,350 # width, height ratio of card is 2.5:3.5.
# Points to warp from the picture
pts = np.float32([   [111,219] ,
                   [284,190] , 
                   [154,482] , 
                   [352,440] ] )
pts1 = np.float32([   [0,0] ,
                    [width,0] ,
                    [0,height] ,
                    [width,height] ])
for x in range(4):
    cv2.circle(img,(int(pts[x][0]),int(pts[x][1])),5,(0,0,255),-1)

# cv2.circle(img ,(int(pts[0][0]) , int(pts[0][1])), 5, (0,0,255), cv2.FILLED)
# cv2.circle(img ,(pts[1][0] , pts[1][1]), 5, (0,255,0), cv2.FILLED)
# cv2.circle(img ,(pts[2][0] , pts[2][1]), 5, (255,0,0), cv2.FILLED)
# cv2.circle(img ,(pts[3][0] , pts[3][1]), 5, (0,0,0), cv2.FILLED)

matrix =  cv2.getPerspectiveTransform(pts,pts1)
print(matrix)
output  = cv2.warpPerspective(img,matrix,(width,height))
print(pts) 
cv2.imshow('Original Cards', img)
cv2.imshow("Warped Cards", output)
cv2.waitKey(0)

