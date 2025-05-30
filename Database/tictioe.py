import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner

    def print_board(self):
        # Print the current board state
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Show which number corresponds to which spot (0-8)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Return list of available moves (indices)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Are there any empty squares left?
        return ' ' in self.board

    def num_empty_squares(self):
        # Count empty squares
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Make a move if valid, return True if valid
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the current move caused a win
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:  # Only diagonal if square is 0, 2, 4, 6, 8
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game=True):
    # Play the game with the two players
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')  # Empty line

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            # Switch players
            letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print("It's a tie!")

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

if __name__ == '__main__':
    # Game setup
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    
    print("Welcome to Tic-Tac-Toe!")
    print("Here are the board positions (0-8):")
    
    # Start the game
    play(t, x_player, o_player, print_game=True)