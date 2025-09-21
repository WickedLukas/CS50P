# Allowed coins.
COINS = (5, 10, 25)

# Insert coins until payment is complete and provide change.
amount_due = 50
while (True):
    if amount_due > 0:
        print("Amount Due:", amount_due)
    else:
        print("Change Owed:", abs(amount_due))
        break

    coin = int(input("Insert Coin: "))
    if coin in COINS:
        amount_due -= coin
