import os
from PIL import Image, ImageTk
import tkinter as tk
from views.student_view import manage_students

class DashboardApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("School Marks Management System")
        self.root.geometry("800x500")  # Adjusted window size
        self.username = username

        image_path = os.path.abspath(os.path.join("assets", "school.jpg"))

        if os.path.exists(image_path):
            self.school_logo = Image.open(image_path)
            self.school_logo = self.school_logo.resize((200, 200), Image.Resampling.LANCZOS)
            self.school_logo = ImageTk.PhotoImage(self.school_logo)
        else:
            print("School logo not found!")
            self.school_logo = None

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.left_frame = tk.Frame(self.main_frame, bg="#D9D9D9", width=200)
        self.left_frame.pack(side="left", fill="y", expand=False)

        self.right_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.show_dashboard()

    def show_dashboard(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        if self.school_logo:
            logo_label = tk.Label(self.right_frame, image=self.school_logo, bg="#ffffff")
            logo_label.pack(pady=20, padx=20)
        else:
            tk.Label(self.right_frame, text="School Logo Missing", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=20, padx=20)

        welcome_label = tk.Label(self.right_frame, text=f"Welcome, {self.username}!", font=("Arial", 18, "bold"), bg="#ffffff")
        welcome_label.pack(pady=10, padx=20)
        self.add_buttons()

    def add_buttons(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        button_frame = tk.Frame(self.left_frame, bg="#D9D9D9")  # Match background color
        button_frame.pack(pady=50, padx=10, anchor="center")

        tk.Button(button_frame, text="Manage Students", command=self.show_student_view, width=15, height=2, fg="#ffffff", bg="#3D56C4", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Manage Subjects", command=self.show_subject_view, width=15, height=2, fg="#ffffff", bg="#3D56C4", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Enter Marks", command=self.show_marks_view, width=15, height=2, fg="#ffffff", bg="#3D56C4", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Logout", command=self.logout, width=15, height=2, fg="#F44336", bg="white", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)

    def show_student_view(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        manage_students(self.right_frame, self)

    def show_subject_view(self):
        print("Subject View")

    def show_marks_view(self):
        print("Marks View")

    def logout(self):
        print("Logout")
        self.root.destroy()

def open_dashboard(username):
    root = tk.Tk()
    app = DashboardApp(root, username)
    root.mainloop()