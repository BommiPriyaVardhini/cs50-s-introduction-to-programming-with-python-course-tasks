import sys
import requests

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Try to convert the argument to a float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a valid number")

    # Fetch the current Bitcoin price from the CoinDesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to retrieve Bitcoin price")

    # Calculate the total cost
    total_cost = num_bitcoins * bitcoin_price

    # Output the total cost in USD with 4 decimal places and thousands separator
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
