# import json
import requests
import sys

# Check the number of command-line arguments.
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument.")

# Get the number of bitcoins from the command line.
try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number.")

# Query the CoinCap API for bitcoin.
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="
                            + "b462d3b5f48c5272deec4f38991bd6c15a69aaec7c62f25e23d01a8a133fa49b")
    response.raise_for_status()
except requests.HTTPError:
    print("Could not complete request!")

content = response.json()
# print(json.dumps(content, indent=4))

# Calculate and output the price for the given number of bitcoins.
price = number * float(content["data"]["priceUsd"])
print(f"${price:,.4f}")
