import tkinter as tk
from tkinter import messagebox
import sqlite3
import blog as blg



# Function to create the database and table
def create_database():
    conn = sqlite3.connect('users.db')  # Create or connect to a database
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to sign up a new user
def signup():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            messagebox.showinfo("Signup Success", "Account created successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Signup Failed", "Username already exists.")
        finally:
            conn.close()
    else:
        messagebox.showerror("Input Error", "Please enter both username and password.")

# Function to log in an existing user
def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login Success", "Welcome!")
        # Call the main  page function here
        blg.create_blog_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the database and table
create_database()

# Create the main window
window = tk.Tk()
window.title("Member Login")
window.geometry("350x500")
window.configure(bg="#ffffff")

# Login frame
login_frame = tk.Frame(window, bg="#333333", bd=10, relief="raised")
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=260, height=330)

# Profile icon
profile_icon = tk.Label(login_frame, text="👤", bg="#9C0E0E", fg="white", font=("Open Sans", 30))
profile_icon.pack(pady=10)

# Title label
title_label = tk.Label(login_frame, text="MEMBER LOGIN", bg="#333333", fg="white", font=("Open Sans", 12, "bold"))
title_label.pack(pady=5)

# Username entry
username_entry = tk.Entry(login_frame, font=("Open Sans", 10))
username_entry.pack(pady=10, ipady=5, ipadx=5)
username_entry.insert(0, "USERNAME")

# Password entry
password_entry = tk.Entry(login_frame, show="*", font=("Open Sans", 10))
password_entry.pack(pady=10, ipady=5, ipadx=5)
password_entry.insert(0, "PASSWORD")

# Login button
login_button = tk.Button(login_frame, text="LOGIN", bg="#556ee6", fg="white", font=("Roboto", 10, "bold"), command=login)
login_button.pack(pady=15, ipadx=10, ipady=5)

# Signup button
signup_button = tk.Button(login_frame, text="SIGN UP", bg="#28a745", fg="white", font=("Roboto", 10, "bold"), command=signup)
signup_button.pack(pady=5, ipadx=10, ipady=5)

# Remember me checkbox
remember_var = tk.IntVar()
remember_check = tk.Checkbutton(login_frame, text="Remember me", variable=remember_var, bg="#333333", fg="white", selectcolor="#050505", activebackground="#333333")
remember_check.pack()

# Forgot password label
forgot_label = tk.Label(window, text="Forgot password?", bg="#f2f2f2", fg="#666666", font=("Arial", 9))
forgot_label.place(relx=0.5, rely=0.87, anchor="center")

# Create account label
create_label = tk.Label(window, text="Not a member? CREATE ACCOUNT", bg="#f2f2f2", fg="#3333cc", font=("Arial", 9, "underline"))
create_label.place(relx=0.5, rely=0.93, anchor="center")

# Start the GUI event loop
window.mainloop()
