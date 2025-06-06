while True:
    print("Please enter youre name: ")
    name = input()
    if name == "Laszlo":
        break
    elif name == "Player":
        print("Try again")
        continue
    elif name == "Balint":
        print(exit)
    else:

       print("Let's Go!!")




operator = input("Enter on operator (+ - * /):")
num1 = str(input("Enter first words:"))
num2 = str(input("Enter second words:"))
num3 = str(input("Enter a third words: "))
num4 = str(input("Enter a fourth words: "))
num5 = str(input("Enter a fifth words: "))



#print(num1 + num2)
if operator == "+":
    result = num1 + num2 + num3 + num4 + num5
    print(f"Name:{num1} + {num2}+ {num3} + {num4} + {num5}")
elif operator == "-":
    result = num1 - num2
    print(f"result{num1} - {num2}")
elif operator == "*":
    result = num1 * num2
    print(f"result")
elif operator == "/":
    result = num1 / num2
    print(f"result")

