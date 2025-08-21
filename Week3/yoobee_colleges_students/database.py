import sqlite3

def create_connection():
    conn = sqlite3.connect("yoobee_colleges.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            status TEXT NOT NULL
        )
    ''')
    
    # Create lecturers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL
        )
    ''')
    
    # Create courses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    ''')
    
    # Create class_offerings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class_offerings (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            lecturer_id INTEGER NOT NULL,
            term TEXT NOT NULL,
            stream TEXT NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses (course_id),
            FOREIGN KEY (lecturer_id) REFERENCES lecturers (lecturer_id),
            UNIQUE(course_id, term, stream)
        )
    ''')
    
    # Create enrollments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            enrolled_on TEXT NOT NULL,
            status TEXT NOT NULL,
            final_grade INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (class_id) REFERENCES class_offerings (class_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("All tables created successfully!")

def should_insert_sample_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    student_count = cursor.fetchone()[0]
    conn.close()
    return student_count == 0

def insert_sample_data():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Insert sample students
    sample_students = [
        ("Alice Johnson", "alice.j@yoobee.ac.nz", "Active"),
        ("Bob Smith", "bob.smith@yoobee.ac.nz", "Active"),
        ("Carol Davis", "carol.davis@yoobee.ac.nz", "Graduated")
    ]
    
    for student in sample_students:
        try:
            cursor.execute("INSERT INTO students (name, email, status) VALUES (?, ?, ?)", student)
        except sqlite3.IntegrityError:
            pass  # Skip if email already exists
    
    # Insert sample lecturers
    sample_lecturers = [
        ("Dr. Sarah Wilson", "sarah.wilson@yoobee.ac.nz", "Computer Science"),
        ("Prof. Mike Brown", "mike.brown@yoobee.ac.nz", "Design"),
        ("Dr. Lisa Chen", "lisa.chen@yoobee.ac.nz", "Business")
    ]
    
    for lecturer in sample_lecturers:
        try:
            cursor.execute("INSERT INTO lecturers (name, email, department) VALUES (?, ?, ?)", lecturer)
        except sqlite3.IntegrityError:
            pass  # Skip if email already exists
    
    # Insert sample courses
    sample_courses = [
        ("CS101", "Introduction to Programming", 15),
        ("DS201", "Digital Design Fundamentals", 15),
        ("BU301", "Business Management", 15)
    ]
    
    for course in sample_courses:
        try:
            cursor.execute("INSERT INTO courses (code, title, credits) VALUES (?, ?, ?)", course)
        except sqlite3.IntegrityError:
            pass  # Skip if course code already exists
    
    # Insert sample class offerings
    sample_classes = [
        (1, 1, "2025-T2", "A"),
        (2, 2, "2025-T2", "A"),
        (3, 3, "2025-T2", "B")
    ]
    
    for class_offering in sample_classes:
        try:
            cursor.execute("INSERT INTO class_offerings (course_id, lecturer_id, term, stream) VALUES (?, ?, ?, ?)", class_offering)
        except sqlite3.IntegrityError:
            pass  # Skip if combination already exists
    
    # Insert sample enrollments
    sample_enrollments = [
        (1, 1, "2025-01-15", "Enrolled", 85),
        (2, 1, "2025-01-15", "Enrolled", 92),
        (3, 2, "2025-01-15", "Enrolled", 78)
    ]
    
    for enrollment in sample_enrollments:
        try:
            cursor.execute("INSERT INTO enrollments (student_id, class_id, enrolled_on, status, final_grade) VALUES (?, ?, ?, ?, ?)", enrollment)
        except sqlite3.IntegrityError:
            pass  # Skip if enrollment already exists
    
    conn.commit()
    conn.close()
    print("Sample data inserted successfully!")
