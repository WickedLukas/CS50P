MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)


def main():
    year, month, day = get_date()

    # Print date in YYYY-MM-DD format (ISO 8601)
    print(f"{year:04d}-{month:02d}-{day:02d}")


def get_date():
    while True:
        date = input("Date: ").strip()

        parts = date.split("/")
        if len(parts) == 3:
            # Date in MM/DD/YYYY format.
            m, d, y = parts

            try:
                month = int(m)
            except ValueError:
                # Failed to convert month to int.
                continue

            if not (1 <= month <= 12):
                # Month is out of range.
                continue
        else:
            # Date in other format.
            # Month word is seperated by whitespace.
            parts = date.split(" ", 1)
            if len(parts) == 2:
                m_word, rest = parts

                # Get month number from month word.
                try:
                    month = MONTHS.index(m_word) + 1
                    # Month found in MONTHS, so there is no need to check its range.
                except ValueError:
                    # Month does not exist (in MONTHS).
                    continue

                # Year is seperated by comma with whitespace.
                parts = rest.split(", ")
                if len(parts) == 2:
                    d, y = parts
                else:
                    # Failed to get day and year because of invalid format.
                    continue

            else:
                # Failed to get month because of invalid format.
                continue

        try:
            day = int(d)
            year = int(y)
        except ValueError:
            # Failed to convert day and/or year to int.
            continue

        if not (1 <= day <= 31) or not (0 <= year <= 9999):
            # Invalid range for day and/or year.
            continue

        return year, month, day


main()
