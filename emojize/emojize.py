import emoji

# Ask user for some text.
text = input("Input: ")

# Print emojized text from user including aliases.
print("Output: ", emoji.emojize(text, language='alias'))
