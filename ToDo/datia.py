import json
f = open('mio.json')
mio = json.load(f)

#Iteration through the json\

for Capota in mio['Capota']:
    print(Capota['fabricat'])

f.close()
