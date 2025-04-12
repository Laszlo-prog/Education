print("========Hello=====")
print("=========Do you like a play?=======")

def my_name():
 while True:
    print("Most complete the name!")
    name = input("Enter youre name: ")
    if name == "Laszlo":
        print("Welcome to play")
        break
    if name == "Balint":
        print("Good welcome.")
        continue
    else:
        print("Not welcome.")





def question():
    print("Who is Nikolai Tesla?")
    answer0 = input("Answer here: ")
    if answer0 == "Inventator":
        print("Very good.")
        if answer0 == " Fizician.":
            print("Good answer.")
    elif answer0 == "Gratest MAN":
        print("Good")
    else:
        print("Incorect!!! Not pass!")

def question0():
    print("What kind of country to find Haga?")
    answer1 = input("Answer here: ")
    if answer1 == "French":
        print("Not good.")
        if answer1 == " Germany":
            print("Almost but not good")
    elif answer1 == "Holland":
        print("Very good it's good")
    else:
        print("It's not corect now!!!")

def question01():
    print("Who write Murder in orient express?")
    answer2 = input("Answer here: ")
    if answer2 == "Robin Cook":
        print("Not good")
        if answer2 == "Agatha Christie":
            print("Very Good")
    elif answer2 == "Charlse Dicken":
        print("Not again.")
    else:
        print("Incorrect answer!!! Dont Pass")


def question02():
    print("Who is Isaac Newton?")
    answer3 = input("Answer here: ")
    if answer3 == "Matematician":
        print("Good")
        if answer3 == "Fizician":
            print("Perfect!")
    elif answer3 == "Astrolog":
        print("Not good")
    else:
        print("Incorect answer!!! Dont Pass")

def question03():
    print("What is Great Britain capital?")
    answer4 = input("Answer here: ")
    if answer4 == 'London':
        print("Well done")
        if answer4 == 'Washington':
            print('Not good')
    elif answer4 == 'Paris':
        print('Not good')
    else:
        print('Incorect!! Dont pass.')


if __name__ == "__main__":
    my_name()
    question()
    question0()
    question01()
    question02()
    
