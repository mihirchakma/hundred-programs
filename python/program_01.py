"""
1. Write a program that prompts the user for two numbers and
displays the addition, subtraction, multiplication, and division
between them.
"""

# Prompt the user for two numbers
number_1 = int(input("Enter number 1 : "))
number_2 = int(input("Enter number 2 : "))

# Perform arithmetic calculations
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = float(number_1 / number_2)

# display the results
print(f'Addition : {addition}')
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")
