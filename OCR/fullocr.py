import cv2
import pytesseract
import numpy as np
import math

labelImage = cv2.imread('rotation3.jpg')



# This function fixes rotations in an image, it should be able to correct most angles somewhat although if
# an image is completly flipped sideways or upside down it will correct that
# used code/instructions from https://www.dynamsoft.com/codepool/deskew-scanned-document.html and 
# https://github.com/YogeshGadade/Deep-Learning/blob/master/End_to_end_Auto_Image_tilt_angle_detection_and_correction.ipynb

def rotateImageHough(label):
                
        rotatedImg = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)

        resizeRatio = (480 / len(label))
        width = int(resizeRatio * len(label[0]))
        rotatedImg = cv2.resize(rotatedImg, (width, 480))

        rotatedImg = cv2.bitwise_not(rotatedImg)
        binaryImg = cv2.threshold(rotatedImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (16, 5))
        #dilatedImg = cv2.dilate(binaryImg, kernel)

        cannyImg = cv2.Canny(binaryImg, 100, 100)
        #cv2.imshow('Label', cannyImg)
        #cv2.waitKey(0)

        lineSegments = cv2.HoughLinesP(cannyImg, 1, np.pi / 180.0, 100, 100, 15)
        
        angles = []
        for lineCoordinates in lineSegments:
                angle = math.degrees(math.atan2(lineCoordinates[0][3] - lineCoordinates[0][1], lineCoordinates[0][2] - lineCoordinates[0][0]))
                if not (87 <= abs(angle) <= 90) and angle != -0.0:
                        angles.append(angle)
        

        if len(angles) == 0:
                return label
        
        angles.sort()
        #print(angles)
        median = np.median(angles)

        #print(median)
        height = label.shape[0]
        width = label.shape[1]
        m = cv2.getRotationMatrix2D((width / 2, height / 2), median, 1)
        deskewed = cv2.warpAffine(labelImage, m, (width, height), borderValue=(255,255,255))

        return deskewed


def displayImage(image):
        cv2.imshow('Label', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# This function performs the preprocessing steps for OCR, it rotates the image, converts it to greyscale
# Then turns it into a binary image, then blurs with gaussian

def preProcess(label):

        rotatedTestImg = rotateImageHough(label)
        greyImg = cv2.cvtColor(rotatedTestImg, cv2.COLOR_BGR2GRAY)
        binaryImg = cv2.threshold(greyImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        blurredImg = cv2.GaussianBlur(binaryImg, (3, 3), 0)


        
        resizeRatio = (480 / len(label))
        width = int(resizeRatio * len(label[0]))
        finalImg = cv2.resize(blurredImg, (width, 480))

        return finalImg



# calls the preprocessing then displays the image and returns the text

def extractText(label):
        processedImg = preProcess(label)
        displayImage(processedImg)
        imageText = pytesseract.image_to_string(processedImg)
        return imageText

        #imageText = imageText.splitlines()
        #print(imageText)


print(extractText(labelImage))


