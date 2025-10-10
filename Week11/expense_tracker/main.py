"""
Week 11 - Activity 2: Personal Expense Tracker with Using Unit Testing

Develop a program using Object-Oriented Programming (OOP) and Unit-testing to create a simple Personal Expense Tracker.
The system should include at least two main functionalities:
Add Expense : Allow the user to add a new expense with a description and an amount.
Calculate Total Expense : Compute and display the total amount of all recorded expenses.
"""

from expense_tracker import ExpenseTracker

def main():
    print("=== Personal Expense Tracker ===")
    
    tracker = ExpenseTracker()

    def menu():
        print("1. Add Expense")
        print("2. Calculate Total Expense")
        print("3. Exit")
        choice = input("Select an option (1-3): ")
        return choice

    while True:
        choice = menu()
        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)
        elif choice == "2":
            print(tracker)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
 