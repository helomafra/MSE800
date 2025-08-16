from database import create_table, create_students_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import insert_sample_students, view_students, add_student

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Student")
    print("6. View All Students")
    print("7. View Both Tables")
    print("8. Exit")

def display_both_tables():
    print("\n==== USERS TABLE ====")
    users = view_users()
    if users:
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("No users found.")
    
    print("\n==== STUDENTS TABLE ====")
    students = view_students()
    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}")
    else:
        print("No students found.")

def main():
    create_table()
    create_students_table()
    insert_sample_students()

    while True:
        menu()
        choice = input("Select an option (1-8): ")
        
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter student name: ")
            address = input("Enter student address: ")
            add_student(name, address)
        elif choice == '6':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '7':
            display_both_tables()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
