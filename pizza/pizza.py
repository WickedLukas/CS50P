import csv
import sys

from tabulate import tabulate

# Check the number of command-line arguments.
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments.")

# Get filepath.
filepath = sys.argv[1]

# Check if a csv file was passed.
if not filepath.endswith(".csv"):
    sys.exit("Not a csv file.")

# Print the csv file in grid-format using tabulate.
try:
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist.")
