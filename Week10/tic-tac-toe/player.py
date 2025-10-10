"""
Player class for Tic-Tac-Toe game.
Handles player information and move input.
"""

import sys

class Player:
    """Represents a player in the Tic-Tac-Toe game."""

    def __init__(self, name, symbol):
        """
        Initialize a player.

        Args:
            name (str): Player's name
            symbol (str): Player's symbol ('X' or 'O')
        """
        self.name = name
        self.symbol = symbol

    def get_move(self):
        """
        Get player's move input.

        Returns:
            tuple: (row, col) coordinates for the move
        """
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter your move (row, col): ")

                # Remove parentheses and split by comma
                move = move.strip('()')
                row, col = map(int, move.split(','))

                # Convert to 0-based indexing
                row -= 1
                col -= 1

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input! Please enter numbers between 1 and 3.")
                    continue

                return row, col

            except ValueError:
                print("Invalid input! Please enter format (row, col) with numbers between 1 and 3.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                sys.exit()

    def __str__(self):
        """String representation of the player."""
        return f"{self.name} ({self.symbol})"
