class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"Starting the {self.year} {self.make} {self.model}'s engine.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"Stopping the {self.year} {self.make} {self.model}'s engine.")
            self.is_running = False
            self.speed = 0
        else:
            print("The engine is already off.")

    def accelerate(self, speed_increase):
        if self.is_running:
            self.speed += speed_increase
            print(f"The car is now moving at {self.speed} mph.")
        else:
            print("You need to start the engine first.")

    def brake(self, speed_decrease):
        if self.speed > 0:
            self.speed = max(0, self.speed - speed_decrease)
            print(f"The car is now moving at {self.speed} mph.")
        else:
            print("The car is already stationary.")

    def honk(self):
        print("Beep! Beep!")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"


# Usage example
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2022, "Blue")
    print(my_car)  # Calls the __str__ method

    my_car.start_engine()
    my_car.accelerate(30)
    my_car.honk()
    my_car.brake(10)
    my_car.stop_engine()

    # Creating another instance
    luxury_car = Car("Mercedes", "S-Class", 2023, "Black")
    print(luxury_car)
    luxury_car.start_engine()
    luxury_car.accelerate(50)