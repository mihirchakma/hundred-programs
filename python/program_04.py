"""
4. Write a program that calculates the geometric mean of three
numbers entered by the user
"""

# imported math module 
import math 

# get inputs from user 
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the first number: "))
number_3 = float(input("Enter the first number: "))

# calculate the geometric mean 
product = number_1 * number_2 * number_3
geometric_mean = math.pow(product, 1/3)

print(f"Geometric mean : {geometric_mean:.2f}")
