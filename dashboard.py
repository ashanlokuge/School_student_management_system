import tkinter as tk
from tkinter import messagebox

# Function to open student management (Placeholder)
def open_students():
    messagebox.showinfo("Students", "Student Management Coming Soon!")

# Function to open subject management (Placeholder)
def open_subjects():
    messagebox.showinfo("Subjects", "Subject Management Coming Soon!")

# Function to open marks entry (Placeholder)
def open_marks():
    messagebox.showinfo("Marks", "Marks Entry Coming Soon!")

# Logout function
def logout(root):
    root.destroy()  # Close the dashboard
    import gui  # Restart login window

# Main dashboard function
def open_dashboard(username):
    root = tk.Tk()
    root.title("School Marks Management System")
    root.geometry("500x400")

    tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 16, "bold")).pack(pady=20)

    # Navigation buttons
    tk.Button(root, text="Manage Students", command=open_students, width=20, height=2, bg="blue", fg="white").pack(pady=10)
    tk.Button(root, text="Manage Subjects", command=open_subjects, width=20, height=2, bg="blue", fg="white").pack(pady=10)
    tk.Button(root, text="Enter Marks", command=open_marks, width=20, height=2, bg="blue", fg="white").pack(pady=10)

    # Logout button
    tk.Button(root, text="Logout", command=lambda: logout(root), width=20, height=2, bg="red", fg="white").pack(pady=20)

    root.mainloop()
