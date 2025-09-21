import string

# Ask user for a word in camel case.
camel_case = input("camelCase: ")

# Transform camel case to snake case.
snake_case = ""
pos = 0
for i in range(len(camel_case)):
    if camel_case[i] in string.ascii_uppercase:
        snake_case += camel_case[pos:i] + "_" + camel_case[i].lower()
        pos = i + 1

if pos < len(camel_case):
    snake_case += camel_case[pos:]

# Output the word in snake case.
print(snake_case)
