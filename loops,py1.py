"""
PE1 3.2B: For Loops in Python
Task: Print all numbers divisible by 7 from 1 to 300 (inclusive).
This solution uses a for loop with range() and the modulus (%) operator.
"""

start, end = 1, 300

for n in range(start, end + 1):
    # If n is divisible by 7, the remainder is 0
    if n % 7 == 0:
        print(n)

# TODO: (optional) Let the user enter a custom start/end range.
