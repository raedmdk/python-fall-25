"""
PE1 3.2A: While Statements in Python
Assignment: 99 Bottles of Beer on the Wall

This program prints the lyrics to the song
"99 Bottles of Beer on the Wall" using a while loop.
It handles the singular/plural form of 'bottle' and ends when no bottles remain.
"""

# Start with 99 bottles
bottles = 99

# Run the loop until there are no bottles left
while bottles > 0:
    # Handle plural vs singular
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
    else:  # last bottle
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")
        print("Take it down, pass it around")

    # Decrease count
    bottles -= 1

    # Print the next line after taking one down
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall!\n")
    elif bottles == 1:
        print(f"{bottles} bottle of beer on the wall!\n")
    else:
        print("No bottles of beer on the wall!\n")

# TODO: Later enhancement – let the user choose the starting number of bottles
