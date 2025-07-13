import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("NewBreak Church")
window.geometry("800x700")
window.configure(bg="#2c2f33")  # ✅ Changed background color

# Header frame
header = tk.Frame(window, bg='lightgrey', height=50, bd=1, relief='groove')  # added slight border
header.pack(fill='x')

# Menu labels
menu_items = [
    "NewBreak Church", "                   ",
    "    Watch About Ministries Next steps Give    ",
    "                      ", "Be our guest"
]

for item in menu_items[:-1]:  # All except last one
    label = tk.Label(header, text=item, bg='lightgrey',
                     font=('Arial', 10, 'bold'), padx=10, pady=20)
    label.pack(side='left')

# ✅ "Be our guest" as a styled button
style = ttk.Style()
style.configure("Rounded.TButton",
                foreground="white",
                background="#007ACC",
                font=("Arial", 10, "bold"),
                padding=6)
style.map("Rounded.TButton",
          background=[('active', '#005a99')])

guest_button = ttk.Button(header, text="Be our guest", style="Rounded.TButton")
guest_button.pack(side='right', padx=10, pady=5)

# Load and display image
img_path = "C:/Pyhton project/church.jpg"
img = Image.open(img_path)
img = img.resize((600, 300))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(window, image=photo)
img_label.image = photo
img_label.pack(pady=20)

# Footer title
footer_title = tk.Label(window, text="One Church. Many Locations.",
                        fg='white', bg="#2c2f33", font=('Arial', 12, 'bold'))
footer_title.pack(pady=(20, 10))

# Footer description
footer_desc = tk.Label(window, text="Join us this weekend at one of our locations where you will find inspiring\n"
                                    "worship, a practical message you can apply to your life right away, a kid’s\n"
                                    "environment your children will never want to leave, and a church company\n"
                                    "happy to join you on your faith journey.",
                       fg='white', bg="#2c2f33", font=('Arial', 10), justify='center')
footer_desc.pack()

window.mainloop()
