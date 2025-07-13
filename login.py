# Inter-group contribution by Ahmad Khawar: Reviewed this file for readability
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

window = tk.Tk()

window.title("Member Login")
window.geometry("300x400")
window.configure(bg="#ffffff")

login_frame = tk.Frame(window, bg="#333333", bd=10, relief="raised")
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=260, height=330)

profile_icon = tk.Label(login_frame, text="👤", bg="#9C0E0E", fg="white", font=("Open Sans", 30))
profile_icon.pack(pady=10)

title_label = tk.Label(login_frame, text="MEMBER LOGIN", bg="#333333", fg="white", font=("Open Sans", 12, "bold"))
title_label.pack(pady=5)

username_entry = tk.Entry(login_frame, font=("Open Sans", 10))
username_entry.pack(pady=10, ipady=5, ipadx=5)
username_entry.insert(0, "USERNAME")

password_entry = tk.Entry(login_frame, show="*", font=("Open Sans", 10))
password_entry.pack(pady=10, ipady=5, ipadx=5)
password_entry.insert(0, "PASSWORD")

login_button = tk.Button(login_frame, text="LOGIN", bg="#556ee6", fg="white", font=("Roboto", 10, "bold"), command=login)
login_button.pack(pady=15, ipadx=10, ipady=5)

remember_var = tk.IntVar()
remember_check = tk.Checkbutton(login_frame, text="Remember me", variable=remember_var, bg="#333333", fg="white", selectcolor="#050505", activebackground="#333333")
remember_check.pack()

forgot_label = tk.Label(window, text="Forgot password?", bg="#f2f2f2", fg="#666666", font=("Arial", 9))
forgot_label.place(relx=0.5, rely=0.87, anchor="center")

create_label = tk.Label(window, text="Not a member? CREATE ACCOUNT", bg="#f2f2f2", fg="#3333cc", font=("Arial", 9, "underline"))
create_label.place(relx=0.5, rely=0.93, anchor="center")

window.mainloop()
