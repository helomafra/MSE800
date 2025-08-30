# Week 5 - activity 2: Develop a Python program that demonstrates the usage of inheritance
 
# Review the attached file and develop code that demonstrates the use of inheritance as a core feature in your OOP implementation. Upload your code to GitHub and share the repository link, including a short comment that explains your understanding.

# Students have: name, address, age, ID, academic record, etc.
# Academics have: name, address, age, ID, tax code, salary, etc.
# General staffs have: name, address, age, ID, tax code, pay rate, etc.

class Person:
  def __init__(self, name, address, age):
    self.name = name
    self.age = age
    self.address = address

  def display(self):
    print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
  def __init__(self, name, address, age, id, academic_record):
    super().__init__(name, address, age)
    self.id = id
    self.academic_record = academic_record

  def display(self):
    super().display()
    print(f"ID: {self.id}, Academic Record: {self.academic_record}, Role: Student")

class Academics(Person):
  def __init__(self, name, address, age, id, tax_code, salary):
    super().__init__(name, address, age)
    self.id = id
    self.tax_code = tax_code
    self.salary = salary

  def display(self):
    super().display()
    print(f"ID: {self.id}, Tax Code: {self.tax_code}, Salary: {self.salary}, Role: Academics")

class GeneralStaff(Person):
  def __init__(self, name, address, age, id, tax_code, pay_rate):
    super().__init__(name, address, age)
    self.id = id
    self.tax_code = tax_code
    self.pay_rate = pay_rate

  def display(self):
    super().display()
    print(f"ID: {self.id}, Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}, Role: General Staff")

def main():
  student = Student("John Doe", "123 Main St", 20, "1234567890", "A")
  academics = Academics("Jane Doe", "456 Main St", 30, "1234567890", "1234567890", 100000)
  general_staff = GeneralStaff("Jim Doe", "789 Main St", 40, "1234567890", "1234567890", 100000)

  student.display()
  academics.display()
  general_staff.display()

if __name__ == "__main__":
    main()


