import cv2

frameWidth  = 640
frameHeight = 480

cap  = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while(True):
    sucess , img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    img  =cv2.imshow("Video", img)
    if cv2.waitKey(2)  &  0xFF == ord('q'):
        break