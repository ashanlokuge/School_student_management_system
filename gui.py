import tkinter as tk
from tkinter import messagebox, simpledialog
from auth import login, add_teacher  # Import authentication functions
from dashboard import open_dashboard  # Import dashboard function

# Function to handle login
def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password):
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()  # Close login window
        open_dashboard(username)  # Open dashboard with logged-in user
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Function to register a new teacher
def register_user():
    new_username = simpledialog.askstring("Register", "Enter new username:")
    new_password = simpledialog.askstring("Register", "Enter new password:", show="*")

    if new_username and new_password:
        if add_teacher(new_username, new_password):
            messagebox.showinfo("Success", f"User '{new_username}' registered successfully!")
        else:
            messagebox.showerror("Error", "Username already exists!")
    else:
        messagebox.showerror("Error", "Username and Password cannot be empty.")

# Create login window
root = tk.Tk()
root.title("Teacher Login")
root.geometry("300x250")

tk.Label(root, text="Login", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")  # Masked input
password_entry.pack()

login_button = tk.Button(root, text="Login", command=authenticate, bg="blue", fg="white")
login_button.pack(pady=10)

register_button = tk.Button(root, text="Create Account", command=register_user, bg="green", fg="white")
register_button.pack(pady=5)

root.mainloop()
