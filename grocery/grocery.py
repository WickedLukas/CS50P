def main():
    # Get items.
    items = get_items()

    # Make grocery list.
    grocery_list = make_grocery_list(items)

    # Output grocery list.
    for element in grocery_list:
        print(element["count"], element["item"])


# Get items from user until CTRL+D is pressed.
def get_items():
    items = []
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            return items

        items.append(item)


# Make grocery list containing alphabatically sorted items and item counts.
def make_grocery_list(items):
    # Sort list of items alphabetically.
    items = sorted(items)

    grocery_list = []
    if len(items) == 0:
        return grocery_list

    grocery_list.append({"item": items[0], "count": 1})
    last_item = items[0]

    if len(items) == 1:
        return grocery_list

    for item in items[1:]:
        if item != last_item:
            grocery_list.append({"item": item, "count": 1})
            last_item = item
        else:
            grocery_list[-1]["count"] += 1

    return grocery_list


main()
