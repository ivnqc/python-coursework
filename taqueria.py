# Menu with item names and prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Function to place an order
def place_order():
    # Initialize total cost to zero
    total_cost = 0.0

    try:
        # Continuously prompt for items until end of input
        while True:
            # Get the item from the user
            item = input("Item: ").strip()

            # Convert the item to title case for matching with menu
            item_title_case = item.title()

            try:
                # Add the item's price to the total cost
                total_cost += menu[item_title_case]
                # Print the updated total cost
                print(f"Total: ${total_cost:.2f}")
            except KeyError:
                # If the item is not in the menu, continue to the next iteration
                continue
    except EOFError:
        # Print a newline when end of input is reached
        print("\n")

place_order()
