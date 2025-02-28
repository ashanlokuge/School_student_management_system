import tkinter as tk
from views import manage_students

class DashboardApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("School Marks Management System")
        self.root.geometry("500x400")
        self.username = username

        self.frame_dashboard = tk.Frame(root)
        self.frame_dashboard.pack(fill="both", expand=True)
        self.frame_student_view = tk.Frame(root)
        self.show_dashboard()

    def show_dashboard(self):
        for widget in self.frame_dashboard.winfo_children():
            widget.destroy()

        tk.Label(self.frame_dashboard, text=f"Welcome, {self.username}!", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Button(self.frame_dashboard, text="Manage Students", command=self.show_student_view, width=20, height=2, bg="blue", fg="white").pack(pady=10)
        tk.Button(self.frame_dashboard, text="Manage Subjects", command=self.show_subject_view, width=20, height=2, bg="blue", fg="white").pack(pady=10)
        tk.Button(self.frame_dashboard, text="Enter Marks", command=self.show_marks_view, width=20, height=2, bg="blue", fg="white").pack(pady=10)
        tk.Button(self.frame_dashboard, text="Logout", command=self.logout, width=20, height=2, bg="red", fg="white").pack(pady=20)

    def show_student_view(self):
        self.frame_dashboard.pack_forget()
        manage_students(self.frame_student_view, self)
        self.frame_student_view.pack(fill="both", expand=True)

    def show_subject_view(self):
        """Switch to the subject management view."""
        pass

    def show_marks_view(self):
        """Switch to the marks entry view."""
        # Similar to show_student_view, add logic to show marks entry
        pass

    def logout(self):
        """Log out by destroying the root window."""
        self.root.destroy()

def open_dashboard(username):
    root = tk.Tk()
    app = DashboardApp(root, username)
    root.mainloop()