"""
Game class for Tic-Tac-Toe.
Manages the game flow, turns, and win detection.
"""

from board import Board
from player import Player


class Game:
    """Main game class that manages the Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize a new game."""
        self.board = Board()
        self.players = []
        self.current_player_index = 0

    def setup_players(self):
        """Setup the two players for the game."""
        print("Welcome to Tic-Tac-Toe!")
        print("=" * 30)

        # Get player names
        player1_name = input("Enter Player 1 name: ").strip()
        if not player1_name:
            player1_name = "Player 1"

        player2_name = input("Enter Player 2 name: ").strip()
        if not player2_name:
            player2_name = "Player 2"

        # Create players
        self.players = [
            Player(player1_name, 'X'),
            Player(player2_name, 'O')
        ]

        print(f"\n{self.players[0]} vs {self.players[1]}")
        print("Let's start the game!\n")

    def get_current_player(self):
        """Get the current player."""
        return self.players[self.current_player_index]

    def switch_player(self):
        """Switch to the next player."""
        self.current_player_index = (self.current_player_index + 1) % 2

    def play_turn(self):
        """
        Play one turn of the game.

        Returns:
            bool: True if game should continue, False if game is over
        """
        current_player = self.get_current_player()
        self.board.display()

        while True:
            row, col = current_player.get_move()

            if self.board.make_move(row, col, current_player.symbol):
                break
            print("That position is already taken! Please choose another.")

        # Check for winner
        winner = self.board.check_winner()
        if winner:
            self.board.display()
            print(f"🎉 Congratulations! {current_player.name} wins!")
            return False

        # Check for draw
        if self.board.is_full():
            self.board.display()
            print("It's a draw! 🤝")
            return False

        # Switch to next player
        self.switch_player()
        return True

    def play(self):
        """Main game loop."""
        self.setup_players()

        while True:
            if not self.play_turn():
                break

        self.play_again()

    def play_again(self):
        """Ask if players want to play again."""
        while True:
            choice = input("\nDo you want to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                self.reset_game()
                self.play()
                break
            if choice in ['n', 'no']:
                print("Thanks for playing! 👋")
                break
            print("Please enter 'y' for yes or 'n' for no.")

    def reset_game(self):
        """Reset the game for a new round."""
        self.board = Board()
        self.current_player_index = 0
        print("\n" + "=" * 30)
        print("New game starting!")
        print("=" * 30)
