
print()
print("Assume 8 hours of sleep, plus 2 hours each for bedtime preparation and the first meal after waking up.")
print()


def to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def to_time(total_minutes):
    total_minutes %= 24 * 60
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def display_time(total_minutes):
    if total_minutes == 24 * 60:
        return "24:00"  # if a free-time period ends at midnight
    return to_time(total_minutes)


# Input sleep start time in China time
sleep_start = input("When do you go to sleep in China time? (HH:MM): ")

sleep_start_min = to_minutes(sleep_start)

# Assume 8 hours of sleep
sleep_duration = 8 * 60
wake_up_min = (sleep_start_min + sleep_duration) % (24 * 60)

print(f"\nYou go to sleep at {to_time(sleep_start_min)}")
print(f"You wake up at {to_time(wake_up_min)}, assuming you sleep for 8 hours.")


# Choose the time difference
print("\nTime difference between China and Sweden:")
print("Enter 6 if Sweden is on summer time (usually late March to late October).")
print("Enter 7 if Sweden is on winter time (usually late October to late March).")

time_difference = int(input("How many hours is Sweden behind China? (6 or 7): "))

if time_difference not in (6, 7):
    print("Please enter either 6 or 7.")
else:
    # Calculate waking period
    print("\nYour free period in China time:")

    preparation = 2 * 60  # Assume 2 hours before sleep
    meal = 2 * 60  # Assume 2 hours after sleep

    busy_start = (sleep_start_min - preparation) % (24 * 60)
    busy_end = (wake_up_min + meal) % (24 * 60)

    if busy_end < busy_start:
        waking_periods = [
            (busy_end, busy_start)
        ]
    else:
        waking_periods = []

        if busy_end < 24 * 60:
            waking_periods.append((busy_end, 24 * 60))

        if busy_start > 0:
            waking_periods.append((0, busy_start))

    for start, end in waking_periods:
        sweden_start = start - time_difference * 60
        sweden_end = end - time_difference * 60

        print(f"China:  {display_time(start)} - {display_time(end)}")
        print(f"Sweden: {to_time(sweden_start)} - {to_time(sweden_end)}")  # Keep to_time() for Sweden time,
        # because the Swedish clock time needs to wrap around midnight.
        print()





