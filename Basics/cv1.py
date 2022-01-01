import cv2

fieldWidth = 720
fieldHeight = 480
path_img  = "Resources/doctor strange.jpg"
path_mp4 = "Resources/test_video.mp4"

img  = cv2.imread(path_img)
img_greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Image", img)
cv2.imshow("Image", img_greyscale)
cv2.waitKey(0)