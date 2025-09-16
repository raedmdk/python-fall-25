"""
PE1 3.3.A: Logical Operations
Objective:
- Prompt the user for TWO DISTINCT integers.
- Demonstrate logical operators: and, or, not (2 examples each).
- Print the logical statement and its result for each comparison.

Notes:
- Includes input validation (integers only) and re-prompt until numbers are distinct.
- Uses clear f-string outputs so the expression and its boolean result are visible.
"""

def read_int(prompt: str) -> int:
    """Read an integer from input, reprompting on invalid entries."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def read_two_distinct_ints() -> tuple[int, int]:
    """Prompt user for two DISTINCT integers."""
    a = read_int("Enter an integer: ")
    b = read_int("Enter another (distinct) integer: ")
    while b == a:
        print("Numbers must be distinct. Please enter a different value.")
        b = read_int("Enter a different integer: ")
    return a, b

def main():
    print("=== Logical Operations Demo (and / or / not) ===")
    n1, n2 = read_two_distinct_ints()

    print("\nAND examples")
    expr1 = (n1 > 0) and (n2 > 0)
    print(f"({n1} > 0) AND ({n2} > 0) -> {expr1}")

    expr2 = (n1 % 2 == 0) and (n2 % 2 == 0)
    print(f"({n1} % 2 == 0) AND ({n2} % 2 == 0) -> {expr2}")

    print("\nOR examples")
    expr3 = (n1 % 7 == 0) or (n2 % 7 == 0)
    print(f"({n1} % 7 == 0) OR ({n2} % 7 == 0) -> {expr3}")

    expr4 = (n1 > 100) or (n2 > 100)
    print(f"({n1} > 100) OR ({n2} > 100) -> {expr4}")

    print("\nNOT examples")
    # NOT example 1: n1 is not even (i.e., n1 is odd)
    expr5 = not (n1 % 2 == 0)
    print(f"NOT ({n1} % 2 == 0) -> {expr5}   # True means n1 is odd")

    # NOT example 2: n2 is NOT between 10 and 50 (inclusive)
    expr6 = not (10 <= n2 <= 50)
    print(f"NOT (10 <= {n2} <= 50) -> {expr6}")

    print("\nDone. Review each line to see the logical statement and its boolean result.")
    # TODO: Extend: Add more comparisons or explain each result in plain English.

if __name__ == "__main__":
    main()
