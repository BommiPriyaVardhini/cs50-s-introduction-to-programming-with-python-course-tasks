# outdated.py

def main():
    import re
    from datetime import datetime

    # List of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        # Check for MM/DD/YYYY format
        if match := re.match(r'^(0?[1-9]|1[0-2])/([0-2]?[0-9]|3[0-1])/([0-9]{4})$', date_str):
            month, day, year = match.groups()
            try:
                date = datetime.strptime(f"{month}/{day}/{year}", "%m/%d/%Y")
                print(date.strftime("%Y-%m-%d"))
                break
            except ValueError:
                continue

        # Check for "Month Day, Year" format
        if match := re.match(r'^([A-Za-z]+) ([0-2]?[0-9]|3[0-1]), ([0-9]{4})$', date_str):
            month_str, day, year = match.groups()
            if month_str in months:
                month = months.index(month_str) + 1
                try:
                    date = datetime.strptime(f"{month}/{day}/{year}", "%m/%d/%Y")
                    print(date.strftime("%Y-%m-%d"))
                    break
                except ValueError:
                    continue

        # If the input does not match any valid date format
        print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
