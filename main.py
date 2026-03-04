"""
TicTacToe Game - Main Entry Point
"""

from game import TicTacToe


def main():
    """Main game loop entry point"""
    game = TicTacToe()
    players = ['X', 'O']
    current_player_index = 0
    
    print("Welcome to TicTacToe!")
    print("Players will take turns entering row and column positions (0-2)")
    print("Example: row 0, col 1 places your mark at top-middle")
    
    while True:
        game.display_board()
        current_player = players[current_player_index]
        
        print(f"Player {current_player}'s turn")
        
        # Get and validate player input
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
            
            is_valid, error_msg = game.is_valid_move(row, col)
            if not is_valid:
                print(f"Invalid move: {error_msg}")
                continue
            
            if game.make_move(row, col, current_player):
                break
        
        # Switch to next player
        current_player_index = 1 - current_player_index


if __name__ == "__main__":
    main()
