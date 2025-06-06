def calculate_bill():
    print("Welcome to the Bill Calculator!")

    # Input total bill amount
    total_bill = float(input("Enter the total bill amount: $"))

    # Input tip percentage (e.g., 10, 15, 20)
    tip_percentage = float(input("Enter the tip percentage you want to add (e.g., 10 for 10%): "))

    # Calculate tip amount
    tip_amount = (tip_percentage / 100) * total_bill
    total_with_tip = total_bill + tip_amount

    # Split the bill among 4 people
    per_person_amount = total_with_tip / 4

    # Display results
    print("\nBill Summary:")
    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
    print(f"Total with Tip: ${total_with_tip:.2f}")
    print(f"Each person owes: ${per_person_amount:.2f}")


# Call the function
if __name__ == "__main__":
    calculate_bill()