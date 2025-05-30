import json

with open('mai.json', 'r') as file:
    data = json.load(file)

for i in data['Usa']:
    print(i)

print(data)

