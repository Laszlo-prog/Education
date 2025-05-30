import json

f = open ('lot.json')
lot = json.load(f)

# Iterating through the json
# list
for employes in lot['employes']:
    print(employes)

# Closing file
f.close()
  



    
    
    
