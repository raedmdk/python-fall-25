"""
PE2 Module 2.5 – Password Validator (Raed)
Goal: Practice strings, loops, and conditions while checking password strength.

Personal touches:
- Mentions Raed as the user.
- Simple, human-style messages (no advanced code).
- Uses only methods you’ve already learned (len, isupper, islower, isdigit, in, while, try/except).
"""

def main():
    print("Raed’s Password Checker")
    print("Make a strong password before your next Amazon night shift.\n")

    while True:
        try:
            password = input("Enter a new password: ")

            # Check all the rules
            if len(password) < 8 or len(password) > 20:
                print("Password must be 8–20 characters long.\n")
                continue

            if not any(ch.isupper() for ch in password):
                print("Add at least one uppercase letter.\n")
                continue

            if not any(ch.islower() for ch in password):
                print("Add at least one lowercase letter.\n")
                continue

            if not any(ch.isdigit() for ch in password):
                print("Add at least one number.\n")
                continue

            if not any(ch in "!@#$%&*" for ch in password):
                print("Add at least one symbol (!@#$%&*).\n")
                continue

            # Confirm password
            confirm = input("Re-enter your password to confirm: ")
            if confirm == password:
                print("\nPassword confirmed. Nice work, Raed — you’re all set.")
                break
            else:
                print("Passwords don’t match. Try again.\n")

        except Exception:
            print("Something went wrong. Try again.\n")

# Run program
main()
