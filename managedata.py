import json

# Sample JSON data
sample_json = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "cycling"]
}

# 1. Writing JSON to a file
def write_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data written to {filename}")

# 2. Reading JSON from a file
def read_json(filename='data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# 3. Modifying JSON data
def modify_json(data):
    # Add a new key-value pair
    data['email'] = 'john@example.com'
    
    # Modify an existing value
    data['age'] = 31
    
    # Add a new hobby
    data['hobbies'].append('painting')
    
    return data

# 4. Deleting from JSON data
def delete_from_json(data, key):
    if key in data:
        del data[key]
        print(f"Deleted '{key}' from the data")
    else:
        print(f"'{key}' not found in the data")
    return data

# 5. Searching in JSON data
def search_json(data, key, value):
    results = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key and v == value:
                results.append(data)
            elif isinstance(v, (dict, list)):
                results.extend(search_json(v, key, value))
    elif isinstance(data, list):
        for item in data:
            results.extend(search_json(item, key, value))
    return results

# Example usage
if __name__ == "__main__":
    # Write initial data to file
    write_json(sample_json)
    
    # Read data from file
    data = read_json()
    print("Initial data:", data)
    
    # Modify data
    modified_data = modify_json(data)
    print("Modified data:", modified_data)
    
    # Delete a key
    modified_data = delete_from_json(modified_data, 'city')
    
    # Search in data
    search_result = search_json(modified_data, 'hobby', 'swimming')
    print("Search result:", search_result)
    
    # Write modified data back to file
    write_json(modified_data)
