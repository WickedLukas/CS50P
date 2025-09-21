def main():
    while True:
        # Get fraction from user.
        fraction = input("Fraction: ")

        try:
            # Convert fraction to percentage.
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    # Calculate gauge value.
    gauge_value = gauge(percentage)

    # Output gauge value.
    print(gauge_value)


# Convert fraction to percentage.
def convert(fraction):
    # Get values from fraction.
    x, _, y = fraction.partition("/")

    # Calculate percentage.
    percentage = int(x) / int(y) * 100

    # Check percentage range.
    if percentage < 0 or percentage > 100:
        raise ValueError

    # Return percentage.
    return percentage


# Get gauge value for a given percentage.
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
