def main():
    # Get meal cost from user
    dollars = dollars_to_float(input("How much was the meal? "))
    # Get desired tip percentage from user
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate tip amount
    tip = dollars * percent
    # Print calculated tip amount
    print(f"Leave ${tip:.2f}")

# Convert dollar amount string to float
def dollars_to_float(d):
    return float(d.strip('$'))

# Convert percentage string to float
def percent_to_float(p):
    return float(p.strip('%')) / 100

main()
