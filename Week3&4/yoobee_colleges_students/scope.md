# YoobeeStudents Database Scope

Creating a small student information system for YB. We need to track: 
- Who studies what
- Who teaches which class 
- Students' final outcome in that class

The DB will store students, lecturers, the courses offered, and student enrollments with a final grade for that class. 

### Main entities 

**1. student**
- **Role**: People studying at YB College
- **Key attrs**: `student_id` (PK), `name` (VARCHAR), `email` (VARCHAR), `status` (VARCHAR)

**2. lecturer**
- **Role**: Staff who teach classes
- **Key attrs**: `lecturer_id` (PK), `name` (VARCHAR), `email` (VARCHAR), `department` (VARCHAR)

**3. course**
- **Role**: Catalog entry that defines what can be taught
- **Key attrs**: `course_id` (PK), `code` (e.g., "CS101") (VARCHAR), `title` (VARCHAR), `credits` (INTEGER)

**4. class_offering**
- **Role**: Instance of a Course in a term
- **Key attrs**: `class_id` (PK), `course_id` (FK → Course), `lecturer_id` (FK → Lecturer), `term` (e.g., "2025-T2"), `stream` (A or B) TEXT
- **Business rules**: (course_id, term, stream) should be UNIQUE

**5. enrollment**
- **Role**: Join that captures which Student takes which ClassOffering and their final outcome
- **Key attrs**: `enrollment_id` (PK), `student_id` (FK → Student), `class_id` (FK → ClassOffering), `enrolled_on` (TEXT), `status` (TEXT), `final_grade` (INT)

## Database Schema Diagram

![Yoobee Students Database Schema](/assets/yoobee_students_diagram.png)


## Use Case Diagram 

![Yoobee Students Use Case Diagram](/assets/UML_use_case.png)

### Actors: 
  - **Student** - People studying at YB College who can view their enrollments and grades
  - **Lecturer** - Staff who teach classes and can manage class offerings and grades
  - **Admin** - System administrators who manage all aspects of the college system

### Use Cases 

**Student Use Cases:**
- View Personal Information
- View Enrollments
- View Grades
- View Available Courses

**Lecturer Use Cases:**
- View Assigned Classes
- View Student Enrollments
- Update Student Grades
- View Course Information

**Admin Use Cases:**
- Manage Students (Add, View, Delete, Update)
- Manage Lecturers (Add, View, Delete, Update)
- Manage Courses (Add, View, Delete, Update)
- Manage Class Offerings (Add, View, Delete, Update)
- Manage Enrollments (Add, View, Delete, Update)
- View All System Data

**Shared Use Cases:**
- View Course Catalog
- View Class Schedules
- Search Records
