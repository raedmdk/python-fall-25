"""
Raed Al Kiswani
PE1 3.6 — Ticket Sales (lists)

i imagined this as an open mic night (20 seats).
also i usually go for the middle seats so i can see better :)
not trying to be fancy here. just:
- start with seats 1..20
- ask for a seat number
- remove it if valid
- 0 means done
"""

# make the seats list (1 through 20)
chairs = list(range(1, 21))  # available seats (renamed from seats just for fun)

print("welcome to my little ticket app (soccer vibes).")
print("available seats right now:")
print(chairs)

# loop until user quits or no seats left
while True:
    if len(chairs) == 0:
        print("no seats left. sold out.")
        break

    raw = input("\npick a seat 1-20 (0 = done): ").strip()

    if raw == "":
        print("please type a number.")
        continue

    try:
        choice = int(raw)
    except ValueError:
        print("hmm, that didn’t look like a number.")  # casual error tone
        continue

    if choice == 0:
        print("ok cool, done for now.")  # casual goodbye
        break

    if choice < 1 or choice > 20:
        print("out of range. choose 1..20.")
        continue

    if choice not in chairs:
        print("yo that seat is gone, try another.")  # slangy personal line
        print("available now:", chairs)
        continue

    chairs.remove(choice)   # list.remove(x)
    print(f"seat {choice} purchased.")

    # show what changed
    print("available now:", chairs)

# summary
sold = 20 - len(chairs)
print(f"\nsummary -> sold: {sold}, left: {len(chairs)}")

# tiny personal note
print("note: i made this thinking about picking seats for an open mic night with friends.")

# why this works (short explanation)
print("why this works: i check 'in' to see if a seat is open,")
print("and i use list.remove() to delete it. [:] would make a copy if i needed one.")
