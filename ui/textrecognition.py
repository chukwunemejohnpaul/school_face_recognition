import pytesseract
import cv2
img = cv2.imread("download.jpg")
config = ("-l eng --oem 1 --psm 7")
text = pytesseract.image_to_string(img, config=config)
print(text)