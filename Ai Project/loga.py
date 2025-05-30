import math

number = 0
while number != 5:
    print(number)
    number -= 1

print(f"blast off")



# Example: Guess the secret number
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number!")