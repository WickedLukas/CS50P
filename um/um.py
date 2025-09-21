import re


def main():
    # Output the number of "um" which are not part of another word.
    print(count(input("Text: ")))


# Count the number of "um" which are not part of another word.
def count(s):
    pattern = r"(?:(?<=[^a-z])|(?<=^))(um)(?:(?=[^a-z])|(?<=$))"
    if matches := re.findall(pattern, s, re.IGNORECASE):
        return len(matches)

    return 0


if __name__ == "__main__":
    main()
