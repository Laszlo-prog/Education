class User:
    def __init__(self, name,  balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
       print(f"{self.name}'s balance: ${self.balance:.2f}")

    #add money to the balance
    def add_money(self, amount):
        self.balance += amount
        print(f"Added ${amount:.2f} to {self.name}'s balance. New balance: ${self.balance:.2f}")
    #send money to another user

    def send_money(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Sent ${amount:.2f} to {recipient.name}. New balance: ${self.balance:.2f}")
        else:
            print(f"Insufficient balance to send ${amount:.2f} to {recipient.name}. Current balance: ${self.balance:.2f}")

    #show menu and handle choices
    def main():
        #create two users 
        user1 = User("Alice", 100.00)
        user2 = User("Bob", 50.00)

        while True:
            print("\nPayment App Menu:")
            print("1. Show Balance")
            print("2. Add Money")
            print("3. Send Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                user1.show_balance()
            elif choice == '2':
                amount = float(input("Enter amount to add: "))
                user1.add_money(amount)
            elif choice == '3':
                amount = float(input("Enter amount to send: "))
                user1.send_money(user2, amount)
            elif choice == '4':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    User.main() 
            
