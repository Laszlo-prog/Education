#Creating accounting app
class Transaction:
    def __init__(self,  amount, description, transaction_type):
        self.amount = amount

        self.description = description
        self.transaction_type = transaction_type
    def __str__(self):

        sign = '+' if self.transaction_type == 'credit' else '-'
        return f"{sign}${self.amount:.2f} - {self.description}"
    
class Account:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append(Transaction(amount, description, 'credit'))
        print(f"Income of ${amount:.2f} added. \n")
    def add_expense(self, amount, description):
        self.balance -= amount
        self.transactions.append(Transaction(amount, description, 'expense'))
        print(f"Expense of ${amount:.2f} recorded. \n")

    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}\n")
    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.\n")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print(t)
            print()  # New line for better readability
    def main():
        account = Account()
        while True:
            print("Welcome to the Accounting App!")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. View Transactions")
            print("5. Exit")

            choice = input("Choose an option(1-5): ")

            if choice == '1':
                amount = float(input("Enter income amount: "))
                description = input("Enter income description: ")
                account.add_income(amount, description)
            elif choice == '2':
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                account.add_expense(amount, description)
            elif choice == '3':
                account.view_balance()
            elif choice == '4':
                account.view_transactions()
            elif choice == '5':
                print("Exiting the Accounting App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    Account.main()
    
    # This code defines a simple accounting application that allows users to manage their income and expenses.