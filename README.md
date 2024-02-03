# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game is played in the console and follows standard rules. Players take turns to mark X or O on the board, and the first player to get three marks in a row (horizontally, vertically, or diagonally) wins.

## Usage

To play the game, simply run the provided script in a Python environment. The game will prompt you to choose your marker (X or O) and take turns placing your marker on the board.

```python
python TicTac.py
```

## Code Overview

The code consists of several functions:

- **displayboard(board):** Displays the Tic-Tac-Toe board.
- **p1input():** Takes input from Player 1 to choose their marker (X or O).
- **place_marker(board, marker, position):** Places the specified marker at the given position on the board.
- **wincheck(board, mark):** Checks if the player with the specified marker has won.
- **pos():** Takes input for the position where the player wants to place their marker.
- **gamest():** Main function to start and manage the Tic-Tac-Toe game.

## How to Play

1. Run the script.
2. Player 1 will be prompted to choose X or O.
3. Players take turns entering the position where they want to place their marker.
4. The game continues until a player wins or it ends in a tie.

Enjoy playing Tic-Tac-Toe!
