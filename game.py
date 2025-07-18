import random

def get_positive_integer(prompt):
    """Prompt the user to enter a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    # Prompt the user for the level
    level = get_positive_integer("Level: ")

    # Randomly generate a number between 1 and the given level
    target = random.randint(1, level)

    while True:
        # Prompt the user to guess the number
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
