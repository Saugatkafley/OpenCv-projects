import cv2
import numpy as np

img = np.zeros((512,512,3) , np.uint8)

# img[:] = 255,0,0 # Blue color , BGR, : all pixels
# img[20:60,200:300]  =250 ,0, 0 # Selected pixels y first then x

cv2.line(img, (0,0) , (img.shape[1],img.shape[0]) , (0,255,0) , 2) # Diagonal line
print(img.shape)
cv2.imshow("Image", img)
cv2.waitKey(0)
