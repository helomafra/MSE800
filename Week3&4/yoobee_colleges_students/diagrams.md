# Use Case Diagram and Activity Diagram 

![Yoobee Students Use Case Diagram](/assets/UML_use_case.png)

## Actors: 
  - **Student** - People studying at YB College who can view their enrollments and grades
  - **Lecturer** - Staff who teach classes and can manage class offerings and grades
  - **Admin** - System administrators who manage all aspects of the college system

## Use Cases 

**Student Use Cases:**
- **View Personal Information:** Student requests personal details, and the system retrieves and displays student profile information including contact details and academic status.
- **View Enrollments:** Student requests enrollment records, and the system retrieves and displays all current and past course enrollments with status and dates.
- **View Grades:** Student requests academic performance data, and the system retrieves and displays grades for all enrolled courses and overall GPA.
- **View Available Courses:** Student requests course catalog, and the system retrieves and displays all available courses with prerequisites and scheduling information.

**Lecturer Use Cases:**
- **View Assigned Classes:** Lecturer requests teaching schedule, and the system retrieves and displays all assigned classes with times, locations, and student counts.
- **View Student Enrollments:** Lecturer requests class roster, and the system retrieves and displays list of enrolled students for specific classes.
- **Update Student Grades:** Lecturer enters student grades and assessment scores, and the system updates the student's academic record and calculates new GPA.
- **View Course Information:** Lecturer requests course details, and the system retrieves and displays course content, objectives, and assessment criteria.

**Admin Use Cases:**
- **Manage Students (Add, View, Delete, Update):** Admin enters student information or requests student records, and the system creates, retrieves, modifies, or removes student accounts and records.
- **Manage Lecturers (Add, View, Delete, Update):** Admin enters lecturer information or requests lecturer records, and the system creates, retrieves, modifies, or removes lecturer accounts and assignments.
- **Manage Courses (Add, View, Delete, Update):** Admin enters course information or requests course records, and the system creates, retrieves, modifies, or removes course offerings and curriculum data.
- **Manage Class Offerings (Add, View, Delete, Update):** Admin enters class schedule information or requests class records, and the system creates, retrieves, modifies, or removes class offerings and scheduling data.
- **Manage Enrollments (Add, View, Delete, Update):** Admin enters enrollment information or requests enrollment records, and the system creates, retrieves, modifies, or removes student course enrollments and status.
- **View All System Data:** Admin requests comprehensive system overview, and the system retrieves and displays aggregated data from all system modules and databases.

**Shared Use Cases:**
- **View Course Catalog:** User requests available courses, and the system retrieves and displays comprehensive course listing with descriptions, prerequisites, and availability.
- **View Class Schedules:** User requests scheduling information, and the system retrieves and displays class timetables, room assignments, and instructor details.
- **Search Records:** User enters search criteria, and the system searches across relevant databases and returns matching records based on specified parameters.

## Activity Diagram 

![Activity Diagram](/assets/activity_diagram.png)

