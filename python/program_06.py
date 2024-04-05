"""
6. Create a program that calculates and displays the perimeter
of a circle, prompting the user for the radius.
"""

import math

radius = float(input("Enter the radius of the circle: "))

# Calculate the perimeter 
perimeter = 2 * math.pi * radius

print(f"The perimeter of the circle is {perimeter:.2f}")
