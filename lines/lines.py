import sys

# Check the number of command-line arguments.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments.")

# Get filepath.
filepath = sys.argv[1]

# Check if a python file was passed.
if not filepath.endswith(".py"):
    sys.exit("Not a python file.")

# Count the lines of code.
lines_of_code = 0
try:
    with open(filepath, "r") as file:
        for line in file:
            lstripped_line = line.lstrip()
            if lstripped_line and not lstripped_line.startswith("#"):
                lines_of_code += 1
except FileNotFoundError:
    sys.exit("File does not exist.")

# Output the lines of code.
print(lines_of_code)
