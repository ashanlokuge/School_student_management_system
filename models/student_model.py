from database import create_connection

def add_student(student_id, name, birthday, city, grade, gender, religion, profile_picture):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (student_id, name, birthday, city, grade, gender, religion, profile_picture)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (student_id, name, birthday, city, grade, gender, religion, profile_picture))
    conn.commit()
    conn.close()