"""
Board class for Tic-Tac-Toe game.
Handles the 3x3 grid display and position management.
"""


class Board:
    """Represents the game board for Tic-Tac-Toe."""

    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.size = 3

    def display(self):
        """Display the current state of the board."""
        print("\n  1   2   3")
        for i in range(self.size):
            print(f"{i+1} {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            if i < self.size - 1:
                print("  --+---+--")
        print()

    def is_valid_move(self, row, col):
        """
        Check if a move is valid.

        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)

        Returns:
            bool: True if move is valid, False otherwise
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        return self.grid[row][col] == ' '

    def make_move(self, row, col, symbol):
        """
        Make a move on the board.

        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            symbol (str): Player symbol ('X' or 'O')

        Returns:
            bool: True if move was successful, False otherwise
        """
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self):
        """
        Check if there's a winner.

        Returns:
            str: Winner symbol ('X' or 'O') if found, None otherwise
        """
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(self.size):
            if (self.grid[0][col] == self.grid[1][col] ==
                    self.grid[2][col] != ' '):
                return self.grid[0][col]

        # Check diagonals
        if (self.grid[0][0] == self.grid[1][1] ==
                self.grid[2][2] != ' '):
            return self.grid[0][0]

        if (self.grid[0][2] == self.grid[1][1] ==
                self.grid[2][0] != ' '):
            return self.grid[0][2]

        return None

    def is_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if board is full, False otherwise
        """
        for row in self.grid:
            if ' ' in row:
                return False
        return True
