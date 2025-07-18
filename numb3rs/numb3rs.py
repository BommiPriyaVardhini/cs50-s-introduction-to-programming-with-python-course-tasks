import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression for a valid IPv4 address
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"

    if re.match(pattern, ip):
        # Split the ip into its parts and check each part
        parts = ip.split('.')
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
