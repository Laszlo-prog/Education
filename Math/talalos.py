import random
number_to_guess = random.randint(1, 10)
while True:
 try:
    guess = int(input('Guess number between 1 and 10: '))
    if guess < number_to_guess:
        print('low!')
    elif guess > number_to_guess:
        print('high!')
    else:
       print('You are won!!')
       break
 except ValueError:
    print('Please enter a valid number')
 

