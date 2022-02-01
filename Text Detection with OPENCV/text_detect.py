import  cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = "Resources/text.png"
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
hImg , wImg , = img.shape [0] , img.shape [1]

print("Enter 1 to read image as characters and 2 to read image as words:")
ch = int(input("Enter your choice: "))

if ch ==1:
    ## Image to boxes.
    config = r'--oem 3 --psm 6 outputphase digits'
    boxes  = pytesseract. image_to_boxes(img , config = config)
    for b in boxes.splitlines():
        b = b.split(' ') 
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg -y), (w,hImg -h), (0,255,0), 1)
        cv2.putText(img , b[0] , (x,hImg -h ), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255) , 2)
    cv2.imshow("Text", img)
    cv2.waitKey(0)

    # hImg , wImg = int(img.shape[0]) , int(img.shape[1])
elif ch ==2:
    ##Image to words.
    # Detect only digits.
    config = r'--oem 3 --psm 6 outputphase digits'
    boxes  = pytesseract. image_to_data(img, config=config)
    # print(boxes)
    for x,b in enumerate(boxes.splitlines()):
        if x !=0:
            b = b.split() 
            if len(b) == 12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x,y), (w+x, h+y), (0,255,0), 1)
                cv2.putText(img , b[-1] , (x,y ), cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,0,255) , 1)
    cv2.imshow("Text", img)
    cv2.waitKey(0)
else:
    print("Invalid choice")