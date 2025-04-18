import json

with open('astro.json', 'r') as file:
    data = json.load(file)

#print(data["stars"][0]["name"])  # Output: "Sun"


def astro_tech():
    while True:
        print("=====All about the Stars.")
        search = input("Please enter stars detail: ")

        if search == "mass_stars":
            for i in data['stars']:
             print(i["mass"])
             continue
        elif search == "all_stars":
            for i in data['stars']:
                print(i["name"] )

        else:
            print("Good Bye!")
            break


astro_tech()





