"""
PE1 3.1 A: Evaluating Expressions and Making Decisions in Python

This program:
- Prompts the user for their age (integer).
- Checks if they are old enough to drive, vote, buy alcohol legally, and qualify for a senior discount.
- Prints clear, user-friendly results for each check.

Assumptions (common U.S. thresholds):
- Drive: 16+
- Vote: 18+
- Buy alcohol: 21+
- Senior discount: 65+

Handles edge cases: negative ages, non-integer input, and ages exactly at each threshold.
"""

DRIVE_AGE = 16
VOTE_AGE = 18
ALCOHOL_AGE = 21
SENIOR_AGE = 65

def read_age() -> int:
    """Read and validate an integer age from the user."""
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            # Optional sanity cap to catch typos
            if age > 120:
                print("That age seems unrealistic. Please enter a valid age (0–120).")
                continue
            return age
        except ValueError:
            print("Please enter a whole number (e.g., 0, 16, 21, 65).")

def main():
    age = read_age()

    # Drive
    if age >= DRIVE_AGE:
        print("You are old enough to drive.")
    else:
        print("You are not old enough to drive.")

    # Vote
    if age >= VOTE_AGE:
        print("You can vote.")
    else:
        print("You cannot vote yet.")

    # Buy alcohol
    if age >= ALCOHOL_AGE:
        print("You can buy alcohol legally.")
    else:
        print("You cannot buy alcohol legally yet.")

    # Senior discount
    if age >= SENIOR_AGE:
        print("You are eligible for the senior discount.")
    else:
        print("You are not eligible for the senior discount.")

    # TODO: If needed, adjust driving age for your specific state’s rules.

if __name__ == "__main__":
    main()
