def analyze_type(data):
    match data:
        case int():
            print(f"{data}is an integer.")
            if data % 2 == 0:
                print('Its an even number.')
            else:
                print('Its an odd number.')
        case str():
            print(f"{data} is a string")
            print(f"Its lenght is{len(data)} characters.")
        case list():
            print(f"{data} is a list")
            print(f"Its contain {len(data)} elements")
        case dict():
            print(f"{data} is a dictionary")
            print(f"It contains {len(data)} key-value paris.")
        case _:
            print(f"The type of {data} is {type(data)}.")
            print(" I dont have specific handling for this type")


analyze_type(42)
analyze_type("Hello wolrd")
analyze_type([1, 2, 3, 4, 5])
analyze_type({"name":"Laszlo", "age": 34})
analyze_type(3.14)


