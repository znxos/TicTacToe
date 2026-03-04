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

    def is_valid_move(self, row, col):
        """
        Check if a move is valid (within bounds and not occupied)
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False, "Position out of bounds. Please enter row and column between 0 and 2."
        
        position = row * 3 + col
        if self.board[position] != ' ':
            return False, "Position already occupied. Choose another position."
        
        return True, ""
