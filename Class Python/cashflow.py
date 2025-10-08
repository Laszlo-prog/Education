class OnlineEarningsApp:
    def __init__(self):
        self.balance = 0

#Add money to  balance
    def add_earnings(self, amount):
        self.balance += amount
        print(f"Earnings of ${amount:.2f} added. \n")

#Viewing method > check balance
    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}\n")

#withdraw method withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

            print(f"Withdrew ${amount:.2f}. \n")

        else:
            print("Insufficient balance. \n")
 #Task method complete task to earn
 # 
    def do_task(self):
        self.balance += 10  # Each task earns $10
        print("Task completed! Earned $10. \n")

    def referral(self):
        self.balance += 5  # Each referral earns $5
        print("Referral successful! Earned $5. \n")

#Menu method = display options
def main():
    app = OnlineEarningsApp()
    while True:
        print("Welcome to the Online Earnings App!")
        print("1. Add Earnings")
        print("2. View Balance")
        print("3. Withdraw")
        print("4. Do Task")
        print("5. Referral")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            amount = float(input("Enter amount to add: "))
            app.add_earnings(amount)
        elif choice == '2':
            app.view_balance()
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            app.withdraw(amount)
        elif choice == '4':
            app.do_task()
        elif choice == '5':
            app.referral()
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
    

