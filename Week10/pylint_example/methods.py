"""Module for string analysis operations."""


class StringAnalysis:
    """Class for analyzing string properties."""

    def __init__(self, string):
        """Initialize with a string to analyze."""
        self.string = string

    def calculate_length(self):
        """Calculate the length of the string."""
        return len(self.string)

    def count_uppercase(self):
        """Count the number of uppercase characters in the string."""
        return sum(1 for char in self.string if char.isupper())


string_analysis = StringAnalysis("Hello, World!")
