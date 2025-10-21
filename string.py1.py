# Raed Al Kiswani
# PE2 Module 2.2 - Strings Practice
# practicing different string functions for class

# testing escape sequences
print("This is line one\nThis is line two")
print("Tab\tspace works too")
print("I said \"Need more sleep\" after studying Data Science")

# multiline string
multi_line = """This week:
- Work at Amazon
- Classes at MCC
- Study Python
"""
print(multi_line)

# concatenation and replication
greeting = "Hello"
name = "Raed"
full_sentence = greeting + " " + name
print(full_sentence)

repeat_line = "Coding is fun! " * 2
print(repeat_line)

# iterating through a string
for letter in "Data":
    print(letter)

# using len(), max(), min()
text = "pythonrocks"
print("Length:", len(text))
print("Max character:", max(text))
print("Min character:", min(text))

# using index() and count()
word = "mississippi"
print("Index of first 's':", word.index("s"))
print("Count of 'i':", word.count("i"))

# converting a string to a list
letters = list("Raed")
print(letters)

# slicing examples
course = "Data Science"
print(course[0:4])   # prints Data
print(course[-7:])   # prints Science

# using 'in' and 'not in'
print("Data" in course)
print("Sleep" not in course)

# showing string immutability (creating a new one instead)
original = "Python"
new_version = "J" + original[1:]
print(new_version)
# testing this late night after work lol
