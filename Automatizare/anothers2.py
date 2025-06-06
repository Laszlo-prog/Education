import random

# Predefined lists of first and last names
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Taylor", "Jordan"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson"]

# Function to generate a random name
def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

# Generate and print 5 random names
for _ in range(2):
    print(generate_name())