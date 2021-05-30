import cv2 
from pyzbar.pyzbar import decode

img = cv2.imread('Qrcode.png')


for code in decode(img):
    print(code.type)
    print(code.data.decode('utf-8'))