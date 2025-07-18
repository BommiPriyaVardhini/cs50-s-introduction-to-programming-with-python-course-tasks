def main():
    time = input("Enter the time in 24-hour format (HH:MM): ")
    meal_time = determine_meal_time(time)
    if meal_time:
        print(meal_time)


def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def determine_meal_time(time):
    hours = convert(time)
    if 7.0 <= hours <= 8.0:
        return "breakfast time"
    elif 12.0 <= hours <= 13.0:
        return " lunch time"
    elif 18.0 <= hours <= 19.0:
        return "dinner time"


if __name__ == "__main__":
    main()
