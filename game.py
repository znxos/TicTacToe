"""
TicTacToe Game Logic Module
"""


class TicTacToe:
    """Game class for managing Tic-Tac-Toe state and logic"""

    def __init__(self):
        """Initialize the game board with empty spaces"""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        """Display the current state of the game board"""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
