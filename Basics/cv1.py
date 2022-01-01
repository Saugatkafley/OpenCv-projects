import cv2

path_img  = "Resources/doctor strange.jpg"
path_mp4 = "Resources/test_video.mp4"

img  = cv2.imread(path_img)
cv2.imshow("Image", img)
cv2.waitKey(0)