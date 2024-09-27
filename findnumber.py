import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 25)

# Initialize guess to None
guess = None

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 25.")

# Start the while loop
while guess != secret_number:
    # Get user input
    guess = input("Enter your guess: ")
    
    # Convert input to integer
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")

print("Thanks for playing!")
