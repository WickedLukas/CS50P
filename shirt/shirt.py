import sys
from PIL import Image, ImageOps

# Check the number of command-line arguments.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments.")

# Get filepaths.
input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

# Check the input and output filenames.
input_filepath_lower = input_filepath.lower()
output_filepath_lower = output_filepath.lower()
for filepath in [input_filepath_lower, output_filepath_lower]:
    if not (filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".png")):
        sys.exit("Invalid input or output extensions.")

if input_filepath_lower.split(".")[-1] != output_filepath_lower.split(".")[-1]:
    sys.exit("Input and output have different extensions.")

# Load input image.
try:
    with Image.open(input_filepath, "r") as input_image:
        input_image = input_image.copy()
except FileNotFoundError:
    sys.exit(f"{input_filepath} file does not exist.")

# Load shirt image.
shirt_filepath = "shirt.png"
try:
    with Image.open(shirt_filepath, "r") as shirt_image:
        shirt_image = shirt_image.copy()
except FileNotFoundError:
    sys.exit(f"{shirt_filepath} file does not exist.")

# Crop input image to fit shirt image.
image = ImageOps.fit(input_image, shirt_image.size)

# Paste shirt image into the cropped input image.
image.paste(shirt_image, shirt_image)

# Save image.
image.save(output_filepath)
