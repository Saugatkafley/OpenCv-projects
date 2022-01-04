import cv2
import numpy as np

img = np.zeros((512,512,3) , np.uint8)

# img[:] = 255,0,0 # Blue color , BGR, : all pixels
# img[20:60,200:300]  =250 ,0, 0 # Selected pixels y first then x

cv2.line(img, (0,0) , (img.shape[1],img.shape[0]) , (0,255,0) , 2) # Diagonal line
cv2.rectangle(img,(200,200) , (300,300), (0,255,255) , cv2.FILLED) # Rectangle
cv2.circle(img, (400,400) , 100 , (255,255,0) , 2) # Circle
cv2.putText(img, "Text Box" , (200,200) , cv2.FONT_HERSHEY_PLAIN ,1 ,(0,0,255), 1) # Text
print(img.shape)
cv2.imshow("Image", img)
cv2.waitKey(0)
