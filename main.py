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
        
        # Check game status
        status = game.get_game_status()
        
        if status != 'ongoing':
            game.display_board()
            if status == 'draw':
                print("It's a draw! The board is full with no winner.")
            else:
                print(f"Player {status} wins!")
            
            # Ask for replay
            while True:
                replay = input("\nPlay again? (yes/no): ").lower().strip()
                if replay in ['yes', 'y']:
                    game = TicTacToe()
                    current_player_index = 0
                    break
                elif replay in ['no', 'n']:
                    print("Thanks for playing!")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")
        else:
            # Switch to next player for ongoing game
            current_player_index = 1 - current_player_index


if __name__ == "__main__":
    main()
