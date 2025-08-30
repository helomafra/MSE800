# Week 5 Activity 5: question - when we can use inheritance?
# Can we update the code with adding a "Course" class to Week 5, Activity 3? See attached file: 
 
class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}, ID: {self.id}")

# ✅ GOOD INHERITANCE: Student IS A Person
class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        super().__init__(name, address, age, id)  # Inherit common attributes
        self.academic_record = academic_record
    
    def display_info(self):
        super().display_info()  # Use parent's method
        print(f"Academic Record: {self.academic_record}, Role: Student")

# ✅ GOOD INHERITANCE: Academics IS A Person
class Academics(Person):
    def __init__(self, name, address, age, id, tax_code, salary):
        super().__init__(name, address, age, id)  # Inherit common attributes
        self.tax_code = tax_code
        self.salary = salary
    
    def display_info(self):
        super().display_info()  # Use parent's method
        print(f"Tax Code: {self.tax_code}, Salary: ${self.salary}, Role: Academic")

# ✅ GOOD INHERITANCE: GeneralStaff IS A Person
class GeneralStaff(Person):
    def __init__(self, name, address, age, id, tax_code, pay_rate):
        super().__init__(name, address, age, id)  # Inherit common attributes
        self.tax_code = tax_code
        self.pay_rate = pay_rate
    
    def display_info(self):
        super().display_info()  # Use parent's method
        print(f"Tax Code: {self.tax_code}, Pay Rate: ${self.pay_rate}, Role: General Staff")

# ❌ BAD INHERITANCE:
# class Course(Person):  # Course IS NOT a Person!
#     def __init__(self, id, course_name, course_code):
#         super().__init__(id)  # This would fail - Person needs 4 parameters
#         self.course_name = course_name
#         self.course_code = course_code

# ✅ CORRECT: Course as independent class
class Course:
    def __init__(self, id, course_name, course_code, credits=3):
        self.id = id
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
    
    def display_info(self):
        print(f"Course ID: {self.id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Credits: {self.credits}")

def inheritance():
    student = Student("John Doe", "123 Main St", 20, "S001", "A")
    academic = Academics("Dr. Jane Smith", "456 Oak Ave", 35, "A001", "TAX123", 75000)
    staff = GeneralStaff("Mike Johnson", "789 Pine Rd", 28, "G001", "TAX456", 25)
    
    print("\nStudent (inherits from Person):")
    student.display_info()
    
    print("\nAcademic (inherits from Person):")
    academic.display_info()
    
    print("\nGeneral Staff (inherits from Person):")
    staff.display_info()

def independent_class():
    # Course is NOT a Person - it's a different entity
    course = Course("C001", "Introduction to Programming", "CS101", 4)
    course.display_info()

def main():
    inheritance()
    independent_class()

if __name__ == "__main__":
    main()
