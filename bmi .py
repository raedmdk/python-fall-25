"""
PE1 4.4 – BMI Calculator (Scope)
Author: Raed Al Kiswani
Date: September 30, 2025

This program calculates BMI using global constants for unit conversion.
It asks for weight and height, converts to metric, then prints BMI and category.
"""

# ===== Global constants (scope demo) =====
LB_TO_KG = 0.453592   # 1 lb = 0.453592 kg
IN_TO_M  = 0.0254     # 1 in = 0.0254 m

# ----- function to calculate BMI (local scope) -----
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    return bmi

# ----- function to classify BMI (local scope) -----
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

# ----- main controls program flow -----
def main():
    # casual + personal prompts
    weight_lb = float(input("Raed, type your weight in lbs: "))
    height_in = float(input("Now give me your height in inches: "))

    # convert to metric using global constants
    weight_kg = weight_lb * LB_TO_KG
    height_m  = height_in * IN_TO_M

    # calculate BMI and category
    bmi = calculate_bmi(weight_kg, height_m)
    category = categorize_bmi(bmi)

    # show results
    print("\nYour BMI is:", round(bmi, 2))
    print("You are in the", category, "category.")
    print("Not bad, keep hitting the gym 💪")

# run the program
main()
