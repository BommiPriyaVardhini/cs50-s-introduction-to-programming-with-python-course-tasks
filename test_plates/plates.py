def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Plates must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Plates must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters
    if not s.isalnum():
        return False

    # Numbers cannot be in the middle of the plate and cannot have leading zero
    number_started = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            if not number_started and s[i] == '0':
                return False
            number_started = True
        elif number_started:
            return False

    return True

if __name__ == "__main__":
    main()
