import sqlite3
import hashlib

# Connect to SQLite database (Creates 'school.db' if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create the users table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
''')

# Function to hash passwords securely
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add a teacher (used to add admin manually)
def add_teacher(username, password):
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(f"✅ User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠ User '{username}' already exists.")

# Add a default admin account (if not exists)
add_teacher("admin", "admin123")

# Close database connection
conn.close()
print("✅ Database setup complete!")
