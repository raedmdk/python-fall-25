"""
PE2 Module 4.5 – The datetime module
Student: Raed Al Kiswani
Course: ADD-100 (Programming Logic)

Assignment: Age Calculator
- Ask the user for their birthday.
- Use datetime to calculate age in days, years, months, weeks, hours, and minutes.
- Explain each line that does time calculation with comments.
"""

import datetime  # import the datetime module so we can work with dates


def main():
    """Main function that gets the birthday and prints age in different units."""
    print("Raed's late-night age calculator")
    print("For those nights when you're coding late and wondering how old you really are.\n")

    # Get birthday input from the user
    try:
        birth_year = int(input("What year were you born? "))
        birth_month = int(input("What month were you born (as a number, e.g. May = 5)? "))
        birth_day = int(input("What day of the month were you born? "))
    except ValueError:
        # This runs if the user types something that is not a whole number
        print("Please use only numbers for year, month, and day.")
        return

    # Build a real date from the pieces the user typed
    try:
        raed_birthday = datetime.date(birth_year, birth_month, birth_day)
    except ValueError:
        # This runs if the combination of year, month, day is not a real calendar date
        print("That is not a valid date. Please check the day and month.")
        return

    print("\nYour birthday is:")
    print(raed_birthday)

    # Get today's date from the system clock
    today = datetime.date.today()

    # Calculate the difference between today and the birthday
    # This gives us a timedelta object
    difference = today - raed_birthday

    # Pull the total number of days out of the timedelta
    days_old = difference.days
    print(f"\nThe difference is {days_old} days")

    # TIME CALCULATIONS (each line is explained)

    # Years (approx): divide days by 365.25 to account for leap years roughly
    years_old = days_old / 365.25

    # Months (approx): 1 year is about 12 months
    months_old = years_old * 12

    # Weeks: 1 week is exactly 7 days
    weeks_old = days_old / 7

    # Hours: 1 day is 24 hours
    hours_old = days_old * 24

    # Minutes: 1 hour is 60 minutes
    minutes_old = hours_old * 60

    # Print everything in a friendly format
    print(f"You are about {years_old:.1f} years old.")
    print(f"Months (approx): {months_old:.1f}")
    print(f"Weeks (approx): {weeks_old:.1f}")
    print(f"Hours (approx): {hours_old:,}")
    print(f"Minutes (approx): {minutes_old:,}")

    print("\nThanks for using my age calculator. - Raed")


# Only run main() when this file is executed directly, not when imported
if __name__ == "__main__":
    main()
