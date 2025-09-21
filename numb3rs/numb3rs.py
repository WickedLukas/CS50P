import re
import sys


def main():
    # Ask user for IP address and output if it is valid.
    print(validate(input("IPv4 Address: ")))


# Check weather the IP address is valid.
def validate(ip):
    # Pattern for matching numbers between 0 and 255.
    pattern_0_255 = r"((?:25[0-5])" \
                    + r"|(?:2[0-4][0-9])" \
                    + r"|(?:1[0-9][0-9])" \
                    + r"|(?:[1-9][0-9])" \
                    + r"|(?:[0-9]))"
    pattern = r"^(?:" + pattern_0_255 + r"\.){3}" + pattern_0_255 + r"$"
    if re.search(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
