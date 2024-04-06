import re

text = """
Nutrition Facts

Valeur nutritive
Per 2 Tbsp. (30 g)
pour 2c. a soupe (30 g)

———
Calories 70 % Daity Value*
ews | Valeur quotidienne*
Fat / Lipldes 6 g 8%
Saturated / saturés 4 g 21%
+ Trans / trans 0.2 9 °
Carbohydrate / Glucides 3 g
Fibre / Fibres 0g 0%
Sugars / Sucres 2 9 2%
Protein / Protéines 2 9
Cholesterol / Cholestérol 20 mg
Sodium 130 mg 6%
ed
Potassium 75 mg . 2%
Calcium 40 mg 3h
Iron / Fer 0 mg 0%
LL
*5% or less is a little, 15% or more is
alot/ *5% ou moins c'est peu, 15% ou
plus c'est beaucoup
"""

def replace_decimal(text):
    pattern = r"\s+\.\s+(\d+)"  # Capture the digit separately
    replacement = lambda match: f" 0.{match.group(1)}"  # Use only the captured digit
    return re.sub(pattern, replacement, text)

def fix_grams(text):
    pattern = r"\s+9(\s|\n)"  # Match whitespace followed by "9" and either whitespace or newline
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


print(process_text(text))
