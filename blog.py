import tkinter as tk
from PIL import ImageTk, Image
import os




def create_blog_page():
    window = tk.Tk()
    window.title("Our Blog")
    window.geometry("900x700")
    window.configure(bg="#f5f5f5")

    # ---------- Header ----------
    header_frame = tk.Frame(window, bg="#535353", padx=20, pady=20)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="Read our Blog", font=("Helvetica", 24), fg="white", bg="#535353")
    title_label.pack(pady=10)

    # ---------- Subtitle ----------
    subtitle_frame = tk.Frame(window, bg="#f5f5f5", padx=20, pady=10)
    subtitle_frame.pack(fill="x")

    subtitle_label = tk.Label(
        subtitle_frame,
        text="Weekly Articles with Insight and the weekend's Message",
        font=("Helvetica", 18),
        fg="#333333",
        bg="#f5f5f5"
    )
    subtitle_label.pack(pady=5)

    # ---------- Description ----------
    desc_frame = tk.Frame(window, bg="#f5f5f5", padx=20, pady=20)
    desc_frame.pack(fill="x")

    desc_text = (
        "Our blog takes the message from the weekend and lays out next right steps\n"
        "so you can hear a message in practical ways"
    )
    desc_label = tk.Label(
        desc_frame,
        text=desc_text,
        font=("Helvetica", 16),
        fg="#555555",
        bg="#f5f5f5",
        justify="left"
    )
    desc_label.pack(pady=5)

    # ---------- Image Section ----------
    image_frame = tk.Frame(window, bg="#f5f5f5")
    image_frame.pack(pady=10)

    image_names = [
        "meeting.jpg",
        "content.jpg",
        "Blog.jpg",
        "virtual photography.jpg"
    ]

    images = []
    image_folder = "C:/Pyhton project"

    for idx, img_name in enumerate(image_names):
        full_path = os.path.join(image_folder, img_name)
        try:
            with Image.open(full_path) as img:
                img_resized = img.resize((150, 100))
                photo = ImageTk.PhotoImage(img_resized)
                images.append(photo)

                img_label = tk.Label(image_frame, image=photo, bg="#f5f5f5")
                img_label.image = photo  # Prevent garbage collection
                img_label.pack(side="left", padx=10)
        except Exception as e:
            print(f"Error loading image {img_name}: {e}")

    # ---------- Tags Section ----------
    tags_frame = tk.Frame(window, bg="#f5f5f5", padx=20, pady=20)
    tags_frame.pack(fill="x")

    tags = ["remote collaboration", "content development", "blog publishing", "visual storytelling"]

    for tag in tags:
        tag_label = tk.Label(
            tags_frame,
            text=tag,
            font=("Helvetica", 10),
            fg="white",
            bg="#838383",
            padx=8,
            pady=4,
            relief="raised"
        )
        tag_label.pack(side="left", padx=40)

    # ---------- Footer ----------
    footer_frame = tk.Frame(window, bg="#333333", padx=20, pady=10, height=50)
    footer_frame.pack(fill="x", side="bottom")

    window.mainloop()

if __name__ == "__main__":
    create_blog_page()
