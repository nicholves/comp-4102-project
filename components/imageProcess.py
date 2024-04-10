import numpy as np
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # reading images
from skimage.color import rgb2gray # converting rgb images to grayscale
import cv2

import components.fullocr as fullocr
import components.labelparser as lp
import components.labelML as labelML

def processImage(image):
    """
    Process an image by rotating it (if necessary), running a machine learning model on it,
    extracting text using OCR, and parsing the nutrition label.

    Args:
        image (PIL.Image.Image): The input image to be processed.

    Returns:
        tuple: A tuple containing the parsed nutrition label and a flag indicating success.
            The parsed nutrition label is a dictionary containing the extracted information.
            The success flag is True if the image processing was successful, False otherwise.
    """
    
    # rotate the image if width > height (to account for mobile uploads)
    if image.shape[1] > image.shape[0]:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    # Resize image to have a width of 1000 pixels while maintaining aspect ratio
    width_ratio = 1000 / image.shape[1]
    width = 1000
    height = int(image.shape[0] * width_ratio)
    image = cv2.resize(image, (width, height))
    
    rotated, success = processImageHelper(image, rotate=True)
    if rotated is not None:
        return rotated, success

    return processImageHelper(image, rotate=False)
    

def processImageHelper(image, rotate):
    """
    Helper function to process an image by rotating it (if necessary), running a machine learning model on it,
    extracting text using OCR, and parsing the nutrition label.
    
    Args:
        image (PIL.Image.Image): The input image to be processed.
        rotate (bool): A flag indicating whether to rotate the image.
        
    Returns:
        tuple: A tuple containing the parsed nutrition label and a flag indicating success.
            The parsed nutrition label is a dictionary containing the extracted information.
            The success flag is True if the image processing was successful, False otherwise.
    """    
      
    try:  
        copyImage = image.copy()
        
        # Rotate image if necessary
        if rotate:
            copyImage = fullocr.rotateImageHough(copyImage)
            # show the image
        
        # Run model on rotated and original image and return the better one
        output, success = labelML.runModel(copyImage)
        
        if not success:
            return None, False
        if output is None:
            return None, True
        
        if rotate and output.shape[1] > output.shape[0]:
            output = cv2.rotate(output, cv2.ROTATE_90_CLOCKWISE)
        
        
        # Use OCR to extract text from nutrition label
        nl_processed = fullocr.extractText(output)
        if(nl_processed is None):
            print("No text extracted from OCR")
            return None, True
        
        # parse both nutrition label and processed nutrition label and return better one
        label = lp.parseNutritionLabel(nl_processed)
        if label is None:
            print("Failed to parse nutrition label")
            return None, True

        return label.toDict(), True
    except Exception as e:
        print(f"An error occurred in image processing: {e}")
        return None, False