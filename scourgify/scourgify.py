import csv
import sys
import os.path

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    # Get the input and output filenames from the command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_filename):
        sys.exit(f"Error: The file '{input_filename}' does not exist")

    # Read the input CSV file and process the data
    try:
        with open(input_filename, mode='r') as input_file:
            reader = csv.DictReader(input_file)
            rows = []
            for row in reader:
                last, first = row['name'].split(", ")
                rows.append({'first': first, 'last': last, 'house': row['house']})

    except Exception as e:
        sys.exit(f"Error: Could not read the file '{input_filename}' - {e}")

    # Write to the output CSV file
    try:
        with open(output_filename, mode='w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(rows)

    except Exception as e:
        sys.exit(f"Error: Could not write to the file '{output_filename}' - {e}")

if __name__ == "__main__":
    main()
