"""
PE1 4.7 – Exceptions
Author: Raed Al Kiswani
Date: October 7, 2025

Goal:
Enhance a basic "square a number" program with exception handling.
Demonstrates try, except, else, and finally.
"""

def square_number():
    raw = input("Enter a number to square: ")

    try:
        number = int(raw)          # may raise ValueError if not an integer string
    except ValueError:
        print("Error: please enter a whole number (e.g., 7).")
    else:
        squared_number = number ** 2
        print(f"The square of {number} is {squared_number}.")
    finally:
        print("Done.")             # runs whether an error happened or not

square_number()
