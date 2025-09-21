# Ask user.
greeting = input("Greeting: ").lstrip().lower()

# Respond to user.
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
