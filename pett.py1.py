"""
PE2 Module 3.3 – OOP: Properties
Assignment: Veterinary Office Pet System

Student: Raed Al Kiswani
Course: Python Essentials 2
Date: 2025-11-10

What this program does:
- Defines a Pet class with private properties and simple getters/setters.
- Uses a class variable for the vet office name (personalized to Raed).
- Creates at least 3 Pet objects (uses Raed, Mohammed, Ali).
- Shows property updates using setters.
- Uses hasattr() (with name-mangling aware check) to verify property existence.
- Prints pet details in a human, simple way.

Nothing advanced is used. The code is kept plain and readable.
"""

class Pet:
    """Simple Pet class for a veterinary office record."""

    # Class variable shared by all pets
    vet_name = "raed"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Private (name-mangled) instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # ----- Getters -----
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    # ----- Setters -----
    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # ----- Display -----
    def display_pet_info(self):
        print("----- Pet Record -----")
        print(f"Vet Office: {Pet.vet_name}")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print("----------------------\n")


def check_property(pet_obj, public_attr_name):
    """
    Check if a private property exists on a Pet object using hasattr().
    Because we used double underscores in the class (e.g., __pet_name),
    Python name-mangles them to _Pet__pet_name. This helper builds that name.
    Returns True/False.
    """
    mangled = f"_Pet__{public_attr_name}"
    return hasattr(pet_obj, mangled)


def main():
    print("Raed’s Pet Record System – quick demo (plain and simple).")
    print("This script shows class variable, private properties, setters, and hasattr().\n")

    # Create three pets (personalized)
    # 1) Raed’s pet: Messi
    pet1 = Pet(owner_first_name="Raed", owner_last_name="Kiswani",
               pet_id="P1001", pet_name="Messi", pet_type="Cat")

    # 2) Mohammed’s pet
    pet2 = Pet(owner_first_name="Mohammed", owner_last_name="Saleh",
               pet_id="P1002", pet_name="Bolt", pet_type="Dog")

    # 3) Ali’s pet
    pet3 = Pet(owner_first_name="Ali", owner_last_name="Zaiton",
               pet_id="P1003", pet_name="Luna", pet_type="Parrot")

    # Show two examples of display_pet_info on different instances
    pet1.display_pet_info()
    pet2.display_pet_info()

    # Use a setter at least once (change Ali’s pet type)
    pet3.set_pet_type("Bird")
    print("Updated Ali’s pet type using a setter:")
    pet3.display_pet_info()

    # Show three examples of check_property on various properties/pets
    print("Property checks with hasattr():")
    print("pet1 has owner_first_name? ->", check_property(pet1, "owner_first_name"))
    print("pet2 has pet_name? ->", check_property(pet2, "pet_name"))
    print("pet3 has middle_name? ->", check_property(pet3, "middle_name"))  # expected False
    print()

    print("Thanks for visiting Raed’s vet office. Take care of your pets!\n")


# Run the program
if __name__ == "__main__":
    main()
