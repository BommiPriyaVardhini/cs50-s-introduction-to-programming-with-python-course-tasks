import csv
import sys
import os.path
from tabulate import tabulate

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py FILENAME")

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    # Check if the file has a .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Error: The file must have a .csv extension")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: The file '{filename}' does not exist")

    # Read the CSV file and store the data
    table_data = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the headers
            for row in reader:
                table_data.append(row)
    except Exception as e:
        sys.exit(f"Error: Could not read the file '{filename}' - {e}")

    # Print the table using tabulate with the grid format
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
