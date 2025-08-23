from database import create_connection
import sqlite3
from datetime import datetime

# ===== STUDENT MANAGEMENT =====
def add_student(name, email, status):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, email, status) VALUES (?, ?, ?)", (name, email, status))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Email must be unique.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

# ===== LECTURER MANAGEMENT =====
def add_lecturer(name, email, department):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturers (name, email, department) VALUES (?, ?, ?)", (name, email, department))
        conn.commit()
        print("Lecturer added successfully!")
    except sqlite3.IntegrityError:
        print("Email must be unique.")
    conn.close()

def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_lecturer(lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecturers WHERE lecturer_id = ?", (lecturer_id,))
    conn.commit()
    conn.close()
    print("Lecturer deleted successfully!")

# ===== COURSE MANAGEMENT =====
def add_course(code, title, credits):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (code, title, credits) VALUES (?, ?, ?)", (code, title, credits))
        conn.commit()
        print("Course added successfully!")
    except sqlite3.IntegrityError:
        print("Course code must be unique.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
    conn.commit()
    conn.close()
    print("Course deleted successfully!")

# ===== CLASS OFFERING MANAGEMENT =====
def add_class_offering(course_id, lecturer_id, term, stream):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO class_offerings (course_id, lecturer_id, term, stream) VALUES (?, ?, ?)", 
                      (course_id, lecturer_id, term, stream))
        conn.commit()
        print("Class offering added successfully!")
    except sqlite3.IntegrityError:
        print("This course, term, and stream combination already exists.")
    conn.close()

def view_class_offerings():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT co.class_id, c.code, c.title, l.name, co.term, co.stream
        FROM class_offerings co
        JOIN courses c ON co.course_id = c.course_id
        JOIN lecturers l ON co.lecturer_id = l.lecturer_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_class_offering(class_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM class_offerings WHERE class_id = ?", (class_id,))
    conn.commit()
    conn.close()
    print("Class offering deleted successfully!")

# ===== ENROLLMENT MANAGEMENT =====
def add_enrollment(student_id, class_id, status, final_grade=None):
    conn = create_connection()
    cursor = conn.cursor()
    enrolled_on = datetime.now().strftime("%Y-%m-%d")
    try:
        cursor.execute("INSERT INTO enrollments (student_id, class_id, enrolled_on, status, final_grade) VALUES (?, ?, ?, ?, ?)", 
                      (student_id, class_id, enrolled_on, status, final_grade))
        conn.commit()
        print("Enrollment added successfully!")
    except sqlite3.IntegrityError:
        print("This student is already enrolled in this class.")
    conn.close()

def view_enrollments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.enrollment_id, s.name, c.code, c.title, l.name, e.status, e.final_grade
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN class_offerings co ON e.class_id = co.class_id
        JOIN courses c ON co.course_id = c.course_id
        JOIN lecturers l ON co.lecturer_id = l.lecturer_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_grade(enrollment_id, final_grade):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE enrollments SET final_grade = ? WHERE enrollment_id = ?", (final_grade, enrollment_id))
    conn.commit()
    conn.close()
    print("Grade updated successfully!")

def delete_enrollment(enrollment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enrollments WHERE enrollment_id = ?", (enrollment_id,))
    conn.commit()
    conn.close()
    print("Enrollment deleted successfully!")
