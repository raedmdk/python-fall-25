"""
PE2 Modules 2.7 & 2.8 – Handling list exceptions (Raed)
Goal: Practice catching ValueError and IndexError while editing a list.

Personal touches:
- Includes Raed’s favorite artists Abdulrahman Mohammed and Nasif Zaiton.
- Written in simple, natural student language.
"""

def show_artists(artists):
    """Print the list with indexes so the user knows which number to enter."""
    print("\nTop artists list (index : name):")
    for i in range(len(artists)):
        print(f"{i} : {artists[i]}")
    print()

def replace_artist(artists):
    """
    Ask for an index and a new name.
    If the index is not a valid number (ValueError) OR out of range (IndexError),
    show a general message and keep running.
    """
    try:
        index_text = input("Enter the index of the artist to replace: ")
        index = int(index_text)  # may raise ValueError
        new_name = input("Enter the new artist name: ").strip()
        artists[index] = new_name  # may raise IndexError
        print("\nUpdated list:")
        show_artists(artists)

    except (ValueError, IndexError):
        print("\nAn input error occurred. Please enter a valid number in range.\n")

def main():
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Abdulrahman Mohammed",
        "Nasif Zaiton", "Elvis Presley", "Mariah Carey", "Stevie Wonder",
        "Michael Jackson", "Rihanna"
    ]

    print("Raed’s Top Artists Editor")
    print("Simple program to practice exception handling and update a top artists list.\n")

    show_artists(top_artists)

    while True:
        replace_artist(top_artists)
        again = input("Do you want to replace another? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nDone. Here’s your final list:")
            show_artists(top_artists)
            print("All changes saved successfully.")
            break

# Run program
main()
