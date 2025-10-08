class Account:
    def __init__(self, name: str, balance: float = 0.0 ):
        self.name = name
        self.balance = balance

#create deposit on amount into the account
    def deposit(self, amount: float):
        self.balance += amount

# create withdraw from the account
    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
# create a method to get the account balance
    def get_balance(self) -> float:

        return self.balance
# handle the command    
class BankApp:
    def __init__(self):
        self.accounts: dict = [str, Account] == {} 
    
    def create(self):
        name = input("Enter account name: ")
        balance = float(input("Enter initial balance: "))
        self.accounts[name] = Account(name, balance)
        print("Account created successfully.")


    def account(self, name: str):
        return self.accounts.get(name, None)
    
    def deposit(self):
        name = input("Enter account name: " )
        amount = float(input("Enter deposit amount: "))
        a = self.account(name)
        if a:
            a.deposit(amount)
            print("Deposited \n")
        else:
            print("Account not found.\n")

    def withdraw(self):
        name = input("Enter account name: ")
        amount = float(input("Enter withdraw amount: "))
        a = self.account(name)
        if a:
            if a.withdraw(amount):
                print("Withdrawn successfully.\n")
            else:
                print("Insufficient balance.\n")    
    def balance(self):
        name = input("Enter account name: ")
        a = self.account(name)
        if a:
            print(f"Balance: {a.get_balance()}\n")  
        else:
            print("Account not found.\n")

    def run(self):

     
        while True:
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.balance()
            elif choice == '5':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    app = BankApp()
    app.run()        

    
        
    
        
    
