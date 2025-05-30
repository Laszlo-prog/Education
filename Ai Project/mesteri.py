import random
secret_number = random.randint(1, 25)
guess = None
print(" Hello! You must match the password!")
print("I'm thinking of a number between 1 and 25")
def my_number(guess):

 while guess != secret_number:
    guess = input('Enter your number: ')

 if guess != secret_number:
    print("Too low! Try again.")
 elif guess != secret_number:
    print("Too high my friend!! Try again.")
 else:
    print(f"Congratulation! You guessed the number {secret_number}correctly!")
print("Thanks for playing!")
if __name__ =="__main__":
    my_number(guess)
