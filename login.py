import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create window
window = tk.Tk()
window.title("Member Login")
window.geometry("300x400")
window.configure(bg="#1e1e2f")  # ✅ Changed background color

# Login frame
login_frame = tk.Frame(window, bg="#2f2f3f", bd=10, relief="raised")
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=260, height=330)

# Profile icon
profile_icon = tk.Label(login_frame, text="👤", bg="#9C0E0E", fg="white", font=("Open Sans", 30))
profile_icon.pack(pady=10)

# Title
title_label = tk.Label(login_frame, text="MEMBER LOGIN", bg="#2f2f3f", fg="white", font=("Open Sans", 12, "bold"))
title_label.pack(pady=5)

# Username
username_entry = tk.Entry(login_frame, font=("Open Sans", 10))
username_entry.pack(pady=10, ipady=5, ipadx=5)
username_entry.insert(0, "USERNAME")

# Password
password_entry = tk.Entry(login_frame, show="*", font=("Open Sans", 10))
password_entry.pack(pady=10, ipady=5, ipadx=5)
password_entry.insert(0, "PASSWORD")

# ✅ Login button color changed
login_button = tk.Button(login_frame, text="LOGIN", bg="#4CAF50", fg="white", font=("Roboto", 10, "bold"), command=login, activebackground="#45a049")
login_button.pack(pady=15, ipadx=10, ipady=5)

# Remember checkbox
remember_var = tk.IntVar()
remember_check = tk.Checkbutton(login_frame, text="Remember me", variable=remember_var,
                                bg="#2f2f3f", fg="white", selectcolor="#050505", activebackground="#2f2f3f")
remember_check.pack()

# Forgot password label
forgot_label = tk.Label(window, text="Forgot password?", bg="#1e1e2f", fg="#bbbbbb", font=("Arial", 9))
forgot_label.place(relx=0.5, rely=0.87, anchor="center")

# Create account label
create_label = tk.Label(window, text="Not a member? CREATE ACCOUNT", bg="#1e1e2f", fg="#33ccff", font=("Arial", 9, "underline"))
create_label.place(relx=0.5, rely=0.93, anchor="center")

# Start GUI loop
window.mainloop()
