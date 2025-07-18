
import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the time format
    match = re.match(r'(\d{1,2}:\d{2}|\d{1,2}) (AM|PM) to (\d{1,2}:\d{2}|\d{1,2}) (AM|PM)', s)
    if not match:
        raise ValueError("Invalid format")

    start_time, start_period, end_time, end_period = match.groups()

    start_24 = convert_to_24_hour(start_time, start_period)
    end_24 = convert_to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    # Split time into hours and minutes
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours = int(time)
        minutes = 0

    if not (0 <= minutes < 60):
        raise ValueError("Invalid time")

    if period == "AM":
        if hours == 12:
            hours = 0
        elif not (0 <= hours < 12):
            raise ValueError("Invalid time")
    elif period == "PM":
        if hours == 12:
            hours = 12
        elif not (1 <= hours <= 11):
            raise ValueError("Invalid time")
        else:
            hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
