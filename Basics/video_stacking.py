import  cv2
import numpy as np 
import sys
sys.path.append('Others')
from Utils import *

cap = cv2.VideoCapture(0)
scale  = 0.8



while(1) : 
    sucess , img = cap.read()
    img  = cv2.resize(img, (500,500) ,None ) # None is the interpolation method
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img, (5,5), 0)
    img_canny = cv2.Canny  (img_blur, 50, 50)
    img_dilate = cv2.dilate(img_canny, np.ones((7,7), np.uint8), iterations=1)
    img_erode = cv2.erode  (img_dilate, np.ones((5,5), np.uint8), iterations=1)
    img_blank = np.zeros(img.shape, np.uint8)
    # hr = np.hstack((img_gray,  img_canny , img_dilate))
    # vr = np.hstack((img_blur , img_dilate, img_gray))
    
    Stacked_images = stackImages( ([img, img_gray, img_blur], [img_canny, img_dilate, img_erode]), scale=0.5)
    #capture fps info in opencv
    # image_stacked = np.vstack((hr, vr))
    cv2.imshow("WebCam Stacking", Stacked_images) 
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break