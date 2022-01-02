import numpy as np
import cv2

kernel  = np.ones((3,3), np.uint8) # 5x5 kernel , np.uint8 is unsigned integer 

fieldWidth = 720
fieldHeight = 480
path_img  = "Resources/doctor strange.jpg"
path_mp4 = "Resources/test_video.mp4"

img  = cv2.imread(path_img)
img_greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    # convert to greyscale
img_blur = cv2.GaussianBlur(img_greyscale,(7,7),0)      # 7x7 kernel shoud be odd , higher kernel size = more blur
img_canny = cv2.Canny(img_blur, 40,40)                  # 40 ,40 is the threshold
img_Dilate = cv2.dilate(img_canny, kernel, iterations=3)# dilate the image , iterations = how many times to dilate
img_eroded = cv2.erode(img_Dilate , kernel , iterations  = 5) # erode the image , iterations = how many times to erode

cv2.imshow("Blurred", img)
cv2.imshow("Image Canny", img_canny)
cv2.imshow("Image", img)
cv2.imshow("Image Dilate", img_Dilate)
cv2.imshow("Image_Gray", img_greyscale)
cv2.imshow("Image_Eroded", img_eroded)
cv2.waitKey(0)