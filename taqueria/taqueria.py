menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    # Ask user for items until CTRL+D is pressed.
    try:
        item = input("Item: ").lower().title()
    except EOFError:
        break

    # Calculate the total for all items.
    try:
        total += menu[item]
    except KeyError:
        continue

    # Output total.
    print(f"Total: ${total:.2f}")
