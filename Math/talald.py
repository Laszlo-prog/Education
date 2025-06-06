import random
 
while True:
    user = input("Please insert a new value(Y/N): ")
    if user == 'Y':
        die1 = random.randint( 2, 50)
        die2 = random.randint(1, 45)
        print(f'({die1}, {die2})')
    elif user == 'N':
        print("Thank for playing")
        break
    else:
        print('Goodbye')

