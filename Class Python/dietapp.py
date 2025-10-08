class DietApp:
    def __init__(self):
        self.daily_calories = 0
        self.calories_goal = None
        self.meals = []

    def set_calories_goal(self):
        try:
            self.calories_goal = int(input("Enter your daily calories goal: "))
            print(f"Daily calories goal set to {self.calories_goal} calories.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def add_meal(self):
        try:
            meal_name = input("Enter meal name: ")
            calories = int(input(f"Enter calories for {meal_name}: "))
            self.meals.append((meal_name, calories))
            self.daily_calories += calories
            print(f"Added {meal_name} with {calories} calories.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_meals(self):
        if not self.meals:
            print("No meals recorded yet.\n")
        else:
            print("Meals recorded:")
            for meal_name, calories in self.meals:
                print(f"{meal_name}: {calories} calories")
            print(f"Total daily calories: {self.daily_calories} calories\n")  
    def view_summary(self):  
        print("Daily Summary:")
        print(f"Total calories consumed: {self.daily_calories} calories")
        if self.calories_goal:
            if self.daily_calories > self.calories_goal:
                print(f"You have exceeded your daily goal by {self.daily_calories - self.calories_goal} calories.")
            else:
                print(f"You are within your daily goal by {self.calories_goal - self.daily_calories} calories.")
        else:
            print("No daily calories goal set.\n")

    def run(self):
        while True:
            print("Diet App Menu:")
            print("1. Set Daily Calories Goal")
            print("2. Add Meal")
            print("3. View Meals")
            print("4. View Daily Summary")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")
            if choice == '1':
                self.set_calories_goal()
            elif choice == '2':
                self.add_meal()
            elif choice == '3':
                self.view_meals()
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                print("Exiting the Diet App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")   
if __name__ == "__main__":
    app = DietApp()
    app.run()         
