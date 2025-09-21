def main():
    # Ask the user for text.
    text = input("Input: ")

    # Shorten text.
    short_text = shorten(text)

    # Output short text.
    print(short_text)


# Shorten text by removing all vowels.
def shorten(text):
    vowels = "aeiouAEIOU"
    for v in vowels:
        text = text.replace(v, "")

    return text


if __name__ == "__main__":
    main()
