def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_with_letters(s):
        return False
    if not valid_length(s):
        return False
    if not numbers_at_end(s):
        return False
    if not no_invalid_characters(s):
        return False
    return True


def starts_with_letters(s):
    return s[:2].isalpha()


def valid_length(s):
    return 2 <= len(s) <= 6


def numbers_at_end(s):
    if s[-1].isdigit():
        if s[-1] == '0':
            return False
        for char in s[2:-1]:
            if char.isdigit():
                return False
        return True
    return False


def no_invalid_characters(s):
    return all(char.isalnum() for char in s)


if __name__ == "__main__":
    main()
