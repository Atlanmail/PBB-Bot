from PIL import Image, ImageOps
import cv2
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\tiep1\Pictures\Saved Pictures\test1\ditto2 (2).png"

img = cv2.imread(image_path)
cv2.imshow('image', img)
cv2.waitKey(0) 
 # img.show()
# gray = ImageOps.grayscale(img)
# gray.show()


pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img,lang= 'eng', config='--psm 4')
print(text[:-1])