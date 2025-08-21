# Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
# Use the sample code to develop a command-line application for Week 3 – Activity 4, 
# incorporating a database sqlite3 and have at least three functionality such as 
# add records, delete records and view records for different tables.

from database import create_tables, insert_sample_data, should_insert_sample_data
from manager import *

def display_menu():
    print("\n" + "="*60)
    print("           YOOBEE COLLEGES STUDENT SYSTEM")
    print("="*60)
    print("1. Manage Students")
    print("2. Manage Lecturers") 
    print("3. Manage Courses")
    print("4. Manage Class Offerings")
    print("5. Manage Enrollments")
    print("6. View All Data")
    print("7. Exit")
    print("="*60)

def student_menu():
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            status = input("Enter status (Active/Inactive/Graduated): ")
            add_student(name, email, status)
        elif choice == '2':
            students = view_students()
            if students:
                print("\nSTUDENTS:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Status: {student[3]}")
            else:
                print("No students found.")
        elif choice == '3':
            student_id = input("Enter student ID to delete: ")
            try:
                delete_student(int(student_id))
            except ValueError:
                print("Invalid ID format.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

def lecturer_menu():
    while True:
        print("\n--- LECTURER MANAGEMENT ---")
        print("1. Add Lecturer")
        print("2. View All Lecturers")
        print("3. Delete Lecturer")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            name = input("Enter lecturer name: ")
            email = input("Enter lecturer email: ")
            department = input("Enter department: ")
            add_lecturer(name, email, department)
        elif choice == '2':
            lecturers = view_lecturers()
            if lecturers:
                print("\nLECTURERS:")
                for lecturer in lecturers:
                    print(f"ID: {lecturer[0]}, Name: {lecturer[1]}, Email: {lecturer[2]}, Department: {lecturer[3]}")
            else:
                print("No lecturers found.")
        elif choice == '3':
            lecturer_id = input("Enter lecturer ID to delete: ")
            try:
                delete_lecturer(int(lecturer_id))
            except ValueError:
                print("Invalid ID format.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

def course_menu():
    while True:
        print("\n--- COURSE MANAGEMENT ---")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Delete Course")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            code = input("Enter course code (e.g., CS101): ")
            title = input("Enter course title: ")
            credits = input("Enter credits: ")
            try:
                add_course(code, title, int(credits))
            except ValueError:
                print("Credits must be a number.")
        elif choice == '2':
            courses = view_courses()
            if courses:
                print("\nCOURSES:")
                for course in courses:
                    print(f"ID: {course[0]}, Code: {course[1]}, Title: {course[2]}, Credits: {course[3]}")
            else:
                print("No courses found.")
        elif choice == '3':
            course_id = input("Enter course ID to delete: ")
            try:
                delete_course(int(course_id))
            except ValueError:
                print("Invalid ID format.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

def class_offering_menu():
    while True:
        print("\n--- CLASS OFFERING MANAGEMENT ---")
        print("1. Add Class Offering")
        print("2. View All Class Offerings")
        print("3. Delete Class Offering")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            course_id = input("Enter course ID: ")
            lecturer_id = input("Enter lecturer ID: ")
            term = input("Enter term (e.g., 2025-T2): ")
            stream = input("Enter stream (A or B): ")
            try:
                add_class_offering(int(course_id), int(lecturer_id), term, stream)
            except ValueError:
                print("Course ID and Lecturer ID must be numbers.")
        elif choice == '2':
            classes = view_class_offerings()
            if classes:
                print("\nCLASS OFFERINGS:")
                for cls in classes:
                    print(f"ID: {cls[0]}, Course: {cls[1]} - {cls[2]}, Lecturer: {cls[3]}, Term: {cls[4]}, Stream: {cls[5]}")
            else:
                print("No class offerings found.")
        elif choice == '3':
            class_id = input("Enter class ID to delete: ")
            try:
                delete_class_offering(int(class_id))
            except ValueError:
                print("Invalid ID format.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

def enrollment_menu():
    while True:
        print("\n--- ENROLLMENT MANAGEMENT ---")
        print("1. Add Enrollment")
        print("2. View All Enrollments")
        print("3. Update Grade")
        print("4. Delete Enrollment")
        print("5. Back to Main Menu")
        
        choice = input("Select option (1-5): ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            class_id = input("Enter class ID: ")
            status = input("Enter status (Enrolled/Completed/Dropped): ")
            final_grade = input("Enter final grade (optional, press Enter to skip): ")
            
            try:
                grade = int(final_grade) if final_grade else None
                add_enrollment(int(student_id), int(class_id), status, grade)
            except ValueError:
                print("Student ID and Class ID must be numbers.")
        elif choice == '2':
            enrollments = view_enrollments()
            if enrollments:
                print("\nENROLLMENTS:")
                for enrollment in enrollments:
                    grade_str = str(enrollment[6]) if enrollment[6] else "N/A"
                    print(f"ID: {enrollment[0]}, Student: {enrollment[1]}, Course: {enrollment[2]} - {enrollment[3]}, Lecturer: {enrollment[4]}, Status: {enrollment[5]}, Grade: {grade_str}")
            else:
                print("No enrollments found.")
        elif choice == '3':
            enrollment_id = input("Enter enrollment ID: ")
            final_grade = input("Enter new grade: ")
            try:
                update_grade(int(enrollment_id), int(final_grade))
            except ValueError:
                print("IDs and grade must be numbers.")
        elif choice == '4':
            enrollment_id = input("Enter enrollment ID to delete: ")
            try:
                delete_enrollment(int(enrollment_id))
            except ValueError:
                print("Invalid ID format.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def view_all_data():
    print("\n" + "="*80)
    print("                           ALL DATA OVERVIEW")
    print("="*80)
    
    # Students
    print("\nSTUDENTS:")
    students = view_students()
    if students:
        for student in students:
            print(f"  ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Status: {student[3]}")
    else:
        print("  No students found.")
    
    # Lecturers
    print("\nLECTURERS:")
    lecturers = view_lecturers()
    if lecturers:
        for lecturer in lecturers:
            print(f"  ID: {lecturer[0]}, Name: {lecturer[1]}, Email: {lecturer[2]}, Department: {lecturer[3]}")
    else:
        print("  No lecturers found.")
    
    # Courses
    print("\nCOURSES:")
    courses = view_courses()
    if courses:
        for course in courses:
            print(f"  ID: {course[0]}, Code: {course[1]}, Title: {course[2]}, Credits: {course[3]}")
    else:
        print("  No courses found.")
    
    # Class Offerings
    print("\nCLASS OFFERINGS:")
    classes = view_class_offerings()
    if classes:
        for cls in classes:
            print(f"  ID: {cls[0]}, Course: {cls[1]} - {cls[2]}, Lecturer: {cls[3]}, Term: {cls[4]}, Stream: {cls[5]}")
    else:
        print("  No class offerings found.")
    
    # Enrollments
    print("\nENROLLMENTS:")
    enrollments = view_enrollments()
    if enrollments:
        for enrollment in enrollments:
            grade_str = str(enrollment[6]) if enrollment[6] else "N/A"
            print(f"  ID: {enrollment[0]}, Student: {enrollment[1]}, Course: {enrollment[2]} - {enrollment[3]}, Lecturer: {enrollment[4]}, Status: {enrollment[5]}, Grade: {grade_str}")
    else:
        print("  No enrollments found.")

def main():
    print("Welcome to Yoobee Colleges Student System!")
    print("Initializing database...")
    
    # Create tables
    create_tables()
    
    # Only insert sample data if database is empty
    if should_insert_sample_data():
        insert_sample_data()
        print("Sample data inserted!")
    else:
        print("Database already has data, skipping sample insertion.")
    
    while True:
        display_menu()
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            student_menu()
        elif choice == '2':
            lecturer_menu()
        elif choice == '3':
            course_menu()
        elif choice == '4':
            class_offering_menu()
        elif choice == '5':
            enrollment_menu()
        elif choice == '6':
            view_all_data()
        elif choice == '7':
            print("Thank you for using Yoobee Colleges Student System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

