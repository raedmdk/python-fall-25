"""
PE2 Module 3.5.1.1 – OOP Fundamentals: Inheritance
Student: Raed Al Kiswani
Course: Python Essentials 2 (MCC)
Date: 2025-11-10

Goal:
- Define an Employee superclass (name, number)
- Define a ProductionWorker subclass (shift number, hourly pay rate)
- Use getters and setters
- Prompt the user for a worker and display details

Personal touches:
- Uses names from my class examples: Raed, Mohammed, Ali
- Simple, readable prompts (no advanced Python)
"""

# -------------------------------
# Superclass: Employee
# -------------------------------
class Employee:
    def __init__(self, name="", number=""):
        self.__name = name
        self.__number = number

    # getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # setters
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        return f"Name: {self.__name}\nEmployee Number: {self.__number}"


# -------------------------------
# Subclass: ProductionWorker
#   shift: 1 (Day) or 2 (Night)
#   pay_rate: hourly pay as float
# -------------------------------
class ProductionWorker(Employee):
    def __init__(self, name="", number="", shift=1, pay_rate=0.0):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    # getters
    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate

    # setters
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def shift_label(self):
        # 1 = Day, 2 = Night (anything else → Unknown)
        if self.__shift == 1:
            return "Day"
        if self.__shift == 2:
            return "Night"
        return "Unknown"

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Shift: {self.shift_label()}\n"
            f"Pay Rate: {self.__pay_rate}"
        )


# -------------------------------
# Small helpers (simple, not fancy)
# -------------------------------
def read_int(prompt):
    text = input(prompt).strip()
    if text == "":
        return None
    return int(text)

def read_float(prompt):
    text = input(prompt).strip()
    if text == "":
        return None
    return float(text)


# -------------------------------
# Main demo
# -------------------------------
def main():
    print("\n--- Production Worker Entry (Raed) ---")
    # Ask the user for one worker (as required by assignment)
    name = input("Enter Employee Name (e.g., Raed): ").strip()
    number = input("Enter Employee Number (e.g., 42): ").strip()

    print("Shift Number: 1 = Day, 2 = Night")
    try:
        shift = read_int("Enter Shift Number (1 or 2): ")
    except ValueError:
        shift = 1  # simple default, keep it basic

    try:
        pay_rate = read_float("Enter Pay Rate (e.g., 20.75): ")
    except ValueError:
        pay_rate = 0.0

    # Fallback defaults if user left anything blank
    if name == "":
        name = "Raed"
    if number == "":
        number = "1001"
    if shift not in (1, 2):
        shift = 1
    if pay_rate is None:
        pay_rate = 0.0

    worker = ProductionWorker(name, number, shift, pay_rate)

    print("\n--- Details of Employee (You Entered) ---")
    print(worker)

    # Two quick sample objects to show understanding (Mohammed & Ali).
    # These are not required by the prompt but help demonstrate usage.
    print("\n--- Sample Workers (Personalized Examples) ---")
    mohammed = ProductionWorker("Mohammed", "1002", 2, 21.50)
    ali = ProductionWorker("Ali", "1003", 1, 19.25)

    print("\nMohammed:")
    print(mohammed)

    print("\nAli:")
    print(ali)
    print("\nDone.\n")


if __name__ == "__main__":
    main()
