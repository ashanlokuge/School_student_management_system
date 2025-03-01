import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from models.student_model import add_student  # Import the function to add students to the database

def open_add_student_window(parent_frame, dashboard):
    # Create a new top-level window for adding a student
    add_student_window = tk.Toplevel(parent_frame)
    add_student_window.title("Add Student")
    add_student_window.geometry("500x600")

    # Frame for the form
    form_frame = tk.Frame(add_student_window)
    form_frame.pack(pady=20)

    # Student ID
    tk.Label(form_frame, text="Student ID:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    student_id_entry = tk.Entry(form_frame, font=("Arial", 12))
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    # Student Name
    tk.Label(form_frame, text="Student Name:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    student_name_entry = tk.Entry(form_frame, font=("Arial", 12))
    student_name_entry.grid(row=1, column=1, padx=10, pady=5)

    # Birthday
    tk.Label(form_frame, text="Birthday:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    birthday_entry = tk.Entry(form_frame, font=("Arial", 12))
    birthday_entry.grid(row=2, column=1, padx=10, pady=5)

    # Address (City)
    tk.Label(form_frame, text="City:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    city_entry = tk.Entry(form_frame, font=("Arial", 12))
    city_entry.grid(row=3, column=1, padx=10, pady=5)

    # Grade (Dropdown)
    tk.Label(form_frame, text="Grade:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    grade_var = tk.StringVar()
    grade_dropdown = ttk.Combobox(form_frame, textvariable=grade_var, font=("Arial", 12), state="readonly")
    grade_dropdown['values'] = ("Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10")
    grade_dropdown.grid(row=4, column=1, padx=10, pady=5)
    grade_dropdown.current(0)

    # Gender (Radio Buttons)
    tk.Label(form_frame, text="Gender:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="e")
    gender_var = tk.StringVar(value="Male")
    tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 12)).grid(row=5, column=1, padx=10, pady=5, sticky="w")
    tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 12)).grid(row=5, column=1, padx=10, pady=5, sticky="e")

    # Religion (Dropdown)
    tk.Label(form_frame, text="Religion:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=5, sticky="e")
    religion_var = tk.StringVar()
    religion_dropdown = ttk.Combobox(form_frame, textvariable=religion_var, font=("Arial", 12), state="readonly")
    religion_dropdown['values'] = ("Christianity", "Islam", "Hinduism", "Buddhism", "Other")
    religion_dropdown.grid(row=6, column=1, padx=10, pady=5)
    religion_dropdown.current(0)

    # Profile Picture
    tk.Label(form_frame, text="Profile Picture:", font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=5, sticky="e")
    profile_picture_path = tk.StringVar()
    profile_picture_label = tk.Label(form_frame, text="No image selected", font=("Arial", 12))
    profile_picture_label.grid(row=7, column=1, padx=10, pady=5)

    def upload_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            profile_picture_path.set(file_path)
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            profile_picture_label.config(image=photo)
            profile_picture_label.image = photo  # Keep a reference to avoid garbage collection

    tk.Button(form_frame, text="Upload Image", command=upload_image, font=("Arial", 12)).grid(row=8, column=1, padx=10, pady=5)

    # Save Button
    def save_student():
        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        birthday = birthday_entry.get()
        city = city_entry.get()
        grade = grade_var.get()
        gender = gender_var.get()
        religion = religion_var.get()
        profile_picture = profile_picture_path.get()

        if not student_id or not student_name or not birthday or not city:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Save to database
        add_student(student_id, student_name, birthday, city, grade, gender, religion, profile_picture)
        messagebox.showinfo("Success", "Student added successfully!")
        add_student_window.destroy()  # Close the window after saving

    tk.Button(form_frame, text="Save", command=save_student, font=("Arial", 12), bg="green", fg="white").grid(row=9, column=1, padx=10, pady=20)

    # Back Button
    tk.Button(form_frame, text="Back", command=add_student_window.destroy, font=("Arial", 12), bg="grey", fg="white").grid(row=9, column=0, padx=10, pady=20)