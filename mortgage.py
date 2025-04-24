# Mortgage Calculator

def main():
    print("Mortgage Calculator")
    print()

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the number of years: "))
    
    monthly_interest_rate = apr / 100 / 12
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    total_payment = monthly_payment * number_of_payments
    total_interest = total_payment - principal

    print()
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")
    print(f"Total Interest: ${total_interest:.2f}")

    return total_payment
# Run the calculator
if __name__ == "__main__":
    main()

