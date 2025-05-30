import random
a = 0
b = 2

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
    
        if guess < random_number:
              print("Sorry you must try again!To low")
            
        
        elif guess > random_number:
        
            print("Sorry you must try again. To high")
    
        print(f"Congratulation Laszlo player WON a {random_number}")
    ticket = input("Get your won ticket:")
    while ticket =="":
        print("Happy")
        ticket = input("Enter your ticket:/!")
    print(f"Thank you { ticket}")
       


def computer_guess(x):
    low = 1
    high = 20
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low(L) or correct(C)').lower()

        if feedback == 'h':
            guess = high - 1
        elif feedback == 'l':
            guess = low + 1

    print(f"Is corectly {guess} your computer won!!")


guess(20)
