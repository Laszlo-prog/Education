def analyze_type(data):
    match data:
        case int():
            print(f"{data} is an integer.")
            if data % 2 == 0:
                print("It's an even number.")
            else:
                print("It's an odd number.")
        case str():
            print(f"'{data}' is a string.")
            print(f"Its length is {len(data)} characters.")
        case list():
            print(f"{data} is a list.")
            print(f"It contains {len(data)} elements.")
        case dict():
            print(f"{data} is a dictionary.")
            print(f"It contains {len(data)} key-value pairs.")
        case _:
            print(f"The type of {data} is {type(data)}.")
            print("I don't have specific handling for this type.")

# Test the function with different types
analyze_type(42)
analyze_type("Hello, World!")
analyze_type([1, 2, 3, 4, 5])
analyze_type({"name": "Alice", "age": 30})
analyze_type(3.14)
