def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Check if the license plate is valid.
def is_valid(s):
    if length_valid(s) and start_valid(s) and nums_valid(s) and chars_valid(s):
        return True
    else:
        return False


# Check if the length is between 2 and 6 characters.
def length_valid(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


# Check if the first two characters are alphabetic.
def start_valid(s):
    if s[:2].isalpha():
        return True
    else:
        return False


# Check if the decimal number positions are valid.
def nums_valid(s):
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i] == "0":
                return False
            elif i + 1 < len(s):
                for j in range(i+1, len(s)):
                    if not s[j].isdecimal():
                        return False
            break
    return True


# Check if characters are all alphanumeric.
def chars_valid(s):
    if s.isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()
