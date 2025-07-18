# figlet.py

import sys
import random
import pyfiglet

def main():
    # List of available fonts
    fonts = pyfiglet.FigletFont.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # No font specified, choose a random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Error: Invalid font name.")
    else:
        sys.exit("Usage: figlet.py [-f | --font] <font_name>")

    # Prompt the user for input text
    text = input("Input: ")

    # Create a Figlet object with the specified or random font
    figlet = pyfiglet.Figlet(font=font)

    # Print the text in the chosen font
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
