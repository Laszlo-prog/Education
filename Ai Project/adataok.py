import json

from classic import result

sample_json = {
    "name": "Balint Foro laszlo",
    "age": 34,
    "hobbies": [
        "reasding",
        "swimming",
        "music",
        "panting",
        "Cycling"
    ],
    "addres": "Arad, Strada Solomon.",
    "movies": [
        "Ring of Power",
        "Wheel of Time",
        "NCIS"
    ]


}
#1 Writing Json file
def write_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 6)
    print(f"Data writen to {filename}")
#2 Reading json file:
def read_json(filename='data.json'):
    with open(filename, 'r') as f:
     data = json.load(f)
    return data

# Modifying json file and data
def modify_json(data):
    data['addres'] = 'Arad, Str Solomon'

    #eEntru data modify
    data['age'] = 34
    #Be set youre data
    data['name'] = 'Balint Foro Laszlo'

    data['hobbies'].append('swimming')
    return data
def delete_from_json(data, key):
    if key in data:
        del data[key]
    else:
        print(f"{key}not found in the data.")

    return data
#search you data with engine.

def search_json(data, key, value):
    results = []
    if isinstance(data, dict):
        for k, v in data.item():
            if k == key and v == value:
             results.append(data)
            elif isinstance(v, (dict, list)):
             results.extend(search_json(v, key, value))
    elif isinstance(data, list):
        for itme in data:
            results.extend(search_json( v, key, value ))
    return results

if __name__ =="__main__":
    write_json(sample_json)

    data = read_json()
    print("Initial data:", data)

    modified_data = modify_json(data)
    print("Modified data:", modified_data )

    modified_data = delete_from_json(modified_data, 'name')

    search_result = search_json(modified_data, 'hobbies', 'swimming')
    print("Search result: ", search_result)

    write_json(modified_data)



