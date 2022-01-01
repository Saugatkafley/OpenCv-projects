import cv2

# reading image from resources folder
img  = cv2.imread("Resources/doctor strange.jpg")

cv2.imshow("Doctor strange", img)
cv2.waitKey(0)
