import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("NewBreak Church")
window.geometry("800x700")
window.configure(bg="#333333")

# Add border to header
header = tk.Frame(window, bg='lightgrey', height=50, bd=2, relief='groove')
header.pack(fill='x')

# Cleaned-up menu items, added spacing with padding instead of spaces
menu_items = ["NewBreak Church", "Watch", "About", "Ministries", "Next Steps", "Give"]

for item in menu_items:
    label = tk.Label(header, text=item, bg='lightgrey', font=('open sans', 10, 'bold'), padx=10, pady=15)
    label.pack(side='left')

# Add a "Be Our Guest" button instead of label
guest_button = tk.Button(header, text="Be our guest", bg="#007ACC", fg="white", font=('open sans', 10, 'bold'), padx=10, pady=8, relief='raised', bd=2)
guest_button.pack(side='right', padx=10)

# Load and show image
img = Image.open("C:/Pyhton project/church.jpg") 
img = img.resize((600, 300))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(window, image=photo)
img_label.pack(pady=20)

# Footer title
footer_title = tk.Label(window, text="One Church. Many Locations.", fg='white', bg="#333333", font=('Arial', 12, 'bold'))
footer_title.pack(pady=(20, 10))

# Footer description with font fix and capitalized sentence
footer_desc = tk.Label(window, text="Join us this weekend at one of our locations where you will find inspiring\n"
                                  "worship, a practical message you can apply to your life right away, a kid’s\n"
                                  "environment your children will never want to leave, and a church company\n"
                                  "happy to join you on your faith journey.",
                                  fg='white', bg="#333333", font=('Arial', 10), justify='center')
footer_desc.pack()

window.mainloop()
