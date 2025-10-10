from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)
        return expense
    
    def calculate_total(self):
        """
        Calculates the total amount of all expenses.
        
        >>> tracker = ExpenseTracker()
        >>> tracker.calculate_total()
        0
        >>> _ = tracker.add_expense("Coffee", 3.50)
        >>> _ = tracker.add_expense("Lunch", 15.00)
        >>> tracker.calculate_total()
        18.5
        """
        return sum(expense.amount for expense in self.expenses)

    def __str__(self):
        if not self.expenses:
            return "No expenses recorded."
        
        result = "Expenses:\n"
        for expense in self.expenses:
            result += f"  {expense}\n"
        result += f"Total: ${self.calculate_total():.2f}"
        return result
