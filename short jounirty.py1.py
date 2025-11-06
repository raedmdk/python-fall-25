"""
PE2 Module 3.2 – A Short Journey from Procedural to OOP
Program: Person class demo – Raed Al Kiswani

This program defines a simple Person class with name, address, age, and phone.
It then creates three Person objects (Raed, Abdulrahman, and Nasif)
and prints out their stored information.

Author: Raed Al Kiswani
Date: November 2025
"""

class Person:
    """Represents a person with basic contact information."""

    def __init__(self, name, address, age, phone):
        self._name = name
        self._address = address
        self._age = age
        self._phone = phone

    # --- Accessors (getters) ---
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    # --- Mutators (setters) ---
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

    # Display method for formatted output
    def display_info(self):
        print("Name   :", self._name)
        print("Address:", self._address)
        print("Age    :", self._age)
        print("Phone  :", self._phone)
        print("-" * 40)


def main():
    # Raed's information
    raed = Person("Raed Al Kiswani", "Crystal Lake, IL", 19, "224-493-5705")

    # Friends' information (same as past assignments)
    abdulrahman = Person("Abdulrahman Mohammed", "Algonquin, IL", 20, "555-870-3344")
    nasif = Person("Nasif Zaiton", "McHenry, IL", 19, "555-492-7712")

    print("People Information List")
    print("=" * 40)

    # Print info for each
    raed.display_info()
    abdulrahman.display_info()
    nasif.display_info()


# Run the program
if __name__ == "__main__":
    main()
