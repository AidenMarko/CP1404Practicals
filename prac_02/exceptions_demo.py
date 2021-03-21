"""
CP1404/CP5632 - Practical
Exceptions Demo
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
Question 1
    ValueError will occur if a entered value is not a number
    
Question 2
    ZeroDivisionError will occur if the denominator value is entered as "0"
    
Question 3
    Using an if statement to check prior to doing the division if the denominator is equal to "0"
"""