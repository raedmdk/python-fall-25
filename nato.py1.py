"""
PE1 4.6.B – Dictionaries: NATO Phonetic Alphabet
Author: Raed Al Kiswani
Date: October 7, 2025

Goal:
- Use a global dictionary (NATO_ALPHABET) to map letters to code words.
- Ask the user for a word, convert to UPPERCASE, and print each letter's code.
- Keep it simple and at PE1 level.
"""

# ===== Global constant dictionary (A–Z) =====
NATO_ALPHABET = {
    "A": "Alpha",   "B": "Bravo",    "C": "Charlie", "D": "Delta",   "E": "Echo",
    "F": "Foxtrot", "G": "Golf",     "H": "Hotel",   "I": "India",   "J": "Juliett",
    "K": "Kilo",    "L": "Lima",     "M": "Mike",    "N": "November","O": "Oscar",
    "P": "Papa",    "Q": "Quebec",   "R": "Romeo",   "S": "Sierra",  "T": "Tango",
    "U": "Uniform", "V": "Victor",   "W": "Whiskey", "X": "X-ray",   "Y": "Yankee",
    "Z": "Zulu"
}

# ----- Function: prompt, convert, and spell with dictionary -----
def spell_nato():
    word = input("Enter a word to spell with NATO: ")
    word_upper = word.upper()  # convert to uppercase once

    print("\nNATO spelling:")
    for ch in word_upper:
        if ch in NATO_ALPHABET:          # letter A–Z
            print(NATO_ALPHABET[ch])
        elif ch == " ":                   # skip spaces cleanly
            print("(space)")
        else:                             # any other character
            print("(ignored:", ch + ")")

# ----- Main entry point -----
def main():
    spell_nato()

# Run the program
main()
