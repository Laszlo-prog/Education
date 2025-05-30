from abc import ABC, abstractmethod

class Chargeable(ABC):
    @abstractmethod
    def charge(self, minutes: int):
        pass

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
        self.__fuel_type = fuel_type

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started (Fuel: {self.__fuel_type})")

    def get_fuel_type(self):
        return self.__fuel_type
    

class ElectricCar(Car, Chargeable):
    def __init__(self, brand: str, model: str, battery_kwh: float):
        super().__init__(brand, model, "Electric")
        self.__battery_kwh = battery_kwh  # Private attribute
        self.__charge_level = 0  # Starts at 0%

    def charge(self, minutes: int):  # Implements Chargeable
        charge_per_minute = 0.5  # 0.5% per minute
        self.__charge_level += minutes * charge_per_minute
        print(f"Charged for {minutes} mins. Battery: {min(self.__charge_level, 100)}%")

    def start_engine(self):  # Overrides Car's method
        if self.__charge_level < 10:
            print("Battery too low! Charge first.")
        else:
            print(f"{self.brand} {self.model} silently hums to life! ⚡")

    def get_battery_info(self):  # Encapsulation
        return f"{self.__battery_kwh}kWh ({self.__charge_level}% charged)"
    

class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None

    def assign_car(self, car: Car):
        self.car = car

    def drive(self):
        if self.car:
            print(f"{self.name} is driving {self.car.brand}")
            self.car.start_engine()
        else:
            print("No car assigned!")

    def charge_car(self, minutes: int):
        if isinstance(self.car, Chargeable):  # Check if car is chargeable
            self.car.charge(minutes)
        else:
            print(f"{self.car.brand} isn't electric—can't charge!")
# Create objects
tesla = ElectricCar("Tesla", "Model 3", 75)
driver = Driver("Alice")

# Assign and interact
driver.assign_car(tesla)
print(tesla.get_battery_info())  # Output: "75kWh (0% charged)"

driver.charge_car(30)  # Charges for 30 mins
# Output: "Charged for 30 mins. Battery: 15%"

driver.drive()  
# Output: "Alice is driving Tesla" 
#         "Battery too low! Charge first."

driver.charge_car(200)  # Charge to full
driver.drive()  
# Output: "Tesla Model 3 silently hums to life! ⚡"