import  cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = "Resources/text.png"


img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
# hImg , wImg = int(img.shape[0]) , int(img.shape[1])
hImg , wImg , = img.shape [0] , img.shape [1]
## Image to boxes.
# boxes  = pytesseract. image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ') 
#     x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg -y), (w,hImg -h), (0,255,0), 1)
#     cv2.putText(img , b[0] , (x,hImg -h ), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255) , 2)
##Image to words.
boxes  = pytesseract. image_to_data(img)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x !=0:
        b = b.split() 
        print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,255,0), 1)
            cv2.putText(img , b[-1] , (x,y ), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255) , 2)
            

cv2.imshow("Text", img)
cv2.waitKey(0)