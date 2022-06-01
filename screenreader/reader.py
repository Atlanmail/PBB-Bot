from configparser import Interpolation
from PIL import Image, ImageOps
import cv2
from pytesseract import pytesseract

path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image_path = r"D:/Programming/Roblox/PBB Bot/screenreader/data/iv test.png"

img = cv2.imread(image_path)
img = cv2.resize(img, (int(img.shape[1]*2.5), int(img.shape[0]*2.5)), interpolation = cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", img)

 # img.show()
# gray = ImageOps.grayscale(img)
# gray.show()


pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img,lang= 'eng', config='-c tessedit_char_whitelist=0123456789 --psm 6')
print(text[:-1])

cv2.waitKey(0) 