def get_fraction():
    while True:
        # Get the fraction from the user
        fraction = input("Fraction: ")

        try:
            # Split the fraction into numerator and denominator
            x, y = map(int, fraction.split('/'))

            # Check if the fraction is valid
            if y == 0 or x > y:
                continue
            else:
                # Return the valid fraction
                return x, y

        except ValueError:
            # If the input is not a valid fraction, continue to the next iteration
            continue

# Function to calculate the fuel percentage from a fraction
def calculate_fuel_percentage(x, y):
    try:
        # Calculate the fuel percentage
        percentage = (x / y) * 100

        # Return the fuel percentage as a string
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{round(percentage)}%"

    except ZeroDivisionError:
        # If the denominator is zero, get a new fraction and recalculate
        x, y = get_fraction()
        return calculate_fuel_percentage(x, y)

def main():
    # Get a valid fraction from the user
    x, y = get_fraction()

    # Calculate and print the fuel percentage
    fuel_percentage = calculate_fuel_percentage(x, y)
    print(fuel_percentage)

main()
