def main():
    # Ask user.
    time = input("What time is it? ")

    time_float = convert(time)
    if time_float == None:
        return

    # Respond to user.
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")


# Convert time, a str in 24-hour format, to the corresponding number of hours as a float.
def convert(time):
    # Get hours and minutes.
    split_time = time.split(":")
    if len(split_time) == 2:
        hours = int(split_time[0])
        minutes = int(split_time[1])
    else:
        return None

    return hours + minutes / 60


if __name__ == "__main__":
    main()
