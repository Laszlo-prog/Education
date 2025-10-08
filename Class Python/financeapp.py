class FinanceApp:
    def __init__(self):
        
        self.balance = 0.0
        self.income = 0.0
        self.expense = 0.0
    #Defition of methods to add income, expense, view balance, and view transactions    
    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}\n")

    def add_income(self, amount, description):
        amount = float(input("Enter income amount: "))
        self.income += amount
        self.balance += amount
        print(f"Income of ${amount:.2f} added. \n")

    def add_expense(self, amount, description):
        amount = float(input("Enter expense amount: "))
        self.expense += amount
        self.balance -= amount
        print(f"Expense of ${amount:.2f} recorded. \n")

    def view_transactions(self):
       
        print(f"Total Expense: ${self.expense:.2f}")
        
    
    def menu(self):
        while True:
            print("Welcome to the Finance App!")
            print("1. View Balance")
            print("2. Add Income")
            print("3. Add Expense")
            print("4. View Transactions")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")
            if choice == '1':
                self.view_balance()
            elif choice == '2':
                amount = float(input("Enter income amount: "))
                description = input("Enter income description: ")
                
                self.add_income(amount, description)
            elif choice == '3':
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                self.add_expense(amount, description)
            elif choice == '4':
                self.view_transactions()
            elif choice == '5':

                print("Exiting the Finance App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    app = FinanceApp()
    app.menu()



