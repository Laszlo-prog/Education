dict1 = {"Marca":'Alfa', "Model":'Romeo', "Fabricat": 2018}


def search_dict1():
    value = input("Enter a item:")
    if value in dict1:
        print("Name found", dict1[value])
    else:
        print("Name not found")

def keres_dict1():
    key = input("Enter a Key:")
    if key in dict1:
        print("Key found",dict1[key])
    else:
        print("Not found")

def add_new_item():
    key = input("Enter a key:")
    value = input("Enter value:")
    dict1[key]= value
    print(dict1)
    entry = input("Add new item Y or N:")
    if entry.lower() =="y":
        add_new_item()
    elif entry.lower() == "n":
        print(dict1)
    else:
        search_dict1()

search_dict1()
keres_dict1()
add_new_item()
