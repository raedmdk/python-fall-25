"""
PE1 3.1B: elif
Assignment: Numeric Grade to Letter Grade Converter

This program asks the user to enter a numeric grade (0–100).
It uses if/elif/else statements to determine the correct letter grade
based on the following scale:
90–100 = A
80–89  = B
70–79  = C
60–69  = D
Below 60 = F

If the input is not between 0 and 100, the program displays an error message.
"""

# Ask the user for their numeric grade
grade = int(input("Enter the numeric grade (0-100): "))

# Check if the grade is within a valid range
if grade < 0 or grade > 100:
    print("Error: Grade must be between 0 and 100.")
elif grade >= 90:   # 90–100
    print("The letter grade is: A")
elif grade >= 80:   # 80–89
    print("The letter grade is: B")
elif grade >= 70:   # 70–79
    print("The letter grade is: C")
elif grade >= 60:   # 60–69
    print("The letter grade is: D")
else:               # Below 60
    print("The letter grade is: F")

# TODO: Enhance program later to accept multiple grades and average them
