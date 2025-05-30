class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Initialize a bank account with account holder name and optional initial balance
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account
        Returns True if successful, False otherwise
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount:.2f}")
            return True
        print("Invalid deposit amount. Amount must be positive.")
        return False
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account
        Returns True if successful, False otherwise
        """
        if amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
            return False
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
            return True
        print("Insufficient funds for this withdrawal.")
        return False
    
    def get_balance(self) -> float:
        """Return the current account balance"""
        return self.balance
    
    def get_transaction_history(self) -> list:
        """Return the transaction history"""
        return self.transaction_history
    
    def __str__(self) -> str:
        """String representation of the account"""
        return f"Account Holder: {self.account_holder}\nCurrent Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        """
        Initialize a savings account with interest rate
        """
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        """Add monthly interest to the account"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest: +${interest:.2f}")
        return interest


# Example usage
if __name__ == "__main__":
    # Create a regular bank account
    account1 = BankAccount("John Doe", 1000.00)
    print(account1)
    
    # Deposit money
    account1.deposit(500.50)
    print(f"\nAfter deposit: ${account1.get_balance():.2f}")
    
    # Withdraw money
    account1.withdraw(200.75)
    print(f"After withdrawal: ${account1.get_balance():.2f}")
    
    # Try invalid operations
    account1.deposit(-100)  # Invalid deposit
    account1.withdraw(2000)  # Insufficient funds
    
    # Print transaction history
    print("\nTransaction History:")
    for transaction in account1.get_transaction_history():
        print(transaction)
    
    # Create a savings account
    savings_account = SavingsAccount("Jane Smith", 5000.00, 0.015)
    print(f"\n{savings_account}")
    
    # Add interest to savings account
    interest = savings_account.add_interest()
    print(f"Interest added: ${interest:.2f}")
    print(f"New balance: ${savings_account.get_balance():.2f}")