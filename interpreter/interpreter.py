# Ask user.
expression = input("Expression: ")

# Get values.
split_expression = expression.split()
if len(split_expression) == 3:
    x = float(split_expression[0])
    y = split_expression[1]
    z = float(split_expression[2])

# Calculate the result.
match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z
    case _:
        result = None

# Respond to user.
print(f"{result:.1f}")
