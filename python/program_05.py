"""
5. Write a program that calculates the BMI of an individual,
using the formula BMI = weight / height²
"""

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# calculate the BMI
bmi = weight / (height ** 2)

print(f"Your BMI is : {bmi:.3f}")
