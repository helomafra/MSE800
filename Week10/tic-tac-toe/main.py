"""
Week 10 - Activity 3: Readability, Maintainability & Refactoring- Tic-Tac-Toe - OOP
 
Develop a project using the following tasks: (estimated time 30 minutes for first version of the development)
Design (Top-Down)
Plan the project structure with classes and functions
Each class should have clear methods
Implementation
Create a 3×3 board and display it.
Let two players take turns entering moves.
Detect winner or draw.
Use good OOP practices (encapsulation, methods, and attributes).
Testing
Run and debug the game using - manual testing
Handle invalid inputs.
Code Quality
Run Pylint:
Improve your score by fixing Pylint warnings and following Python style guidelines.
Share your result with sharing GitHub link.
"""

from game import Game

def main():
    """Main function to start the Tic-Tac-Toe game."""
    try:
        game = Game()
        game.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋")
    except (ValueError, EOFError) as e:
        print(f"Input error: {e}")
        print("Please try again.")


if __name__ == "__main__":
    main()
