class IQTestApp:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is 2 + 2?": "4",
            "What is the largest planet in our solar system?": "Jupiter",
            "What is the chemical symbol for water?": "H2O",
            "Who was Nicolas Tesla?": "Inventor"

        }
        self.score = 0

    def display_menu(self):
        print("Welcome to the IQ Test App!")
        print("1. Take the IQ Test")
        print("2. View Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        action = {
            "1": self.take_test,
            "2": self.view_score,
            "3": self.exit_app

        }
        action.get(choice, self.invalid_choice)()
    def invalid_choice(self):
        print("Invalid choice. Please try again.")
        self.display_menu() 


    def take_test(self): 
        self.score = 0
        for q, a in self.questions.items():
            answer = input(f"{q} ")
            if answer.strip().lower() == a.lower():
                self.score += 1 
        print(f"Your score: {self.score}/{len(self.questions)}")
    def view_score(self):
        print(f"Your current score is: {self.score}/{len(self.questions)}")

    def exit_app(self):
        print("Thank you for using the IQ Test App. Goodbye!")
        exit()
        raise SystemExit

if __name__ == "__main__":
    app = IQTestApp()
    while True:
        app.display_menu()    
