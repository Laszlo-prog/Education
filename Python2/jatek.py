print("======WELCOME!=====")
name = str(input("Please enter youre name: "))

def my_name(name):
    while True:
        if name == 'Laszlo':
            print("Well done!")
            break
        elif name == 'Balint':
            print("Very well")
            
        else:
            print("Not welcome!!")
            break

print("======My age======")
age = int(input("Please enter you're age: "))

def my_age(age):
    
    while True:
        if age == 24:
            print("well well")
            break
        elif age == 34:
            print("very good")

        else:
            print("Not good")
            break


my_name(name)
my_age(age)


