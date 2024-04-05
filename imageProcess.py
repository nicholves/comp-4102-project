import numpy as np
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # reading images
from skimage.color import rgb2gray # converting rgb images to grayscale
import torch
import cv2

import OCR.fullocr as fullocr
import labelparser as lp


def loadModel():
    model_path = 'models/exp5/weights/best.pt'
    model = torch.hub.load('yolov5', 'custom', path=model_path, source='local')    
    return model

model = loadModel()

def runModel(image):
    try:
        results = model(image)

        # Check if there are any results
        if results.pred[0] is None:
            return None, False

        # Get the first result and 
        crop = cropImage(image, results.crop(save=False)[0])
        if crop is None:
            return None, False
        
        return crop, True
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred: {e}")
        return None, False

def cropImage(image, crop):
    try:
        # Get the bounding box of the crop
        x1, y1, x2, y2 = crop['box']
        
        # convert to integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Crop the image
        cropped_image = image[y1:y2, x1:x2]
        
        return cropped_image
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred: {e}")
        return None


def processImage(image):
    try:  
        # Rotate image if necessary
        rotated = fullocr.rotateImageHough(image)
        fullocr.displayImage(rotated)
        
        # Run model on rotated and original image and return the better one
        output, success = runModel(rotated)
        if not success:
            output, success = runModel(image)
            if not success:
                return None, False
        
        # Use OCR to extract text from nutrition label
        nl_processed = fullocr.extractText(output)
        
        # parse both nutrition label and processed nutrition label and return better one
        label = lp.parseNutritionLabel(nl_processed)

        return label, True
    except Exception as e:
        print(e)
        return None, False