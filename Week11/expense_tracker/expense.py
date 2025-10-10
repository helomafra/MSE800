class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    
    def __str__(self):
        """
        Returns string representation of the expense.
        
        >>> expense = Expense("Coffee", 3.50)
        >>> str(expense)
        'Coffee: $3.50'
        >>> expense2 = Expense("Lunch", 15.00)
        >>> str(expense2)
        'Lunch: $15.00'
        """
        return f"{self.description}: ${self.amount:.2f}"
