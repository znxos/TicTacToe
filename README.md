# # TicTacToe

## Project Description

TicTacToe is a command-line implementation of the classic Tic-Tac-Toe game. The game allows two human players to play against each other on a 3x3 grid. Players take turns placing their marks (X or O) on the board, and the first player to align three marks in a row, column, or diagonal wins the game. If the board becomes full without a winner, the game ends in a draw.

## Features

- Two-player gameplay (Human vs Human)
- Input validation for invalid moves and out-of-bounds positions
- Clear board display after each move
- Win detection for rows, columns, and diagonals
- Draw detection when the board is full
- Replay option to play multiple games without restarting the program
- User-friendly prompts and error messages

## Prerequisites

- Python 3.x or higher

## Installation

No external dependencies are required. The game uses only Python's standard library.

1. Clone or download the repository
2. Navigate to the project directory

## How to Run

To start the game, run the following command in your terminal:

```bash
python main.py
```

## Gameplay Instructions

1. The game starts with an empty 3x3 board
2. Player X always goes first
3. Players alternate turns entering their move coordinates
4. To place your mark, enter the row (1-3) and column (1-3) when prompted
   - Row 1 is the top, Row 3 is the bottom
   - Column 1 is the left, Column 3 is the right
5. Invalid moves (occupied cells or out-of-bounds positions) will be rejected
6. The game ends when:
   - A player gets three marks in a row, column, or diagonal (that player wins)
   - All 9 cells are filled with no winner (the game is a draw)
7. After the game ends, you can choose to play again or exit

## Example Board Layout

```
 0 | 1 | 2     (columns)
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8

Press Enter to confirm each entry.
```

## File Structure

- `main.py` - Entry point and CLI game loop
- `game.py` - Core game logic and board management
- `README.md` - Project documentation

## Game Example
![vYnmFCKcoW](https://github.com/user-attachments/assets/cf5ff61e-06a3-43e4-9883-94b7889d4b2e)
## License

This project is part of a Software Engineering assignment (Assignment 2).

