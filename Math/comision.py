def calculate_commission(sale_amount):
   # commission_rate = 0.19  # 10% commission
    commission_rate = 9 # 9% Comission
    winner = 109 # Comision winner 19%  can be change 119 !
    commission = sale_amount * commission_rate / winner
    return commission

# Example usage
while True:
    
    sale = float(input("Enter your value: "))  # Sale amount of $1000
    if sale == float:
        print("Well done")
        continue
    else:
        print("It's astring cannnot tranform.")
        break

    
        

result = calculate_commission(sale)
print(f"For a sale of ${sale}, the 9% commission is ${result:.2f}")
