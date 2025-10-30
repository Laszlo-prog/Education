#Create class quiz game for beginner level

class QuizGame:
    def __init__(self):
        self.score = 0
#create name function
    def my_name(self):
        while True:
            print("Most complete your name continued the game!!!")
            name = input("Please enter your name: ")
            if name == "Laszlo":
                print("Welcome to play.")
                break
            elif name == "Balint":
                print("Good job!!")
                continue
            else:
                print("You are not welcome!")
#create question functions
    def question1(self):
        print("Cine a inventat scrisoarea?")
        answer0 = input("Answer here: ")
        if answer0 == "Alfred":
            print('Corect!')
            self.score += 1
        else:
            print("Incorect don't pass.")

    def question2(self):
        print("Cine a fost Hippocrate?")
        answer1 = input("Answer here: ")
        if answer1 == "Tatal medicinei":
            print("Corect!")
            self.score += 1
        else:
            print("Incorect. don't pass")

    def question3(self):
        print("Cine a inventat prima masina electrica?")
        answer2 = input("Answer here: ")
        if answer2 == "Nikolai Tesla":
            print("Corect")
            self.score += 1
        else:
            print("Incorect. Don't pass")

    def question4(self):
        print("Cine a fost primul om pe luna?")
        answer3 = input("Answer here: ")
        if answer3 == "Armstrong":
            print("Corect")
            self.score += 1
        else:
            print("Incorect!! Don't pass!!")

    def question5(self):
        print("Cine a descoperit America?")
        answer4 = input("Answer here: ")
        if answer4 == "Cristofor Columb":
            print("Corect")
            self.score += 1
        else:
            print("Incorect. Don't pass")

    def show_score(self):
        print(f"Your total score is: {self.score}/5")

if __name__ == "__main__":
    game = QuizGame()
    game.my_name()
    game.question1()
    game.question2()
    game.question3()
    game.question4()
    game.question5()
    game.show_score()
