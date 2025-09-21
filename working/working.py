import re


def main():
    # Convert 12-hour format to 24-hour format.
    print(convert(input("Hours: ")))


# Convert time period in 12-hour format to 24-hour format.
def convert(s: str):
    pattern_hours = r"(1[0-2]|[1-9])"
    pattern_minutes = r"([0-5][0-9])"
    pattern_time = r"(?:" + pattern_hours + r"(?::" + pattern_minutes + r")? (AM|PM))"
    pattern = r"^" + pattern_time + r" to " + pattern_time + r"$"
    if match := re.search(pattern, s):
        hours_from, minutes_from, am_pm_from, hours_to, minutes_to, am_pm_to = match.groups()
        minutes_from = minutes_from if minutes_from != None else "00"
        minutes_to = minutes_to if minutes_to != None else "00"
        return convert_hours(hours_from, am_pm_from) + ":" + minutes_from + " to " + convert_hours(hours_to, am_pm_to) + ":" + minutes_to
    else:
        raise ValueError


# Convert hours in 12-hour format to 24-hour format.
def convert_hours(hours: str, am_pm: str):
    if am_pm == "AM":
        if hours == "12":
            hours_24 = "00"
        elif int(hours) > 9:
            hours_24 = hours
        else:
            hours_24 = "0" + hours
    else:
        if int(hours) == 12:
            hours_24 = "12"
        else:
            hours_24 = str(12 + int(hours))

    return hours_24


if __name__ == "__main__":
    main()
