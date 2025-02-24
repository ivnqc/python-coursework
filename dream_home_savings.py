import math

# Constants
PORTION_DOWN_PAYMENT = 0.25  # Percentage of the home price needed for a down payment
R = 0.05  # Annual interest rate

def calculate_months(yearly_salary, portion_saved, cost_of_dream_home):
    """
    Calculates the number of months needed to save for a down payment.

    Parameters:
    yearly_salary (float): The user's annual salary.
    portion_saved (float): The fraction of salary to be saved each month.
    cost_of_dream_home (float): The total cost of the desired home.

    Returns:
    int: Number of months required to save for the down payment.
    """
    amount_saved = portion_saved * (yearly_salary / 12)  # Monthly savings
    required_down_payment = PORTION_DOWN_PAYMENT * cost_of_dream_home  # Total amount needed

    # Prevent division by zero or negative values
    if amount_saved <= 0:
        raise ValueError("Error: The saving amount must be positive. Please check your inputs.")

    # Solve for months using logarithm formula
    months = math.log((required_down_payment * (R / 12) / amount_saved) + 1) / math.log(1 + (R / 12))

    return math.ceil(months)

def main():
    """Handles user input and program execution."""
    try:
        yearly_salary = float(input("Enter your yearly salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        cost_of_dream_home = float(input("Enter the cost of your dream home: "))

        months = calculate_months(yearly_salary, portion_saved, cost_of_dream_home)
        print(f"Number of months: {months}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
