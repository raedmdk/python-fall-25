"""
PE1 4.3 – Simple Interest Calculator
Author: Raed Al Kiswani
Date: September 30, 2025

This program calculates simple interest using a function
that returns the result. The main() function controls the program.
"""

# function to calculate simple interest
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# main function
def main():
    # Raed-style prompts
    principal = float(input("Raed, how much money are you putting in? "))
    rate = float(input("What interest rate (%) are you getting? "))
    time = float(input("How many years do you want to wait? "))

    # call the function
    interest = calculate_interest(principal, rate, time)

    # print result
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
    print("Not bad, maybe I need more Amazon shifts")

# run program
main()
