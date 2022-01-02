import cv2

fieldWidth = 720
fieldHeight = 480
path_img  = "Resources/doctor strange.jpg"
path_mp4 = "Resources/test_video.mp4"

img  = cv2.imread(path_img)
img_greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_greyscale,(7,7),0) # 7x7 kernel shoud be odd , higher kernel size = more blur
img_canny = cv2.Canny(img_blur, 40,40) # 40 ,40 is the threshold

cv2.imshow("Blurred", img)
cv2.imshow("Image Canny", img_canny)
cv2.imshow("Image", img)
# cv2.imshow("Image_Gray", img_greyscale)
cv2.waitKey(0)