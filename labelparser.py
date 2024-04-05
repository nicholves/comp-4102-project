
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
    
    def toDict(self):
        return {
            "servings_per_container": self.servings_per_container,
            "serving_size": self.serving_size,
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
                "vitamin_d": self.special_nutrients.vitamin_d,
                "calcium": self.special_nutrients.calcium,
                "iron": self.special_nutrients.iron,
                "potassium": self.special_nutrients.potassium
            }
        }
        
def parse(nl):
    # Create NutritionLabel based on the nutrition label text
    return NutritionLabel("1", "1 cup", "100", "10g", "5g", "0g", "0mg", "0mg", "10g", "20g", "5g", "5g", "1000IU", "1000mg", "10mg", "100mg")  

def parseNutritionLabel(nl_processed):
    nl_processed_parsed = parse(nl_processed)
    
    # compare the two nutrition labels and return the better one
    # return compareParsedLabels(nl_processed_parsed, nl_parsed)
    
    return nl_processed_parsed