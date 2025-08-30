# Week 5 Activity 4: learning about overriding methods 
# Use the attached file to demonstrate method overriding. Update the attached Python code accordingly and share your GitHub link.
 
class Person:
  def __init__(self, name, address, age, id):
    self.name = name
    self.age = age
    self.address = address
    self.id = id

  def greet(self):
    print(f"Hello, my name is {self.name}")

class Student(Person):
  def __init__(self, name, address, age, id, academic_record):
    super().__init__(name, address, age, id)
    self.academic_record = academic_record

  def greet(self):
    print(f"Hi there! I'm {self.name}, a student with academic record: {self.academic_record}")

class Academics(Person):
  def __init__(self, name, address, age, id, tax_code, salary):
    super().__init__(name, address, age, id)
    self.tax_code = tax_code
    self.salary = salary

  def greet(self):
    print(f"Good day! I'm Dr. {self.name}, an academic staff member.")

class GeneralStaff(Person):
  def __init__(self, name, address, age, id, tax_code, pay_rate):
    super().__init__(name, address, age, id)
    self.tax_code = tax_code
    self.pay_rate = pay_rate

  def greet(self):
    print(f"Hello! I'm {self.name}, general staff member. How can I help you today?")

def main():
  student = Student("John Doe", "123 Main St", 20, "1234567890", "A")
  academics = Academics("Jane Doe", "456 Main St", 30, "1234567890", "1234567890", 100000)
  general_staff = GeneralStaff("Jim Doe", "789 Main St", 40, "1234567890", "1234567890", 100000)

  print("Person base class:")
  person = Person("Generic Person", "Generic Address", 25, "0000000000")
  person.greet()
  
  print("\nStudent (overridden greet method):")
  student.greet()
  
  print("\nAcademics (overridden greet method):")
  academics.greet()
  
  print("\nGeneral Staff (overridden greet method):")
  general_staff.greet()

if __name__ == "__main__":
    main()