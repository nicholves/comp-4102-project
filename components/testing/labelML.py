
import torch
import cv2

def loadModel():
    """ Load the YOLOv5 model from the specified path and return it"""
    
    model_path = 'models/exp5/weights/best.pt'
    model = torch.hub.load('yolov5', 'custom', path=model_path, source='local')    
    return model

def cropImage(image, crop):
    """ Crop the image using the bounding box of the crop

    Args:
        image (np.array): The image to crop
        crop (dict): The crop object containing the bounding box

    Returns:
        np.array: The cropped image
    """
    
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
        print(f"An error occurred during cropping: {e}")
        return None

def runModel(image):
    """ Run Nutrition Label Detection model on the image and return the cropped image if successful """
    
    try:
        results = model(image)

        # if there are no detections, return None and False
        if results.pandas().xyxy[0].empty:
            print("No detections found")
            return None, True
        
        # Get the first result and 
        crop = cropImage(image, results.crop(save=False)[0])
        if crop is None:
            print("Failed to crop image")
            return None, False
        
        return crop, True
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred in model processing: {e}")
        return None, False
    
model = loadModel()