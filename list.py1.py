"""
PE1 3.7 – Daily Heart Rate Tracker
Author: Raed Al Kiswani
Date: September 23, 2025

Goal:
This program asks me to enter my heart rate (BPM) at different times of the day.
It saves the times and numbers together in a multi-level list.
Then it prints each reading and shows the average for the day.
"""

# 1) Time slots (I picked ones that match my day)
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# 2) List to hold results and total for average
heart_rates = []
total_bpm = 0

# 3) Collect inputs from me
for slot in time_slots:
    bpm = int(input(f"Raed, enter your heart rate (BPM) in the {slot}: "))

    # simple check so I don't type something impossible
    while bpm < 40 or bpm > 200:
        print("That doesn't look right. Try again with a number between 40 and 200.")
        bpm = int(input(f"Enter your heart rate (BPM) in the {slot}: "))

    heart_rates.append([slot, bpm])

# 4) Print the results
print("\n--- Raed's Daily Heart Rate Readings ---")
for pair in heart_rates:
    print(f"At {pair[0]} my heart rate was {pair[1]} BPM")
    total_bpm = total_bpm + pair[1]

# 5) Average
average_bpm = total_bpm / len(heart_rates)
print(f"\nMy average heart rate today: {average_bpm:.2f} BPM")

# 6) A tiny note based on the average (optional but shows if/else)
if average_bpm > 90:
    print("Note: My average is a little on the high side today.")
elif average_bpm < 55:
    print("Note: My average is pretty low today.")
else:
    print("My average heart rate looks normal.")
