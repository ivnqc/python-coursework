import sys
import requests

# Fetches the current Bitcoin price from the CoinDesk API
def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        # Send a GET request to the API and raise an exception for bad status codes
        response = requests.get(url)
        response.raise_for_status()
        # Parse the JSON response and extract the USD price
        data = response.json()
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except requests.RequestException:
        # Exit the program if the request fails
        sys.exit("Error: Unable to fetch Bitcoin price.")

def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Attempt to convert the command-line argument to a float
        bitcoins = float(sys.argv[1])
    except ValueError:
        # Exit the program if the argument is not a number
        sys.exit("Command-line argument is not a number")

    # Fetch the current Bitcoin price and calculate the total cost
    price_per_bitcoin = get_bitcoin_price()
    total_cost = bitcoins * price_per_bitcoin

    # Print the total cost with commas and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
