"""
PE2: Module 1.1 and 1.2 - Modules
Assignment: Number Guessing Game

Objective:
Use the random module to generate a random number between 1 and 100.
Let the user guess until they are correct.
Use abs() to see how close the guess is and print:
    - "Very Hot"  if difference is within 5
    - "Hot"       if difference is within 15
    - "Cool"      if difference is within 25
    - "Cold"      if difference is more than 25
Use a while loop and call main() at the bottom.

Student: Raed Al Kiswani
Course: ADD-100 Programming Logic
Date: (put your date here)

AI Use Disclosure:
Some parts of this file were written with help from ChatGPT (OpenAI).
I reviewed, tested, and edited the code so I understand how it works.
https://chat.openai.com/
"""

import random  # built-in module for random numbers


def get_feedback(difference):
    """
    Return a string showing how close the guess is.

    difference: absolute value of (guess - secret_number)
    """
    if difference <= 5:
        return "Very Hot"
    elif difference <= 15:
        return "Hot"
    elif difference <= 25:
        return "Cool"
    else:
        return "Cold"


def main():
    """Main game loop for the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it. I'll tell you if you're Very Hot, Hot, Cool, or Cold.\n")

    # random number between 1 and 100
    secret_number = random.randint(1, 100)

    guesses = 0
    guessed_correctly = False

    # keep looping until the user guesses the number
    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a whole number.\n")
            continue

        # optional: basic range check
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.\n")
            continue

        guesses += 1

        if guess == secret_number:
            print("\nYou got it! The number was:", secret_number)
            print("You needed", guesses, "guesses. Nice job!")
            guessed_correctly = True
        else:
            difference = abs(guess - secret_number)
            feedback = get_feedback(difference)
            print(feedback + "! Try again.\n")


# make sure main() runs when we start the program
if __name__ == "__main__":
    main()
