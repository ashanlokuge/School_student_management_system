import sqlite3
import hashlib

# Function to hash passwords securely
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check login credentials
def login(username, password):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    
    user = cursor.fetchone()
    conn.close()
    
    return user is not None  # Return True if user exists, False otherwise

# Function to add a new teacher
def add_teacher(username, password):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    hashed_password = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True  # Success
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username already exists
