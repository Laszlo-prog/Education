from math import ceil
from datetime import datetime, timedelta

class CreditCalculator:
    def __init__(self):
        self.credit_principal = None
        self.monthly_payment = None
        self.credit_interest = None
        self.number_of_periods = None
        self.payment_type = None

    def get_parameters(self):
        print("Enter the credit details:")
        
        while True:
            param = input("What do you want to calculate?\n"
                          "type 'n' for number of monthly payments,\n"
                          "type 'a' for annuity monthly payment amount,\n"
                          "type 'p' for credit principal:\n")
            if param in ['n', 'a', 'p']:
                self.payment_type = param
                break
            print("Invalid input. Please try again.")

        if self.payment_type != 'p':
            self.credit_principal = float(input("Enter the credit principal:\n"))
        if self.payment_type != 'a':
            self.monthly_payment = float(input("Enter the monthly payment:\n"))
        if self.payment_type != 'n':
            self.number_of_periods = int(input("Enter the number of periods:\n"))
        
        self.credit_interest = float(input("Enter the credit interest:\n")) / 100 / 12

    def calculate(self):
        if self.payment_type == 'n':
            return self.calculate_periods()
        elif self.payment_type == 'a':
            return self.calculate_annuity()
        elif self.payment_type == 'p':
            return self.calculate_principal()
        else:
            return "Invalid calculation type"

    def calculate_periods(self):
        # Calculate number of months needed to repay the credit
        i = self.credit_interest
        numerator = self.monthly_payment - i * self.credit_principal
        denominator = self.monthly_payment - i * self.credit_principal
        
        if numerator <= 0 or denominator <= 0:
            return "Invalid parameters - cannot calculate periods"

        n = ceil((self.monthly_payment / (self.monthly_payment - i * self.credit_principal)).__log__(1 + i))
        
        years = n // 12
        months = n % 12
        
        period_str = ""
        if years > 0:
            period_str += f"{years} year{'s' if years > 1 else ''}"
        if months > 0:
            if years > 0:
                period_str += " and "
            period_str += f"{months} month{'s' if months > 1 else ''}"
        
        overpayment = ceil(self.monthly_payment * n - self.credit_principal)
        
        return f"It will take {period_str} to repay this credit!\nOverpayment = {overpayment}"

    def calculate_annuity(self):
        # Calculate fixed monthly payment
        i = self.credit_interest
        n = self.number_of_periods
        
        annuity = ceil(self.credit_principal * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        overpayment = ceil(annuity * n - self.credit_principal)
        
        return f"Your annuity payment = {annuity}!\nOverpayment = {overpayment}"

    def calculate_principal(self):
        # Calculate loan principal
        i = self.credit_interest
        n = self.number_of_periods
        
        principal = ceil(self.monthly_payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        overpayment = ceil(self.monthly_payment * n - principal)
        
        return f"Your credit principal = {principal}!\nOverpayment = {overpayment}"

    def calculate_diff_payments(self, principal, periods, interest):
        # Calculate differentiated payments
        total_payment = 0
        current_date = datetime.now()
        
        for m in range(1, periods + 1):
            payment = ceil(principal / periods + interest * (principal - (principal * (m - 1)) / periods))
            total_payment += payment
            payment_date = current_date + timedelta(days=30 * m)
            print(f"{payment_date.strftime('%d.%m.%Y')}: {payment}")
        
        overpayment = ceil(total_payment - principal)
        print(f"\nOverpayment = {overpayment}")

    def run(self):
        self.get_parameters()
        
        if all(v is not None for v in [self.credit_principal, self.credit_interest, self.number_of_periods]):
            print("\nDifferentiated payments:")
            self.calculate_diff_payments(self.credit_principal, self.number_of_periods, self.credit_interest)
            print("\nAnnuity payment calculation:")
        
        result = self.calculate()
        print("\n" + result)


if __name__ == "__main__":
    calculator = CreditCalculator()
    calculator.run()