import unittest
from expense_tracker import ExpenseTracker
from expense import Expense

class TestExpense(unittest.TestCase):
    """Test cases for Expense class."""

    def test_add_expense(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Rent", 1000)
        self.assertEqual(len(tracker.expenses), 1)

        expense_description = tracker.expenses[0].description
        expense_amount = tracker.expenses[0].amount

        self.assertEqual(expense_description, "Rent")
        self.assertEqual(expense_amount, 1000)

    def test_calculate_total(self): 
        tracker = ExpenseTracker()
        tracker.add_expense("Rent", 1000)
        tracker.add_expense("Food", 200)

        total = tracker.calculate_total()
        self.assertEqual(total, 1200)

    def test_calculate_total_empty_list(self):
        tracker = ExpenseTracker()
        total = tracker.calculate_total()
        self.assertEqual(total, 0)

    def test_add_expense_with_decimals(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Coffee", 3.50)
        
        self.assertEqual(len(tracker.expenses), 1)
        self.assertEqual(tracker.expenses[0].amount, 3.50)

    def test_add_expense_zero_amount(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Free item", 0)
        
        self.assertEqual(len(tracker.expenses), 1)
        self.assertEqual(tracker.expenses[0].amount, 0)

    def test_add_expense_returns_expense_object(self):
        tracker = ExpenseTracker()
        expense = tracker.add_expense("Test", 100)
        
        self.assertIsInstance(expense, Expense)
        self.assertEqual(expense.description, "Test")
        self.assertEqual(expense.amount, 100)

    def test_str_representation_empty(self):
        tracker = ExpenseTracker()
        self.assertEqual(str(tracker), "No expenses recorded.")

    def test_str_representation_with_expenses(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Rent", 1000)
        tracker.add_expense("Food", 200)
        
        expected = "Expenses:\n  Rent: $1000.00\n  Food: $200.00\nTotal: $1200.00"
        self.assertEqual(str(tracker), expected)

    def test_multiple_expenses(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Rent", 1000)
        tracker.add_expense("Food", 200)
        tracker.add_expense("Transport", 150)
        
        self.assertEqual(len(tracker.expenses), 3)
        self.assertEqual(tracker.calculate_total(), 1350)

if __name__ == '__main__':
    unittest.main()
