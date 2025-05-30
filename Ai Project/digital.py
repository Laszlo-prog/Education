num = int(input("Enter the number: "))
sum_of_digit = 0
while num !=0:
    sum_of_digit += num %10
    num = num //10
    if num == 3:
        print('Welcom')
        break
print(f"Sum od digit of number is: {sum_of_digit}")

