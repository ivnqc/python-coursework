def main():
    # Define the accepted coin denominations
    accepted_coins = [5, 10, 25]

    # Initialize total amount inserted by the user
    total_inserted = 0

    # Loop until the total inserted is at least 50 cents
    while total_inserted < 50:
        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is a valid denomination
        if coin in accepted_coins:
            total_inserted += coin

        print(f"Amount Due: {50 - total_inserted}")

    # Calculate the change owed
    change = total_inserted - 50
    print(f"Change owed: {change}")

# Run the program
main()
