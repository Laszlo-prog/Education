
def user_choice(int):
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice.isdigit() == False:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Choose a number: ")
        
        # Error Message Check
        if choice.isdigit() == False:
            print("Sorry, but you did not enter an integer. Please try again.")
    
    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)
user_choice(int)