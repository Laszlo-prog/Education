import json

f = open('mai.json')
mai = json.load(f)

for Usa in mai['Usa']:
    print(Usa['model'])

f.close()
