"""
3. Create a program that calculates and displays the arithmetic
mean of three grades entered by the user.
"""

# get user inputs 
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

# calculate the arithmetic mean 
mean = (grade1 + grade2 + grade3) / 3

print(f"Arithmetic mean: {mean}")
