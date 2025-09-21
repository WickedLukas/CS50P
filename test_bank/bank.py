def main():
    # Get greeting.
    greeting = input("Greeting: ")

    # Get dollar amount for greeting.
    amount = value(greeting)

    # Output dollar amount.
    print(f"${amount}")


# Get dollar amount for greeting.
def value(greeting):
    greeting = greeting.lstrip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
