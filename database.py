import sqlite3
import hashlib
import os

# Connect to SQLite database (Creates 'school.db' if it doesn't exist)
def create_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect("school.db")
    return conn

# Function to hash passwords securely
def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Function to initialize the database
def initialize_database():
    """Create tables if they don't exist."""
    conn = create_connection()
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Create the students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            city TEXT NOT NULL,
            grade TEXT NOT NULL,
            gender TEXT NOT NULL,
            religion TEXT NOT NULL,
            profile_picture TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a teacher (used to add admin manually)
def add_teacher(username, password):
    """Add a teacher/admin user to the database."""
    hashed_password = hash_password(password)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(f"✅ User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠ User '{username}' already exists.")
    finally:
        conn.close()

# Function to add a student
def add_student(student_id, name, birthday, city, grade, gender, religion, profile_picture):
    """Add a student to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO students (student_id, name, birthday, city, grade, gender, religion, profile_picture)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student_id, name, birthday, city, grade, gender, religion, profile_picture))
        conn.commit()
        print(f"✅ Student '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠ Student with ID '{student_id}' already exists.")
    finally:
        conn.close()

# Function to fetch all students
def get_all_students():
    """Retrieve all students from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

# Add a default admin account (if not exists)
if __name__ == "__main__":
    initialize_database()
    add_teacher("admin", "admin123")
    print("✅ Database setup complete!")