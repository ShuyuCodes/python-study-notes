from datetime import datetime
from zoneinfo import ZoneInfo

print()
print("Assume 8 hours of sleep, plus 2 hours for bedtime preparation "
      "and 2 hours for your morning routine (including your first meal and medication).")
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
# sleep_start = '18:00'

sleep_start_min = to_minutes(sleep_start)

# Assume 8 hours of sleep
sleep_duration = 8 * 60
wake_up_min = (sleep_start_min + sleep_duration) % (24 * 60)

print(f"\nYou go to sleep at {to_time(sleep_start_min)}")
print(f"You wake up at {to_time(wake_up_min)}, assuming you sleep for 8 hours.")


# Choose the time difference
print("\nTime difference between China and Sweden:")
print("6 if Sweden is on summer time (usually late March to late October).")
print("7 if Sweden is on winter time (usually late October to late March).")


def get_sweden_time_difference():
    china_time = datetime.now(ZoneInfo("Asia/Shanghai"))
    # print('n', china_time)  # 2026-10-17 18:13:58.738944+08:00
    sweden_time = china_time.astimezone(ZoneInfo("Europe/Stockholm"))

    # utc stands for Coordinated Universal Time.
    # It is the global time standard used as a reference for calculating time zones
    difference = int(
        (china_time.utcoffset() - sweden_time.utcoffset()).total_seconds() / 3600  # china_time.utcoffset())  # 8:00:00
        # sweden_time.utcoffset())  # 2:00:00
    )
    # print('d', difference)  # 6

    if sweden_time.dst().total_seconds() != 0:  # dst stands for daylight saving time
        season = "summer time"
        utc_offset = "UTC+2"
    else:  # sweden_time.dst() returns zero during winter because Sweden is not observing daylight saving time then.
        season = "winter time"
        utc_offset = "UTC+1"

    print(f"\nCurrent date: {china_time.strftime('%B %d, %Y')}")
    print(f"Sweden is currently on {season}.")
    print(f"Sweden's current UTC offset is {utc_offset}.")
    print(f"Sweden is {difference} hours behind China.")

    return difference


# time_difference = int(input("How many hours is Sweden behind China? (6 or 7): "))
time_difference = get_sweden_time_difference()

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





