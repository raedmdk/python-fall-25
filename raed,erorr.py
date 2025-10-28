"""
PE2 Module 2.6 – Errors: Raed's mini calculator
Goal: Practice try/except by catching common input errors.

Personal touches:
- Prompts mention Raed, night Amazon shifts, and studying data science.
- Keeps language simple and human. No advanced Python features.
"""

def main():
    print("Raed's quick calculator")
    print("Use this to check small math while studying data science or before an Amazon night shift.\n")

    while True:
        # Get first number
        try:
            first_text = input("Enter the first number: ")
            a = float(first_text)  # may raise ValueError
        except ValueError:
            print("That first value isn't a number. Try something like 7 or 12.5.\n")
            continue

        # Get operator
        op = input("Pick an operation (+, -, *, /): ").strip()
        if op not in ["+", "-", "*", "/"]:
            print("Please choose only +, -, *, or /.\n")
            continue

        # Get second number (catch zero-division later)
        try:
            second_text = input("Enter the second number: ")
            b = float(second_text)
        except ValueError:
            print("That second value isn't a number. Try again.\n")
            continue

        # Do the math with error handling for division by zero
        try:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            else:  # op == "/"
                result = a / b  # may raise ZeroDivisionError

            # Show result
            print(f"Result: {a} {op} {b} = {result}\n")

        except ZeroDivisionError:
            print("You tried to divide by 0. Use another number for the second value.\n")

        # Ask to continue
        again = input("Do you want another quick calc? (yes/no): ").strip().lower()
        if again != "yes":
            print("All set. Good luck with classes and shifts.")
            break


# Run the program
main()
