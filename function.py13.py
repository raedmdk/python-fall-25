"""
PE1 4.1 – Functions
Author: Raed Al Kiswani
Date: September 30, 2025

This program has two functions to calculate areas:
- square: calculates the area of a square
- circle: calculates the area of a circle
"""

# function to calculate the area of a square
def square(side):
    area = side * side
    print("The area of the square is", area, "square units.")

# function to calculate the area of a circle
def circle(radius):
    pi = 3.14
    area = pi * radius * radius
    print("The area of the circle is", area, "square units.")

# test calls with sample values
print("--- Testing My Functions ---")
square(4)      # example side length
circle(5)      # example radius
