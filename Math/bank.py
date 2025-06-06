
def main():
    balance = 0
    bank = bank
    is_running = True

    while True:
        print("\n--- Banking Application ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            acc_num = input("Enter new account number: ")
            print(bank.create_account(acc_num))
        elif choice in ['2', '3', '4', '5']:
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    print(account.deposit(amount))
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    print(account.withdraw(amount))
                elif choice == '4':
                    print(account.get_balance())
                elif choice == '5':
                    for transaction in account.get_transaction_history():
                        print(f"{transaction[0]}: ${transaction[1]:.2f} on {transaction[2]}")
            else:
                print("Account not found")
        elif choice == '6':
            print("Thank you for using the Banking Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        bank.save_accounts()

if __name__ == "__main__":
    main()