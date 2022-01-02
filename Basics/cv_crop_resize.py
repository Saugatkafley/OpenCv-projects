import cv2
import numpy as np

img_path = "Resources/doctor strange.jpg"
width , height  = 500,500
img  = cv2.imread(img_path)
img_resized = cv2.resize(img ,(width,height) )

image_Cropped = img[0:900, 400:1000]            # img[height, width] , y,x
print(img.shape)                                # (900,1600, 3)

cv2.imshow("Original", img)
cv2.imshow("Image Resized", img_resized)
cv2.imshow("Image Cropped", image_Cropped)
cv2.waitKey(0)