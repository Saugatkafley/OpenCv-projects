import cv2
import numpy as np

img  = cv2.imread("Resources/shape1.png")
img.set(3, 500)
img.set(4, 500)

cv2.imshow("Image" , img)
cv2.waitKey(0)
