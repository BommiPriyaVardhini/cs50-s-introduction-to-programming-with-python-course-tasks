def get_names():
    """Prompt the user to enter names and return the list of names."""
    print("Enter names (press Control-D to end input):")
    names = []
    try:
        while True:
            name = input()
            if name.strip():  # Only add non-empty names
                names.append(name)
    except EOFError:
        pass
    return names

def format_farewell(names):
    """Format the list of names into a farewell string."""
    output = "Adieu, adieu, to "
    if len(names) == 1:
        output += names[0]
    else:
        output += ', '.join(names[:-1]) + ", and " + names[-1]
    return output

def main():
    import sys

    # Get the list of names
    names = get_names()

    # Debugging: Print the list of names
    print(f"Debug: Names entered: {names}")

    # Ensure there is at least one name
    if not names:
        sys.exit("Error: No names provided. Please run the script again and enter at least one name.")

    # Format and print the farewell message
    farewell_message = format_farewell(names)
    print(farewell_message)

if __name__ == "__main__":
    main()
