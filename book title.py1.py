# Raed Al Kiswani
# PE2 Module 2.4 - Strings in Action and List Methods
# Program to collect 10 book titles, capitalize them, and sort the list

def main():
    print("Welcome to the Book Titles Collector!")
    print("You'll enter 10 book titles below.\n")

    books = []  # empty list to store book titles
    count = 0

    # ask the user for 10 titles
    while count < 10:
        title = input(f"Enter the title for book {count + 1}: ")
        title = title.title()  # capitalize each word
        books.append(title)
        count += 1

    # create a sorted copy of the list
    books_sorted = sorted(books)

    print("\nHere are your book titles in alphabetical order:")
    for book in books_sorted:
        print(book)

# run the program
if __name__ == "__main__":
    main()
