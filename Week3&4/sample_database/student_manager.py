from database import create_connection

def insert_sample_students():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Insert two sample students
    sample_students = [
        ("John Smith", "123 Main Street, City"),
        ("Mary Johnson", "456 Oak Avenue, Town")
    ]
    
    for student in sample_students:
        cursor.execute("INSERT INTO students (stu_name, stu_address) VALUES (?, ?)", student)
    
    conn.commit()
    conn.close()
    print("Sample students added successfully!")

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (stu_name, stu_address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.close()
    print("Student added successfully!")