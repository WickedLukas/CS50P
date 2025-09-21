from validator_collection import validators, checkers, errors

# Get email address.
email_address = input("What's your email address? ")

# Check and print if email address is valid.
try:
    validators.email(email_address)
except ValueError:
    print("Invalid")
else:
    print("Valid")
