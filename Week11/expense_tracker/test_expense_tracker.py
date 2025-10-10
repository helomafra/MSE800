import unittest
from expense import Expense
from expense_tracker import ExpenseTracker

class TestExpense(unittest.TestCase):
    """Test cases for Expense class."""

    tracker = ExpenseTracker()
    
    def test_add_expense(self):
        self.tracker.add_expense("Rent", 1000)
        self.assertEqual(len(self.tracker.expenses), 1)

        expense_description = self.tracker.expenses[0].description
        expense_amount = self.tracker.expenses[0].amount

        self.assertEqual(expense_description, "Rent")
        self.assertEqual(expense_amount, 1000)


    def test_calculate_total(self): 
        # already added one expense in test_add_expense
        self.tracker.add_expense("Food", 200)

        total = self.tracker.calculate_total()
        self.assertEqual(total, 1200)

if __name__ == '__main__':
    unittest.main()
