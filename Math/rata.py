def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (as a decimal).
    time (float): The time period in years.
    
    Returns:
    float: The amount of interest earned.
    """
    interest = principal * rate * time
    return interest

def calculate_total_amount(principal, interest):
    """
    Calculate the total amount after adding interest.
    
    Args:
    principal (float): The initial amount of money.
    interest (float): The amount of interest earned.
    
    Returns:
    float: The total amount after adding interest.
    """
    return principal + interest

# Example usage
principal = 1000  # Initial amount, e.g., $1000
rate = 0.05  # 5% annual interest rate
time = 2  # 2 years

interest = calculate_simple_interest(principal, rate, time)
total_amount = calculate_total_amount(principal, interest)

print(f"Principal amount: ${principal:.2f}")
print(f"Interest rate: {rate*100:.1f}%")
print(f"Time period: {time} years")
print(f"Interest earned: ${interest:.2f}")
print(f"Total amount after {time} years: ${total_amount:.2f}")