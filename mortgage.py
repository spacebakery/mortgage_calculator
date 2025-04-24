# Mortgage Calculator

def main():
    """
    Calculates the monthly payment, total payment, and total interest paid on a mortgage.
    """
    print("Mortgage Calculator")
    print()

    # Get the loan amount, annual interest rate (%), and number of years
    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the number of years: "))

    # Convert the annual interest rate to a monthly interest rate
    monthly_interest_rate = apr / 100 / 12

    # Calculate the number of payments
    number_of_payments = years * 12

    # Calculate the monthly payment
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    # Calculate the total payment and total interest
    total_payment = monthly_payment * number_of_payments
    total_interest = total_payment - principal

    # Print the results
    print()
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")
    print(f"Total Interest: ${total_interest:.2f}")

    return total_payment

# Run the calculator
if __name__ == "__main__":
    main()

