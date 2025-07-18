import sys
import os

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    # Get the input filename from the command-line argument
    filename = sys.argv[1]

    # Check if the file extension is .py
    if not filename.endswith(".py"):
        sys.exit("Error: The file must have a .py extension")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: The file '{filename}' does not exist")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        sys.exit(f"Error: Could not read the file '{filename}' - {e}")

    loc = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1

    print(loc)

if __name__ == "__main__":
    main()
