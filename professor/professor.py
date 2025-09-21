from random import randint


def main():
    # Get level.
    level = get_level()

    score = 0
    for _ in range(10):
        # Generate math problem.
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        for i in range(3):
            try:
                # Ask user for the solution of the math problem.
                answer = int(input(f"{x} + {y} = ").strip())
                if answer == result:
                    # Correct answer.
                    score += 1
                    break
                else:
                    # Incorrect answer.
                    raise ValueError
            except ValueError:
                print("EEE")
                if i == 2:
                    # Display result after 3 attempts.
                    print(f"{x} + {y} = {result}")
                continue

    print("Score:", score)


# Get level which must be an integer between 1 and 3 (inclusive).
def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 1 <= level <= 3:
                return level
        except ValueError:
            continue


# Generate a random positive integer (!= 0) with a specified number of decimals.
def generate_integer(dec):
    if dec <= 0:
        raise ValueError

    if dec == 1:
        start = 0
        end = 9
    else:
        start = 10 ** (dec - 1)
        end = 10 * start - 1

    return randint(start, end)


if __name__ == "__main__":
    main()
