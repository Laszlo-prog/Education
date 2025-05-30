num = int(input("Enter a number: "))
sum_of_digits = 0
while num !=0:
    sum_of_digits += num % 10
    num = num // 10
    if num == 3:
        print("welcome!!!")
        break
    print(f"Sum of digit of number is: {sum_of_digits}")

