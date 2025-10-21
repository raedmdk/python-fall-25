# Raed Al Kiswani
# PE2 Module 2.1: Characters and Strings vs. Computers
# Program to convert between characters and ASCII values

def main():
    print("Welcome to the ASCII Value Finder!\n")

    # --- Part 1: Character to ASCII ---
    while True:
        user_input = input("Enter a single character: ")
        if len(user_input) == 1:  # validate one character only
            ascii_value = ord(user_input)
            print(f"The ASCII value of '{user_input}' is {ascii_value}.")
            break
        else:
            print("Please enter exactly one character.\n")

    # --- Part 2: ASCII to Character ---
    while True:
        try:
            ascii_number = int(input("\nEnter an ASCII value (32–127): "))
            if 32 <= ascii_number <= 127:
                character = chr(ascii_number)
                print(f"The character for ASCII value {ascii_number} is '{character}'.")
                break
            else:
                print("Please enter a number between 32 and 127.")
        except ValueError:
            print("That’s not a valid number. Try again.")

# Run program
if __name__ == "__main__":
    main()
