"""
PE2 Module 4.1 – Generators, iterators, and closures
Student: Raed Al Kiswani
Course: Python Essentials 2 (MCC)
Date: 2025-11-19

Goal:
- Write a generator that yields all two-letter combinations from a given list of characters.
- Use a simple 5-letter original list.
- Keep the code readable and at class level (no advanced features).

Personal touch:
- Default character list uses letters from "RAED" + "M" (for Mohammed): ['r','a','e','d','m'].
"""

from typing import Iterable, Generator  # type hints are optional but clear


def two_letter_combinations(characters: Iterable[str]) -> Generator[str, None, None]:
    """
    Generator that yields two-letter combos (e.g., 'aa', 'ab', ...).

    characters: an iterable of single-character strings
    yields: each two-letter combination as a string
    """
    # Basic validation (kept simple)
    chars = list(characters)
    for ch in chars:
        if not isinstance(ch, str) or len(ch) != 1:
            # Keep the message friendly for your class level
            raise ValueError("All items must be single-character strings (e.g., 'a').")

    # Nested loops to create every pair (including same-letter pairs)
    for c1 in chars:
        for c2 in chars:
            # yield pauses and hands back one combo at a time
            yield c1 + c2


def main():
    print("Two-Letter Combinations (Generator Demo)\n")

    # Original 5-letter list (personalized to you)
    letters = ['r', 'a', 'e', 'd', 'm']

    try:
        # Use the generator and print results
        count = 0
        for combo in two_letter_combinations(letters):
            print(combo, end="  ")
            count += 1
            # new line every 10 items to keep output tidy
            if count % 10 == 0:
                print()
        if count % 10 != 0:
            print()  # final newline
        print(f"\nTotal combos: {count}")  # should be 25 for 5×5

    except ValueError as err:
        # Simple, clear error message if list has a bad entry
        print("Input error:", err)


if __name__ == "__main__":
    main()
