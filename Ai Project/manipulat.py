import json
from typing import Dict, List

# Sample JSON data
data = {
    "users": [
        {"id": 1, "name": "Alice", "age": 30, "skills": ["python", "java"]},
        {"id": 2, "name": "Bob", "age": 25, "skills": ["javascript"]}
    ],
    "company": "TechCorp"
}


def save_json(data: Dict, filename: str) -> None:
    """Save data to JSON file with proper formatting"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def load_json(filename: str) -> Dict:
    """Load JSON data from file"""
    with open(filename, 'r') as f:
        return json.load(f)


def find_user_by_id(users: List[Dict], user_id: int) -> Dict:
    """Find user by ID"""
    return next((user for user in users if user["id"] == user_id), None)


def add_user(data: Dict, name: str, age: int, skills: List[str]) -> Dict:
    """Add new user to data"""
    new_id = max(user["id"] for user in data["users"]) + 1
    new_user = {
        "id": new_id,
        "name": name,
        "age": age,
        "skills": skills
    }
    data["users"].append(new_user)
    return data


# Example usage
if __name__ == "__main__":
    # Save JSON to file
    save_json(data, "users.json")

    # Load JSON from file
    loaded_data = load_json("users.json")

    # Find user
    user = find_user_by_id(loaded_data["users"], 1)

    # Add new user
    updated_data = add_user(loaded_data, "Charlie", 28, ["python", "golang"])

    # Modify existing data
    for user in updated_data["users"]:
        if "python" in user["skills"]:
            user["skills"].append("django")

    # Convert to string
    json_string = json.dumps(updated_data, indent=2)