import random
from typing import List

class Hangman:
    def __init__(self, word_list: List[str], max_attempts: int = 6):
        self.word = random.choice(word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.max_attempts = max_attempts
        self.game_over = False
        self.won = False
    
    def display_word(self) -> str:
        """Display the word with underscores for unguessed letters"""
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append('_')
        return ' '.join(display)
    
    def display_hangman(self) -> str:
        """Return ASCII art of hangman based on attempts left"""
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[self.attempts_left]
    
    def guess_letter(self, letter: str) -> bool:
        """Process a letter guess"""
        letter = letter.upper()
        
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'!")
            return False
        
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.attempts_left -= 1
            print(f"Wrong! '{letter}' is not in the word.")
            if self.attempts_left == 0:
                self.game_over = True
                self.won = False
            return False
        else:
            print(f"Correct! '{letter}' is in the word.")
            
            # Check if all letters have been guessed
            if all(char in self.guessed_letters for char in self.word):
                self.game_over = True
                self.won = True
            return True
    
    def play(self):
        """Main game loop"""
        print("Welcome to Hangman!")
        print(f"You have {self.attempts_left} attempts to guess the word.")
        print(self.display_hangman())
        
        while not self.game_over:
            print("\n" + self.display_word())
            print(f"Attempts left: {self.attempts_left}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
            
            guess = input("Guess a letter: ").strip()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            self.guess_letter(guess)
            print(self.display_hangman())
        
        # Game over message
        if self.won:
            print(f"\nCongratulations! You guessed the word: {self.word}")
        else:
            print(f"\nGame over! The word was: {self.word}")

# Word list for the game
word_list = [
    "python", "programming", "hangman", "computer", "keyboard",
    "developer", "algorithm", "function", "variable", "dictionary",
    "javascript", "internet", "database", "software", "hardware"
]

if __name__ == "__main__":
    game = Hangman(word_list)
    game.play()