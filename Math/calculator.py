number1 = input('Enter first number:')
num1 = int(number1)
sign = input('Enter the sign:')
number2 = input('Enter second number:')
num2 = int(number2)

if sign == '+1':
    print('Your result is: ' + str(num1 +num2))
elif sign == '-':
    print('Your result is:' + str(num1 -num2))
elif sign =='*':
    print('Your result is: ' + str(num1 *num2))
elif sign =='/':
    print('Your result is: ' +str(num1 /num2))

else:
    print('please enter +, -, * or /')