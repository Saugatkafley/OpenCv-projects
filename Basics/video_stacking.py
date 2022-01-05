import  cv2
import numpy as np 

cap = cv2.VideoCapture(0)
scale  = 0.8

def stackImages(imgArray,scale,lables=[]):
    sizeW= imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

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