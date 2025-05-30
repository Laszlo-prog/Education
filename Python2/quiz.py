
    

def quiz_game():
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        }
    ]

    score = 0

       # Iterate through each question
    for q in questions:
        print("\
" + q["question"])
        for option in q["options"]:
            print(option)

        # Get the player's answer
        answer = input("Your answer (A, B, C, D): ").strip().upper()

        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was " + q["answer"])

    # Display the final score
    print("\
Your final score is: " + str(score) + " out of " + str(len(questions)))

# Run the quiz game
quiz_game()
