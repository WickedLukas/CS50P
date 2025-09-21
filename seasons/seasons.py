import sys

from datetime import date, timedelta
import inflect


def main():
    # Get birth date.
    birth_date = get_birth_date()

    # Calculate the timedelta between today and the birth date.
    delta = date.today() - birth_date

    # Convert timedelta to minutes and the to words.
    words_minutes = convert_minutes_to_words(convert_to_minutes(delta))

    # Print the minutes between today and birth date in words.
    print(words_minutes)


def get_birth_date() -> date:
    """
    Get birth date from the user.
    """
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date.")

    return birth_date


def convert_to_minutes(delta: timedelta) -> int:
    """
    Convert date.timedelta to minutes.
    """
    return round(delta.total_seconds() / 60)


def convert_minutes_to_words(minutes: int) -> str:
    """
    Convert number of minutes to words.
    """
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
