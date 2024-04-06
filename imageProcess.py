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

        # if there are no detections, return None and False
        if results.pandas().xyxy[0].empty:
            return None, True
        
        # Get the first result and 
        crop = cropImage(image, results.crop(save=False)[0])
        if crop is None:
            return None, False
        
        return crop, True
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred in model processing: {e}")
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
        print(f"An error occurred cropping: {e}")
        return None

def processImage(image):
    # resize image to 480 pixels
    width_ratio = 3000 / image.shape[1]
    width = 3000
    height = int(image.shape[0] * width_ratio)
    image = cv2.resize(image, (width, height))
    
    rotated, success = processImageHelper(image, rotate = True)
    if rotated is not None:
        return rotated, success

    return processImageHelper(image, rotate = False)
    

def processImageHelper(image, rotate = True):
    try:  
        copyImage = image.copy()
        
        # Rotate image if necessary
        if rotate:
            copyImage = fullocr.rotateImageHough(copyImage)
        
        # Run model on rotated and original image and return the better one
        output, success = runModel(copyImage)
        
        if not success:
            return None, False
        if output is None:
            return None, True
        
        # Use OCR to extract text from nutrition label
        nl_processed = fullocr.extractText(output)
        
        # parse both nutrition label and processed nutrition label and return better one
        label = lp.parseNutritionLabel(nl_processed)
        if label is None:
            return None, True

        return label, True
    except Exception as e:
        print(f"An error occurred in image processing: {e}")
        return None, False