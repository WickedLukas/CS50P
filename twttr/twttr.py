vowels = "aeiouAEIOU"

# Ask the user for text.
text = input("Input: ")

# Remove all vowels from text.
for v in vowels:
    text = text.replace(v, "")

# Output text without vowels.
print(text)
