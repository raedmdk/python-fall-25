"""
PE2 Module 3.4 – Object-Oriented Programming: Methods
Assignment: Pet Class Creation and Exploration

Student: Raed Al Kiswani
Course: Python Essentials 2
Date: 2025-11-10

This program shows:
- A simple Pet class that stores kind, breed, and name.
- Uses methods (getters, setters, and print_details).
- Creates three pets owned by Raed, Mohammed, and Ali.
- Demonstrates special built-in features: type(), isinstance(), and __name__.
"""

# Created by Raed — Python Essentials 2, MCC

class Pet:
    """A small class that stores information about a pet."""

    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    # Get methods
    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # Set methods
    def set_kind(self, new_kind):
        self.kind = new_kind

    def set_breed(self, new_breed):
        self.breed = new_breed

    def set_name(self, new_name):
        self.name = new_name

    # Method to print details
    def print_details(self):
        print("-----------------------------")
        print(f"Pet Name : {self.name}")
        print(f"Pet Kind : {self.kind}")
        print(f"Pet Breed: {self.breed}")
        print("-----------------------------\n")


def main():
    print("🐾 Raed’s Pet Detail Viewer — quick test before my Amazon night shift!\n")

    # Three pets from Raed, Mohammed, and Ali
    pet1 = Pet("Cat", "British Shorthair", "Messi")       # Raed's pet
    pet2 = Pet("Dog", "German Shepherd", "Rocky")         # Mohammed's pet
    pet3 = Pet("Bird", "Budgerigar", "Luna Blue")         # Ali's pet

    # Print details
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    # Change one of Ali’s pet details
    pet3.set_name("Luna Sky")
    pet3.set_breed("African Grey Parrot")
    print("Updated Ali’s pet details using setters:\n")
    pet3.print_details()

    # Special methods demonstrations
    print("Special Method Demonstrations:")
    print("Class name via __name__:", Pet.__name__)
    print("Type of pet1:", type(pet1))
    print("Is pet2 an instance of Pet?", isinstance(pet2, Pet))
    print("Is 'Messi' an instance of Pet?", isinstance('Messi', Pet))

    print("\nThanks for checking out my pets — time to feed Messi! 🐱")


if __name__ == "__main__":
    main()
