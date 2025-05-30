import json

f = open ('letter.json')
letter = json.load(f)

#Call a function!!!
def search_dict1(value):
    item = input("Enter a item:")
    if Capota in letter:
        print("Name found", Capota[value])
    else:
        print("Name not found")


# Iterating through the json
# list
for Capota in letter['Capota']:
    print(Capota['Fabricat'])

# Closing file

search_dict1()
f.close()