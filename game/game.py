from random import randint

def main():
    # Get level.
    level = get_pos_int("Level: ")

    # Get random number between 1 and level (inclusive).
    value = randint(1, level)

    while True:
        guess = get_pos_int("Guess: ")

        if guess < value:
            print("Too small!")
        elif guess > value:
            print("Too large!")
        else:
            print("Just right!")
            return


# Get positive integer.
def get_pos_int(s):
    while True:
        try:
            result = int(input(s).strip())
            if result > 0:
                return result
        except ValueError:
            continue


main()
