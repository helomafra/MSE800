"""Week 10 - Activity 1: Use Pylint.

Develop an Object-Oriented (OO) Python project that reads either a string or a list,
then performs two analyses:
- Calculates the total length.
- Determines the number of uppercase characters.

The project should be structured with appropriate classes and methods.
After implementation, use Pylint to analyze and improve the code quality,
ensuring adherence to Python's best practices and style guidelines.
"""
from methods import StringAnalysis

def main():
    """Main function to demonstrate string analysis."""
    string_analysis = StringAnalysis("Hello, World!")
    print(string_analysis.calculate_length())
    print(string_analysis.count_uppercase())


if __name__ == "__main__":
    main()
