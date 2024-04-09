import re 

class SpecialNutrients:
    def __init__(self, calcium, iron, potassium):
        self.calcium = calcium
        self.iron = iron
        self.potassium = potassium
        
    def __str__(self) -> str:
        return f"Calcium: {self.calcium}, Iron: {self.iron}, Potassium: {self.potassium}"

class NutritionLabel ():   
    def __init__(self, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_sugars, total_carbs, dietary_fiber, protein, calcium, iron, potassium):
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
        self.special_nutrients = SpecialNutrients(calcium, iron, potassium)    
        
    def __init__(self, nlDict: dict):
        self.calories = nlDict.get("calories", None)
        self.total_fat = nlDict.get("total_fat", None)
        self.saturated_fat = nlDict.get("saturated_fat", None)
        self.trans_fat = nlDict.get("trans_fat", None)
        self.cholesterol = nlDict.get("cholesterol", None)
        self.sodium = nlDict.get("sodium", None)
        self.total_carbs = nlDict.get("total_carbs", None)
        self.dietary_fiber = nlDict.get("dietary_fiber", None)
        self.total_sugars = nlDict.get("total_sugars", None)
        self.protein = nlDict.get("protein", None)
        self.special_nutrients = SpecialNutrients(nlDict.get("calcium", None), nlDict.get("iron", None), nlDict.get("potassium", None))
    
    def toDict(self):
        return {
            "calories": self.calories,
            "total_fat": self.total_fat,
            "saturated_fat": self.saturated_fat,
            "trans_fat": self.trans_fat,
            "cholesterol": self.cholesterol,
            "sodium": self.sodium,
            "total_carbs": self.total_carbs,
            "dietary_fiber": self.dietary_fiber,
            "total_sugars": self.total_sugars,
            "protein": self.protein,
            "special_nutrients": {
                "calcium": self.special_nutrients.calcium,
                "iron": self.special_nutrients.iron,
                "potassium": self.special_nutrients.potassium
            }
        }
    
    def __str__(self):
        return f"Calories: {self.calories}, Total Fat: {self.total_fat}, Saturated Fat: {self.saturated_fat}, Trans Fat: {self.trans_fat}, Cholesterol: {self.cholesterol}, Sodium: {self.sodium}, Total Carbs: {self.total_carbs}, Dietary Fiber: {self.dietary_fiber}, Total Sugars: {self.total_sugars}, Protein: {self.protein}, {self.special_nutrients}"
  
nutrientSize = 13
  
def replace_decimal(text):
    pattern = r"\s+\.\s+(\d+)"  # Capture the digit separately
    replacement = lambda match: f" 0.{match.group(1)}"  # Use only the captured digit
    return re.sub(pattern, replacement, text)

def fix_grams(text):
    pattern = r"\s+9(\s|\n)(^g)"  # Match whitespace followed by "9" and either whitespace or newline
    replace = lambda match: " g" + (match.group(1) or "")  # Add "g" and optionally the captured group (whitespace or newline)
    return re.sub(pattern, replace, text)

def remove_percent(text):
    pattern = r"\d+(?:\.\d+)?%"  # Match one or more digits, optionally followed by a decimal and more digits, then "%"
    return re.sub(pattern, "", text)

def clean_text(text):
    pattern = r"[^a-zA-Z0-9\.\n\s]"
    text = re.sub(pattern, "", text)
    pattern = r" +"
    text = re.sub(pattern, " ", text)
    return text

def remove_before_calorie(text):
    # Find the index of the first occurrence of "calorie" (or -1 if not found).
    calorie_index = text.find("calorie")
    return text[calorie_index:] if calorie_index != -1 else text

def insert_space(text):
    # Match a digit sequence followed by 'm' or 'g' and add a space between them
    pattern = r"(\d+)([mg])"
    return re.sub(pattern, r"\1 \2", text)

def remove_non_numeric(text):
    # remove all lines that do not contain a digit
    pattern = r"\d"
    return "\n".join(line for line in text.splitlines() if re.search(pattern, line))

def process_text(text):
    new_text = text.lower()
    new_text = remove_before_calorie(new_text)
    new_text = replace_decimal(new_text)
    new_text = remove_percent(new_text)
    new_text = fix_grams(new_text)
    new_text = clean_text(new_text)
    new_text = insert_space(new_text)
    new_text = remove_non_numeric(new_text)
    return new_text     

def parseNutritionLabel(nl_processed):
    try:    
        # Parse the nutrition label text
        nl_processed = process_text(nl_processed)
        
        # split the text into lines and strip whitespace
        lines = [line.strip() for line in nl_processed.split('\n')]

        nutrients = {
            "calo": "calories",
            "fat": "total_fat",
            "sat": "saturated_fat",
            "tran": "trans_fat",
            "carb": "total_carbs",
            "fib": "dietary_fiber",
            "flb": "dietary_fiber", # i has been mistaken for l
            "sug": "total_sugars",
            "prot": "protein",
            "chol": "cholesterol",
            "sod": "sodium",
            "pot": "potassium",
            "calc": "calcium",
            "ron": "iron"
        }
            
        nlDict = {}
        found = 0
        for line in lines:
            for nutrient in nutrients.keys():
                if nutrient in line:
                    found += 1
                    temp = line.split(" ")
                    if len(temp) < 2:
                        continue
                    
                    # Get the first float in temp
                    value = [s for s in temp if is_float(s)]
                    if len(value) == 0:
                        continue
                    index = temp.index(value[0])
                    
                    # check if the unit is in the next index
                    unit = None
                    if index + 1 < len(temp) and temp[index + 1] == "mg":
                        unit = temp[index + 1]
                    
                    if len(value) == 0:
                        continue
                    
                    nlDict[nutrients[nutrient]] = convertToGrams(float(value[0]), unit)
                    nutrients.pop(nutrient)
                    break
        
        if found < 4:  # if it doesn't find at least 4 nutrients, we can't be sure it's a nutrition label
            return None
        return NutritionLabel(nlDict)
    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred in label parser: {e}")
        return None

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def convertToGrams(value, unit):
    if unit and unit == "mg":
        return value / 1000
    return value