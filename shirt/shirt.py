import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    # Get the input and output filenames from the command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the file extensions are valid
    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not input_filename.lower().endswith(valid_extensions) or not output_filename.lower().endswith(valid_extensions):
        sys.exit("Error: Files must have a .jpg, .jpeg, or .png extension")

    # Check if the input and output filenames have the same extension
    if os.path.splitext(input_filename)[1].lower() != os.path.splitext(output_filename)[1].lower():
        sys.exit("Error: Input and output files must have the same extension")

    # Check if the input file exists
    if not os.path.isfile(input_filename):
        sys.exit(f"Error: The file '{input_filename}' does not exist")

    # Open the input image and shirt image
    try:
        input_image = Image.open(input_filename)
        shirt_image = Image.open("shirt.png")
    except Exception as e:
        sys.exit(f"Error: Could not open the image files - {e}")

    # Resize and crop the input image to the size of the shirt image
    try:
        input_image = ImageOps.fit(input_image, shirt_image.size)
    except Exception as e:
        sys.exit(f"Error: Could not resize or crop the input image - {e}")

    # Overlay the shirt image on the input image
    try:
        input_image.paste(shirt_image, (0, 0), shirt_image)
    except Exception as e:
        sys.exit(f"Error: Could not overlay the shirt image - {e}")

    # Save the output image
    try:
        input_image.save(output_filename)
    except Exception as e:
        sys.exit(f"Error: Could not save the output image - {e}")

if __name__ == "__main__":
    main()
