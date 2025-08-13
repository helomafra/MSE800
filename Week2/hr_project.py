# Week 2 - Activity 6 : Develop a basic HR project using OO
# You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Job Title: {self.job_title}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s Salary increased by {amount}. New salary: {self.salary}")

def main():
    john_doe = Employee("John Doe", 70000, "Software Engineer")
    jane_smith = Employee("Jane Smith", 60000, "Data Analyst")

    john_doe.display_info()
    jane_smith.display_info()

    john_doe.give_raise(10000)

if __name__ == "__main__":
    main()