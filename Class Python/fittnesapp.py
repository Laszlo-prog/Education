import time

class FitnessApp:
    def __init__(self):
        self.user_name = ""
        self.weight = 0
        self.height = 0
        self.goal == ""
        self.water_intake = 0
        self.calories_consumed = 0
        self.progress_log = []

    def register_user(self):
        self.user_name = input("Enter your name: ")
        self.weight = float(input("Enter your weight (kg): "))
        self.height = float(input("Enter your height (cm): "))
        self.goal = input("Enter your fitness goal (e.g., lose weight, gain muscle): ")
        print(f"User {self.user_name} registered successfully!")

    def workout_plan(self):
        print("\nWorkout Plan:")

        if "lose" in self.goal.lower():
            print("Focus on cardio and strength training.")
        elif "gain" in self.goal.lower():
            print("Focus on strength training and high-protein diet.")
        else:
            print("Maintain a balanced workout routine.")
    def track_calories(self):
        self.calories_consumed = float(input("Enter calories consumed today: "))
        print(f"Calories consumed today: {self.calories_consumed} kcal")
    def hidration_reminder(self):
        self.water_intake = float(input("Enter water intake today (liters): "))
        print(f"Water intake today: {self.water_intake} liters")
    
    def daily_challenge(self):
        challenge = [
            "Run 5 km",
            "Do 50 push-ups",
            "Complete a 30-minute yoga session",
            "Drink 2 liters of water",
            "Prepare a healthy meal"
        ]

        print("\nToday's Challenge:")
    def track_progress(self):
        date = time.strftime("%Y-%m-%d")
        weight = float(input("Enter your current weight (kg): "))
        self.progress_log.append((date, weight))
        print(f"Progress logged for {date}: {weight} kg")

    def menu(self):
        while True:
            print("\nFitness App Menu:")
            print("1. Register User")
            print("2. Workout Plan")
            print("3. Track Calories")
            print("4. Hydration Reminder")
            print("5. Daily Challenge")
            print("6. Track Progress")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.workout_plan()
            elif choice == "3":
                self.track_calories()
            elif choice == "4":
                self.hidration_reminder()
            elif choice == "5":
                self.daily_challenge()
            elif choice == "6":
                self.track_progress()
            elif choice == "7":
                print("Exiting the app. Stay fit!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = FitnessApp()
    app.menu()
