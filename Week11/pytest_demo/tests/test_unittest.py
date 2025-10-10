# Week 11 - Activity 1: Unit testing
# Develop a test unit for the *, -, / and % functions and add it to the below example. 
# Once completed, please push your updated code to GitHub and share it here.
 
import unittest
from mypackage.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)