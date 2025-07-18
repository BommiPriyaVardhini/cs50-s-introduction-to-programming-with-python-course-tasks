def main():
    fraction = input("Enter the fraction in X/Y format: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(e)

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = round((x / y) * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid input. X and Y must be integers.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
