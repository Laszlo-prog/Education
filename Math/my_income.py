import math

# Function to calculate simple income
def calculate_income(hourly_wage, hours_worked):
    income = hourly_wage * hours_worked
    return income

# Input values
hourly_wage = int(input("Enter your hourly wage: "))
hours_worked = int(input("Enter the number of hours worked: "))

# Calculate income
income = calculate_income(hourly_wage, hours_worked)

# Output the result
print(f"Your total income is: ${income:.2f}")
