# Week 5 - Activity 6.1 : Use the attached file – Different Types of Attributes
# Can you add one more method to the class that uses the private attribute? Also, please create a new class to demonstrate the use of the public and protected attributes. See attached file. See slide 3 : 
# Encapsulation_Python_OOP.pptx
 
class Student:
    def __init__(self, name, age, grade, id):
        self.name = name # public attribute
        self._age = age # protected attribute
        self.__grade = grade # private attribute
        self.__id = id # private attribute
    
    def get_grade(self):
        return self.__grade
    
    def get_id(self):
        return self.__id
    
    # Additional method using private attribute
    def get_academic_status(self):
        if self.__grade == "A":
            return "Excellent"
        elif self.__grade == "B":
            return "Good"
        elif self.__grade == "C":
            return "Average"
        else:
            return "Needs Improvement"

    def updated_info(self):
        if self.__grade == "A":
            self.__grade = "A+"
        return self.__grade

class Student2(Student):
    def __init__(self, name, age, grade, id):
        super().__init__(name, age, grade, id)

    def get_name(self):
        return self.name # public attribute inherited from parent

    def get_age(self):
        return self._age # protected attribute inherited from parent

    # Access through parent's public method instead of private attribute
    # return __grade would cause AttributeError: 'Student2' object has no attribute '__grade'
    def get_grade(self):
        return super().get_grade() 
    
    def get_id(self):
        return super().get_id() 
    
    # Method demonstrating access to inherited private attributes
    def display_full_info(self):
        print(f"Student: {self.name}")
        print(f"Age: {self._age}")
        print(f"Grade: {self.get_grade()}") # Access through public method
        print(f"ID: {self.get_id()}") # Access through public method
        print(f"Status: {self.get_academic_status()}") # Inherited method

if __name__ == "__main__":
    print("DEMONSTRATING DIFFERENT TYPES OF ATTRIBUTES:\n")

    # ================================ PARENT CLASS ================================
    print("PARENT CLASS (Student):")
    student = Student("John", 20, "A", 123456)

    # PUBLIC ATTRIBUTES
    print(f"Public attribute: {student.name}") # ✅ Ok, public attribute

    # PROTECTED ATTRIBUTES
    print(f"Protected attribute: {student._age}") # ✅ Ok, protected attribute    

    # PRIVATE ATTRIBUTES
    print(f"Grade via method: {student.get_grade()}") # ✅ Ok, accessed through method
    print(f"ID via method: {student.get_id()}") # ✅ Ok, accessed through method
    print(f"Academic status: {student.get_academic_status()}") # ✅ New method using private attribute
    print(f"Updated grade: {student.updated_info()}") # ✅ New method using private attribute
    
    # This would cause AttributeError:
    # print(student.__grade) # ❌ Not ok, private attribute
    # print(student.__id) # ❌ Not ok, private attribute

    print("\n" + "="*60 + "\n")

    # ================================ CHILD CLASS ================================
    print("CHILD CLASS (Student2 inheriting from Student):")
    student2 = Student2("Jane", 21, "B", 789012)

    # PUBLIC ATTRIBUTES (inherited)
    print(f"Inherited public: {student2.name}") # ✅ Ok, inherited public attribute

    # PROTECTED ATTRIBUTES (inherited)
    print(f"Inherited protected: {student2._age}") # ✅ Ok, inherited protected attribute

    # PRIVATE ATTRIBUTES (inherited, accessed through methods)
    print(f"Grade via method: {student2.get_grade()}") # ✅ Ok, inherited method
    print(f"ID via method: {student2.get_id()}") # ✅ Ok, inherited method
    print(f"Updated grade: {student2.updated_info()}") # ✅ New method using private attribute

    # This would cause AttributeError:
    # print(student2.__grade) # ❌ Not ok, private attribute
    # print(student2.__id) # ❌ Not ok, private attribute
    
    print("DEMONSTRATING INHERITANCE:")
    student2.display_full_info()


  