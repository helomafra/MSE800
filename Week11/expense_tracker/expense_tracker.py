from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)
        return expense
    
    def calculate_total(self):
        return sum(expense.amount for expense in self.expenses)

    def __str__(self):
        if not self.expenses:
            return "No expenses recorded."
        
        result = "Expenses:\n"
        for expense in self.expenses:
            result += f"  {expense}\n"
        result += f"Total: ${self.calculate_total():.2f}"
        return result
