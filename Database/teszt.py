
class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand  # Encapsulated attribute
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this!")  # Abstraction

class Car(Vehicle):
    def __init__(self, brand: str, model: str, fuel_type: str):
        super().__init__(brand, model)
        self.__fuel_type = fuel_type  # Private attribute (encapsulation)

    def start_engine(self):  # Polymorphism (override)
        print(f"{self.brand} {self.model}'s engine started (Fuel: {self.__fuel_type})")

    def get_fuel_type(self):  # Getter (encapsulation)
        return self.__fuel_type


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None  # Composition: Driver "has-a" Car

    def assign_car(self, car: Car):
        self.car = car

    def drive(self):
        if self.car:
            print(f"{self.name} is driving {self.car.brand}")
            self.car.start_engine()
        else:
            print("No car assigned!")


# Create objects
my_car = Car("Tesla", "Model S", "Electric")
driver = Driver("Alice")

# Associate objects (composition)
driver.assign_car(my_car)

# Interact
driver.drive()  
# Output: "Alice is driving Tesla" 
#         "Tesla Model S's engine started (Fuel: Electric)"

# Access info (encapsulation)
print(my_car.get_fuel_type())  # Output: "Electric"
