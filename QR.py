#QR GENERATOR
import qrcode
input=input("Please enter the Text or link you want to share...")
qr=qrcode.make(input)
qr.save("image.jpg")

#DISPLAY QR
from PIL import Image
im = Image.open("image.jpg")
im.show()

#QR READER
import cv2
seek=cv2.QRCodeDetector()
retval, points, straight_qrcode= seek.detectAndDecode(cv2.imread("image.jpg")) #since detectAndDecode returns 3 value
print(retval) #The reval variable stores the string