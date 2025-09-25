# PE1 3.4 – Steps Tracker
# Author: Raed Al Kiswani
# Date: September 23, 2025

# A list of all days in the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# An empty list where I will store steps
steps = []

# Ask for steps each day and add them to the list
for d in days:
    s = int(input("How many steps did you take on " + d + "? "))
    steps.append(s)

# Show daily steps
print("\n--- my weekly steps ---")
for i in range(len(days)):
    print(days[i] + ": " + str(steps[i]))

# Find total steps
total = 0
for n in steps:
    total = total + n

# Find average steps
average = total / len(steps)

# Show results
print("Total steps:", total)
print("Average steps:", int(average))
