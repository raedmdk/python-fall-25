"""
PE2 Module 4.2: Processing Files - Option 1 Personal Diary

Student: Raed Kiswani
Course: ADD-100 Programming Logic
Instructor: Dr. Meri Kasprak

Program goal:
- Ask the user for a date, time, and diary entry.
- Append each entry to a text file named diary.txt (do not overwrite).
- Separate entries with a blank line so they are easy to read later.
- Use try/except so the program does not crash if there is a file error.
"""


def write_entry(file_name="diary.txt"):
    """
    Ask the user for one diary entry and append it to the diary file.

    Parameters:
        file_name (str): name of the text file to store diary entries.

    Returns:
        None
    """
    print("\nNew diary entry for today.")
    date = input("Date (example: 2025-11-19): ").strip()
    time = input("Time (example: 21:30): ").strip()
    mood = input("How are you feeling right now? ").strip()

    print("Write about your day (classes, Amazon shift, gym, anything):")
    entry_text = input("> ").strip()

    # Build one formatted block for this diary entry
    full_entry = (
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Mood: {mood}\n"
        "Entry:\n"
        f"{entry_text}\n"
        "\n"  # blank line between entries
    )

    try:
        # Open the file in append mode so we keep old entries
        with open(file_name, "a", encoding="utf-8") as diary_file:
            diary_file.write(full_entry)

        print(f"\nEntry saved to {file_name}.")
    except OSError as error:
        # Catch file-related errors (permissions, missing folder, etc.)
        print("There was a problem writing to the diary file.")
        print("System message:", error)


def main():
    """
    Main loop for Raed's personal diary program.

    Keeps asking the user if they want to add diary entries.
    """
    print("=== Raed's Personal Diary ===")
    print("Use this to track your day, classes, Amazon shifts, and mood.")

    while True:
        write_entry()

        again = input("\nAdd another entry right now? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nDiary updated. Goodbye.")
            break


# Only run main() when this file is executed directly
if __name__ == "__main__":
    main()
