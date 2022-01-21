import cv2
import numpy as np
path_img = "Resources/shape1.png"
img  = cv2.imread(path_img)


cv2.imshow("Image" , img)
cv2.waitKey(0)
