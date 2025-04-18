import json


with open('edu.json', 'r') as file:
    data = json.load(file)

#print(data['Verb'])

def myfunction():
    create = input("Enter your validation: ")

    if create == "Verb":
        for i in data['Verb']:
            print(i)
    elif create == "past":
        for i in data['Verb']:
            print(i['Past'])
    elif create == "present":
        for i in data['Verb']:
            print(i['Present'])    
    else:
        print('Good by')

def mytech():
    while True:
        print("======Let's Do that=====")
        creator = input("Enter your data: ")
        if creator =="Verbero":
            for i in data['Verb']:
                print(i)
                continue
        elif creator == 'paste':
            for i in data['Verb']:
                print(i['Past'])
        else:
            print("Good By!!")
            break





#print(type(data['Verbs']))
#print(type(data))

#for i in data['Verb']:
    #print(i)

#for i in data['Verb']:
    #print(i['Past'])

#for Verb in data['Verb']:
    #print(Verb)

#for Verb in data['Verb']:
   #print(Verb['Past'], Verb['Present'])   
myfunction()
mytech()

