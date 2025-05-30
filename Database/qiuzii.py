import json
import random
from typing import List, Dict, Optional

class Question:
    """Class to represent a single quiz question"""
    def __init__(self, text: str, choices: List[str], answer: str):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, user_answer: str) -> bool:
        """Check if user's answer is correct"""
        return user_answer.lower() == self.answer.lower()
    
    def shuffle_choices(self):
        """Shuffle the answer choices"""
        random.shuffle(self.choices)

class Quiz:
    """Class to manage the quiz game"""
    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
    
    def get_current_question(self) -> Optional[Question]:
        """Get the current question"""
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    
    def next_question(self):
        """Move to the next question"""
        self.current_question_index += 1
    
    def check_answer(self, user_answer: str) -> bool:
        """Check the answer for the current question"""
        current_question = self.get_current_question()
        if current_question and current_question.check_answer(user_answer):
            self.score += 1
            return True
        return False
    
    def has_more_questions(self) -> bool:
        """Check if there are more questions remaining"""
        return self.current_question_index < len(self.questions)
    
    def get_score(self) -> str:
        """Get the current score as a string"""
        return f"Score: {self.score}/{len(self.questions)}"

class QuizGame:
    """Class to handle the game interface"""
    def __init__(self, quiz_data: List[Dict]):
        # Create Question objects from the quiz data
        questions = []
        for item in quiz_data:
            question = Question(
                text=item["question"],
                choices=item["choices"],
                answer=item["answer"]
            )
            question.shuffle_choices()
            questions.append(question)
        
        # Shuffle all questions
        random.shuffle(questions)
        self.quiz = Quiz(questions)
    
    def start(self):
        """Start the quiz game"""
        print("Welcome to the Python Quiz Game!")
        print("Answer the questions to test your knowledge.\n")
        
        while self.quiz.has_more_questions():
            current_question = self.quiz.get_current_question()
            
            print(f"\nQuestion: {current_question.text}")
            for idx, choice in enumerate(current_question.choices, start=1):
                print(f"{idx}. {choice}")
            
            # Get user input with validation
            while True:
                try:
                    user_choice = int(input("\nYour answer (number): "))
                    if 1 <= user_choice <= len(current_question.choices):
                        break
                    print(f"Please enter a number between 1 and {len(current_question.choices)}")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Check answer
            selected_answer = current_question.choices[user_choice - 1]
            if self.quiz.check_answer(selected_answer):
                print("Correct! 🎉")
            else:
                print(f"Wrong! The correct answer was: {current_question.answer}")
            
            print(self.quiz.get_score())
            self.quiz.next_question()
        
        print("\nQuiz completed!")
        print(f"Your final score: {self.quiz.score}/{len(self.quiz.questions)}")
        self._show_final_message()
    
    def _show_final_message(self):
        """Show a message based on the final score"""
        percentage = (self.quiz.score / len(self.quiz.questions)) * 100
        
        if percentage >= 80:
            print("Excellent! You're a Python expert! 🐍")
        elif percentage >= 60:
            print("Good job! You know quite a bit about Python.")
        elif percentage >= 40:
            print("Not bad! Keep learning Python.")
        else:
            print("Keep practicing! Python is fun to learn.")

# Sample quiz data
quiz_data = [
    {
        "question": "What is the correct way to create a class in Python?",
        "choices": [
            "class MyClass:",
            "def MyClass():",
            "new class MyClass:",
            "create MyClass:"
        ],
        "answer": "class MyClass:"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "choices": [
            "list",
            "tuple",
            "array",
            "dict"
        ],
        "answer": "array"
    },
    {
        "question": "How do you start a for loop in Python?",
        "choices": [
            "for x in y:",
            "for (x in y)",
            "for x in range(y)",
            "loop x in y:"
        ],
        "answer": "for x in y:"
    },
    {
        "question": "What does OOP stand for?",
        "choices": [
            "Object-Oriented Programming",
            "Object-Optimized Process",
            "Optional Object Protocol",
            "Operational Object Programming"
        ],
        "answer": "Object-Oriented Programming"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": [
            "func",
            "def",
            "function",
            "define"
        ],
        "answer": "def"
    },

    {
        "question": "Who invented Python?",
        "choices": [
            "Mark Anthony",
            "Jenifer Lopez",
            "Guido van Rossum",
            "Abba"
        ],
        "answer": "Guido van Rossum"
    },
]

# Load and start the game
if __name__ == "__main__":
    game = QuizGame(quiz_data)
    game.start()