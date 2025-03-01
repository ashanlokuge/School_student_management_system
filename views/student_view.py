import tkinter as tk
from tkinter import messagebox
from views.Add_student import open_add_student_window  # Import the new Add Student window function

def manage_students(parent_frame, dashboard):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    tk.Label(parent_frame, text="Manage Students", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(parent_frame, text="Add Student", command=lambda: open_add_student_window(parent_frame, dashboard), width=20, height=2).pack(pady=10)
    tk.Button(parent_frame, text="View Students", command=lambda: messagebox.showinfo("View Students", "List of students"), width=20, height=2).pack(pady=10)

    tk.Button(parent_frame, text="Back to Dashboard", command=lambda: back_to_dashboard(parent_frame, dashboard), width=20, height=2, bg="grey", fg="white").pack(pady=10)

def back_to_dashboard(current_frame, dashboard):
    current_frame.pack_forget()
    if dashboard:
        dashboard.frame_dashboard.pack(fill="both", expand=True)
        dashboard.show_dashboard()