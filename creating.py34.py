"""
PE1 4.5 – Creating and Organizing Functions (Recursion)
Author: Raed Al Kiswani
Date: October 7, 2025

Goal:
Use recursion to calculate the factorial of a number.
Practice writing tidy, organized code with functions.
"""

# Recursive factorial function
def factorial(n):
    """Return factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main function
def main():
    """Main program to get user input and show factorial."""
    print("Welcome to Raed’s factorial finder!")
    try:
        num = int(input("Enter a non-negative number: "))
        if num < 0:
            print("Sorry, negative numbers don’t work here.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
    except ValueError:
        print("That’s not a number — try again with digits only.")

# Run program
main()
