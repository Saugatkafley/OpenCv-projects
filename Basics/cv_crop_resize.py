import cv2
import numpy as np

img_path = "Resources/doctor strange.jpg"

img  = cv2.imread(img_path)
cv2.imshow("Original", img)
cv2.waitKey(0)