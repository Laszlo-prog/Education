def calculate_income(hourly_wage, hours_worked, deductions=0, bonuses=0):
    """
    Calculate the net income based on hourly wage, hours worked,
    deductions, and bonuses.

    Parameters:
    - hourly_wage (float): The rate of pay per hour.
    - hours_worked (float): Total hours worked.
    - deductions (float): Total deductions (default is 0).
    - bonuses (float): Additional bonuses (default is 0).

    Returns:
    - float: The calculated net income.
    """
    gross_income = hourly_wage * hours_worked
    net_income = gross_income + bonuses - deductions
    return net_income


# Example usage
hourly_wage = 15.0  # $20/hour
hours_worked = 46  # 40 hours in a week
deductions = 0  # $50 deductions
bonuses = 10  # $100 bonus

net_income = calculate_income(hourly_wage, hours_worked, deductions, bonuses)
print(f"Your net income is: ${net_income:.2f}")