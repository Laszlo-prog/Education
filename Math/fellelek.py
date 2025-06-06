name= input("Enter your firstname: ")
def names():
    if name == 'Balint':
        print("Not good but accept.")
    elif name =='Laszlo':
        print('Very good Accept.')
    elif name == 'Foro':
        print('Excellent.')
    else:
        print('Not good Bye!!!')

print(name)

def quiz_game():
    print(f"Welcome to the Quiz Game!{name}")
    print(f"Answer the following questions {name} by typing the letter of your choice (a, b, c, or d).")

    # Questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer": "c"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
            "answer": "b"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["a) Harper Lee", "b) J.K. Rowling", "c) Ernest Hemingway", "d) Mark Twain"],
            "answer": "a"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["a) 0", "b) 1", "c) 2", "d) 3"],
            "answer": "c"
        }
    ]

    score = 0

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").lower()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    # Final score
    print("\nQuiz Completed!")
    print(f"Your final score is {score}/{len(questions)}.")


# Run the quiz game
if __name__ == "__main__":
    names()
    quiz_game()
