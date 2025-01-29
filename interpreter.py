def main():
    # Get user input for an arithmetic expression (x y z)
    expression = input("Enter an arithmetic expression (x y z): ")

    # Split the input into x, operator, and z
    x, y, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the specified arithmetic operation
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        try:
            result = x / z
        except ZeroDivisionError:
            print("Cannot divide by zero")
            result = 0

    # Print the result with one decimal place
    print(f"{result:.1f}")

main()
