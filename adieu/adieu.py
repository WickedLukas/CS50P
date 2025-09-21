import inflect
import sys


def main():
    # Get names.
    names = get_names()

    # Convert names to an enumeration string.
    # names_enumeration = enumeration(names)
    p = inflect.engine()
    names_enumeration = p.join(names)

    print("Adieu, adieu, to", names_enumeration)


# Ask user for names until CTRL+D is pressed.
def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            return names

        if name != "":
            names.append(name)


# Convert a list of strings to an enumaration string.
def enumeration(strings):
    if len(strings) == 0:
        # Exit because no name was provided.
        sys.exit()

    result = ""
    result += strings[0]

    if len(strings) == 1:
        return result

    if len(strings) == 2:
        result += " and " + strings[1]
        return result
    else:
        for string in strings[1:-1]:
            result += ", " + string

    result += ", and " + strings[-1]

    return result


main()
