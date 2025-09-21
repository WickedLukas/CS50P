from pyfiglet import Figlet, FontNotFound
import random
import sys

figlet = Figlet()
if len(sys.argv) == 1:
    # Pick random font.
    fonts = figlet.getFonts()
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    # Parse command line arguments for font.
    if not (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        sys.exit("The first argument needs to be '-f' or '--font'.")

    f = sys.argv[2]
else:
    sys.exit("Only zero or two arguments are supported!")

# Set font.
try:
    figlet.setFont(font=f)
except FontNotFound:
    sys.exit("Unknown font!")

# Ask user for text.
text = input("Input: ")

# Print text is ASCII art font.
print("Output:\n" + figlet.renderText(text))
