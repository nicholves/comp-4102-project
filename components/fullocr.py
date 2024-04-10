import cv2
import pytesseract
import numpy as np
import math

def rotateImageHough(label):
        """
        This function fixes rotations in an image, it should be able to correct most angles somewhat although if
        an image is completly flipped sideways or upside down it will correct that
        used code/instructions from https://www.dynamsoft.com/codepool/deskew-scanned-document.html and 
        https://github.com/YogeshGadade/Deep-Learning/blob/master/End_to_end_Auto_Image_tilt_angle_detection_and_correction.ipynb                
        """
        
        # Convert the image to grayscale
        rotatedImg = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)

        # Resize the image to a fixed height of 480 pixels
        resizeRatio = (480 / len(label))
        width = int(resizeRatio * len(label[0]))
        rotatedImg = cv2.resize(rotatedImg, (width, 480))

        # Invert the image to have a white background and black text then apply binary thresholding
        rotatedImg = cv2.bitwise_not(rotatedImg)
        binaryImg = cv2.threshold(rotatedImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Apply edge detection using the Canny algorithm
        cannyImg = cv2.Canny(binaryImg, 100, 100)

        # Apply Hough Line Transform to detect lines in the image
        lineSegments = cv2.HoughLinesP(cannyImg, 1, np.pi / 180.0, 100, 100, 15)
        
        
        angles = []
        # Calculate the angle of each line segment
        for lineCoordinates in lineSegments:
                angle = math.degrees(math.atan2(lineCoordinates[0][3] - lineCoordinates[0][1], lineCoordinates[0][2] - lineCoordinates[0][0]))
                if not (87 <= abs(angle) <= 90) and angle != -0.0:
                        angles.append(angle)
                        
        if len(angles) == 0:
                return label
        
        angles.sort()
        median = np.median(angles)

        # Rotate the image by the median angle
        height = label.shape[0]
        width = label.shape[1]
        m = cv2.getRotationMatrix2D((width / 2, height / 2), median, 1)
        deskewed = cv2.warpAffine(label, m, (width, height), borderValue=(255,255,255))

        return deskewed

def preProcess(label):  
        """ This function performs the preprocessing steps for OCR, converts it to grayscale, then turns it into a binary image
        
        Args:
            label: The label image to be preprocessed     
        Returns:
            label: The preprocessed label image
        """
        
        greyImg = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
        binaryImg = cv2.threshold(greyImg, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        return binaryImg


# calls the preprocessing then displays the image and returns the text
def extractText(label):
        """ This function extracts text from the label image using OCR
        
        Args:
            label: The label image to extract text from
        Returns:
            nl_processed: The extracted text from the label image
        """        
        
        if(label is None):
            print("No label found")
            return None
        
        preProcessedLabel = preProcess(label)
        nl_processed = pytesseract.image_to_string(preProcessedLabel, lang='eng')
        return nl_processed


