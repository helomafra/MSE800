# Yoobee Colleges Student System

## Project Overview

This is a command-line application for **Week 3 - Activity 4**, implementing a comprehensive student information system for Yoobee Colleges using SQLite3 database. The system tracks students, lecturers, courses, class offerings, and student enrollments with final grades.

## Technical Aspects

### Database Architecture
- **Database Engine**: SQLite3
- **Database File**: `yoobee_colleges.db`
- **Tables**: 5 main entities with proper relationships
- **Foreign Keys**: Implemented for referential integrity
- **Constraints**: UNIQUE constraints on email fields and course codes

### Database Schema

| Table | Fields | Description |
|-------|--------|-------------|
| **students** | `student_id` (PK), `name`, `email`, `status` | Student information |
| **lecturers** | `lecturer_id` (PK), `name`, `email`, `department` | Lecturer information |
| **courses** | `course_id` (PK), `code`, `title`, `credits` | Course catalog |
| **class_offerings** | `class_id` (PK), `course_id` (FK), `lecturer_id` (FK), `term`, `stream` | Class instances |
| **enrollments** | `enrollment_id` (PK), `student_id` (FK), `class_id` (FK), `enrolled_on`, `status`, `final_grade` | Student enrollments |

### Core Functionalities
- ✅ **Add Records**: Create new students, lecturers, courses, class offerings, and enrollments
- 👀 **View Records**: Display all records from each table with formatted output
- 🗑️ **Delete Records**: Remove records by ID with proper error handling
- ✏️ **Update Records**: Modify enrollment grades and other attributes

## File Structure

```
yoobee_colleges_students/
├── main.py          # Main application entry point and menu system
├── database.py      # Database connection and table creation functions
├── manager.py       # CRUD operations for all entities
├── README.md        # This documentation file
└── scope.md         # Project scope definition
```

## Usage Instructions

1. **Run the application**: `python main.py`
2. **Navigate through the menu system** using number inputs
3. **Manage Students**: Add, view, and delete student records
4. **Manage Lecturers**: Add, view, and delete lecturer records
5. **Manage Courses**: Add, view, and delete course records
6. **Manage Class Offerings**: Add, view, and delete class instances
7. **Manage Enrollments**: Add, view, update grades, and delete enrollments
8. **View All Data**: See complete database overview

## Dependencies

- Python 3.x (built-in `sqlite3` module)
- No external packages required


