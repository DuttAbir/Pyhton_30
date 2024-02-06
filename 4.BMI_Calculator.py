"""
    Calculate the Body Mass Index (BMI) and determine the BMI category.
    
    :param height: Height in centimeters.
    :param weight: Weight in kilograms.
    :return: A tuple containing the BMI value (rounded to two decimal places) and the BMI category.
"""


def calculate_bmi(height, weight):
    category = ""
    height=height/100
    BMI = round(weight/(height**2), 2)
    if BMI < 18.5:
        category="underweight"
    elif (BMI>18.5 and BMI <25):
        category="healthy"
    elif (BMI > 25 and BMI < 30):
        category="overweight"
    else:
        category="obese"
    return (BMI, category)


# Example function calls
print(calculate_bmi(155, 43.3))  # Expected: (18.02, "underweight")
print(calculate_bmi(170, 62.2))  # Expected: (21.52, "healthy")
print(calculate_bmi(150, 77.1))  # Expected: (34.27, "obese")
print(calculate_bmi(189, 101.2)) # Expected: (28.37, "overweight")