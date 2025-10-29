class FoodItem:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

#Class to handle calorie counter
class CalorieCounter:
    def __init__(self):
        self.items = []

    #add food item
    def add_item(self, name, calories):
        self.items.append(FoodItem(name, calories))

    #view total calories

    def view_total(self):
        if not self.items:
            print("No food items logged.")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name}: {item.calories} kcal")

    #Get total calories
    def total_calories(self):
        total = sum(item.calories for item in self.items)

        print(f"Total Calories Consumed:{total} kcal")
    #Main function for menu interaction

    def menu():
        counter = CalorieCounter()

        while True:
            print("\nCalorie Counter Menu:")
            print("1. Add Food Item")
            print("2. View Food Items")
            print("3. View Total Calories")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter food item name: ")
                calories = float(input("Enter calories for the item: "))
                counter.add_item(name, calories)
                print(f"{name} added with {calories} kcal.")

            elif choice == '2':
                counter.view_total()

            elif choice == '3':
                counter.total_calories()

            elif choice == '4':
                print("Exiting Calorie Counter.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    CalorieCounter.menu()
    






