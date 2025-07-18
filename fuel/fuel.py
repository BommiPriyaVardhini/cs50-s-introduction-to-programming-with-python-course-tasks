def main():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ")
            fuel_percentage = calculate_fuel_percentage(fraction)
            if fuel_percentage == 'E':
                print("E")
            elif fuel_percentage == 'F':
                print("F")
            else:
                print(f"{fuel_percentage}% ")
            break
        except ValueError:
            print("Invalid input. Please enter integers for X and Y.")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")


def calculate_fuel_percentage(fraction):
    parts = fraction.split('/')
    if len(parts) != 2:
        raise ValueError("Invalid input format. Please use X/Y format.")
    X, Y = map(int, parts)
    if Y == 0:
        raise ZeroDivisionError("Invalid input. Y cannot be zero.")
    if not (1 <= X <= Y):
        raise ValueError("Invalid input. X must be between 1 and Y.")
    percentage = (X / Y) * 100
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return round(percentage)


if __name__ == "__main__":
    main()
