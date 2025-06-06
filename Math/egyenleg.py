def calculate_bill(total_bill, tip_percentage, num_people):
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / num_people
    return tip_amount, total_amount, amount_per_person

def main():
    print("Welcome to the Bill Calculator!")
    
    while True:
        try:
            total_bill = float(input("Enter the total bill amount: $"))
            tip_percentage = float(input("Enter the tip percentage (10, 12, 15, etc.): "))
            num_people = int(input("Enter the number of people splitting the bill: "))
            
            if total_bill <= 0 or tip_percentage < 0 or num_people <= 0:
                raise ValueError("Please enter positive values.")
            
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    tip_amount, total_amount, amount_per_person = calculate_bill(total_bill, tip_percentage, num_people)
    
    print("\n--- Bill Summary ---")
    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Amount (including tip): ${total_amount:.2f}")
    print(f"Amount per person: ${amount_per_person:.2f}")

if __name__ == "__main__":
    main()