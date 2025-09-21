import csv
import sys

# Check the number of command-line arguments.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments.")

# Get filepaths.
read_filepath = sys.argv[1]
write_filepath = sys.argv[2]

# Read csv file containing "name" and "house" columns.
read_rows = []
try:
    with open(read_filepath, "r") as read_file:
        read_rows = list(csv.DictReader(read_file, ["name", "house"]))
except Exception:
    sys.exit(f"Could not read {read_filepath}.")

# Create list of dictonaries containing "first", "last" and "house" columns.
write_rows = []
for read_row in read_rows[1:]:
    last, first = read_row["name"].split(", ")
    house = read_row["house"]

    write_rows.append({"first": first, "last": last, "house": house})

# Write csv file containing "first", "last" and "house" columns.
try:
    with open(write_filepath, "w") as write_file:
        writer = csv.DictWriter(write_file, ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(write_rows)
except Exception:
    sys.exit(f"Could not write {write_filepath}.")
