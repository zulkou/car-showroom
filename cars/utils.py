from decimal import Decimal

def calculate_loan_details(transaction, car):
    services_cost = sum(service.cost for service in car.services.all())

    if transaction.is_loan:
        down_payment = Decimal(transaction.down_payment) if isinstance(transaction.down_payment, str) else transaction.down_payment
        tenor = int(transaction.tenor) if isinstance(transaction.tenor, str) else transaction.tenor
        annual_interest_rate = Decimal(transaction.annual_interest_rate) if isinstance(transaction.annual_interest_rate, str) else transaction.annual_interest_rate

        principal = car.base_price - down_payment
        monthly_interest = annual_interest_rate / 12

        loan_amount = (principal * (1 + monthly_interest)) + services_cost
        monthly_payment = loan_amount / tenor
        total_cost = down_payment + loan_amount
    else:
        loan_amount = 0
        monthly_payment = 0
        total_cost = car.base_price + services_cost

    return services_cost, loan_amount, monthly_payment, total_cost