import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("NewBreak Church")
window.geometry("800x700")
window.configure(bg="#333333")

header = tk.Frame(window, bg='lightgrey', height=50)
header.pack(fill='x')

menu_items = ["NewBreak Church","                   ", "    Watch About Ministries Next steps Give    ","                      ", "Be our guest"]
for item in menu_items:
    label = tk.Label(header, text=item, bg='lightgrey', font=('open sans', 10, 'bold'), padx=10, pady=20)
    label.pack(side='left')

img = Image.open("C:/Pyhton project/church.jpg") 
img = img.resize((600, 300))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(window, image=photo)
img_label.pack(pady=20)


footer_title = tk.Label(window, text="One Church. Many Locations.", fg='white', bg="#333333", font=('Arial', 12, 'bold'))
footer_title.pack(pady=(20, 10))

footer_desc = tk.Label(window, text="join us this weekend at one of our locations where you will find inspiring\n"
                                  "worship a practical message you can apply to your life right away a kid’s\n"
                                  "environment your children will never want to leave and a church company\n"
                                  "happy to join you on your faith journey.",
                                   
 fg='white', bg="#333333", font=('Sans serif', 10), justify='center')
footer_desc.pack()

window.mainloop()
