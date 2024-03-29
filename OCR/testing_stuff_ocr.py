import cv2
import pytesseract
import numpy as np
from PIL import Image

# pretty print the OCR
def pretty_print(ocr):
    for line in ocr:
        print(line)
        
def remove_lines(image, colors):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bin_image = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    h_contours = get_contours(bin_image, (25, 1))
    v_contours = get_contours(bin_image, (1, 25))

    for contour in h_contours:
        cv2.drawContours(image, [contour], -1, colors[0][0], 2)

    for contour in v_contours:
        cv2.drawContours(image, [contour], -1, colors[0][0], 2)

    return image


def get_contours(bin_image, initial_kernel):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, initial_kernel)

    detected_lines = cv2.morphologyEx(
        bin_image, cv2.MORPH_OPEN, kernel, iterations=2)

    contours = cv2.findContours(
        detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    return contours

def nls_to_text(labelImage):
    # custom_config = r'-l eng+equ'
    imageText = pytesseract.image_to_string(labelImage)
    imageText = imageText.splitlines()
    # remove empty lines
    imageText = [line for line in imageText if len(line) > 0]
    return imageText

def test_nls_to_text():
    labelImage = cv2.imread('OCR/nutrition4.jpg', 0)
    # sharpen the image
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    labelImage = cv2.filter2D(labelImage, -1, kernel)
    cv2.imshow('image', labelImage)
    cv2.waitKey(0)
    
    
    
    imageText = nls_to_text(labelImage)
    return imageText

class SpecialNutrients:
    def __init__(self, vitamin_d, calcium, iron, potassium):
        self.vitamin_d = vitamin_d
        self.calcium = calcium
        self.iron = iron
        self.potassium = potassium

    def __str__(self):
        return f"Special Nutrients:\nVitamin D: {self.vitamin_d}\nCalcium: {self.calcium}\nIron: {self.iron}\nPotassium: {self.potassium}"

class NutritionLabel ():   
    def __init__(self, servings_per_container, serving_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_sugars, total_carbs, dietary_fiber, protein, vitamin_d, calcium, iron, potassium):
        self.servings_per_container = servings_per_container
        self.serving_size = serving_size
        self.calories = calories
        self.total_fat = total_fat
        self.saturated_fat = saturated_fat
        self.trans_fat = trans_fat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.total_carbs = total_carbs
        self.dietary_fiber = dietary_fiber
        self.total_sugars = total_sugars
        self.protein = protein
        self.special_nutrients = SpecialNutrients(vitamin_d, calcium, iron, potassium)

    def __str__(self):
        return f"Nutrition Label:\nServings Per Container: {self.servings_per_container}\nServing Size: {self.serving_size}\nCalories: {self.calories}\nTotal Fat: {self.total_fat}\nSaturated Fat: {self.saturated_fat}\nTrans Fat: {self.trans_fat}\nCholesterol: {self.cholesterol}\nDietary Fiber: {self.dietary_fiber}\nTotal Sugars: {self.total_sugars}\nAdded Sugars: {self.added_sugars}\nProtein: {self.protein}"
    
if __name__ == '__main__':
    pretty_print(test_nls_to_text())
    tets = [0]*31
    tets[30] = 1
    print(tets[2])