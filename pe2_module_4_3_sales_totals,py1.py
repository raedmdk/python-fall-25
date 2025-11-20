"""
PE2 Module 4.3 – Working with Real Files
Student: Raed Kiswani
Course: ADD-100 / Python Essentials 2

Assignment summary:
- Open sales_totals in read mode
- Read each line, strip newline, convert to float
- Add to a running total and count the lines
- Format and print each number
- Print the total, count, and average
- Use main() and try/except for errors

This version is Raed’s practice script for reading a real data file
and printing a clean money summary (something that could fit a small
side business or Amazon-paycheck-style report).
"""


def format_money(amount):
    """
    Take a float and return a string with commas and 2 decimals.
    Example: 13420.22 -> '13,420.22'
    """
    return f"{amount:,.2f}"


def main():
    filename = "sales_totals.txt"  # Make sure this matches the file name you downloaded

    try:
        total = 0.0
        count = 0

        print(f"Reading sales data from {filename}...\n")

        # Open file in read mode
        with open(filename, "r") as sales_file:
            for line in sales_file:
                # Strip newline and spaces
                clean_line = line.strip()

                # Skip empty lines just in case
                if clean_line == "":
                    continue

                # Convert to float
                amount = float(clean_line)

                # Update totals
                total += amount
                count += 1

                # Print each value formatted like money
                print(format_money(amount))

        # After the loop, check if we actually read anything
        if count > 0:
            average = total / count
        else:
            average = 0.0

        print("\n-------------------------------")
        print(f"Total: {format_money(total)}")
        print(f"Number of entries: {count}")
        print(f"Average: {format_money(average)}")

    except FileNotFoundError:
        print(f"Could not find the file '{filename}'.")
        print("Make sure sales_totals.txt is in the same folder as this program.")
    except ValueError:
        print("One of the lines in the file was not a valid number.")
        print("Check the data inside sales_totals.txt.")
    except Exception as error:
        print("An unexpected error happened:", error)


if __name__ == "__main__":
    main()
