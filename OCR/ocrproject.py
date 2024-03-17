import cv2
import pytesseract


labelImage = cv2.imread('nutrition3.jpg')
imageText = pytesseract.image_to_string(labelImage)
print(imageText)

imageText = imageText.splitlines()
print(imageText)


