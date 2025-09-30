"""
PE1 4.2 – My Madlib Song
Author: Raed Al Kiswani
Date: September 30, 2025

This program makes a custom Happy Birthday song.
It collects 8 words from the user and puts them into the song.
"""

# define the function with 8 parameters
def custom_song(name, age, place, food, color, object1, hobby, feeling):
    print("\n--- My Happy Birthday Madlib ---\n")
    print("Happy Birthday to " + name + "!")
    print("Today you turn " + str(age) + " and everyone at " + place + " is here.")
    print("We all brought " + food + " and a big cake too.")
    print("Your " + color + " " + object1 + " is buzzing with texts all day long.")
    print("After the party, we will play " + hobby + ".")
    print("Everyone feels " + feeling + " and sings: Happy Birthday " + name + "!")

# collect user input
user_name = input("Enter a name: ")
user_age = input("Enter an age: ")
user_place = input("Enter a place: ")
user_food = input("Enter a favorite food: ")
user_color = input("Enter a color: ")
user_object1 = input("Enter an object: ")
user_hobby = input("Enter a hobby: ")
user_feeling = input("Enter a feeling: ")

# call the function with named arguments
custom_song(
    name=user_name,
    age=user_age,
    place=user_place,
    food=user_food,
    color=user_color,
    object1=user_object1,
    hobby=user_hobby,
    feeling=user_feeling
)
