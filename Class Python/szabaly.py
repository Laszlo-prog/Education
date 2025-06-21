
class Student:
    def __call__(self, name, house, age):
        self.name = name
        self.house = house
        self.age = age

    
    


def main():
    name = get_name()
    house = get_house()
    age = show_age()

    print(f"{name} from {house} and {age} old")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def show_age():
    return input("Ages:")

if __name__ == "__main__":
    main()
    