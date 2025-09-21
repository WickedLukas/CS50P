def main():
    # Take input text from user.
    text = input()

    # Print text with emoticons.
    print(convert(text))


# Return str where ":)" is replaced with "🙂" and ":(" is replaced with "🙁".
def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()
