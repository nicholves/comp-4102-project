import numpy as np
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # reading images
from skimage.color import rgb2gray # converting rgb images to grayscale

def processImage(image):
    # convert to grayscale
    image = rgb2gray(image)
    
    # print image to console
    print(image)   

    return image