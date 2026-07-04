import tkinter as tk
from tkinter import ttk, filedialog as fd

root = tk.Tk()
root.title("Notebook")

window_width = 900
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

def make_note():
    text_box = tk.Text()
    text_box.pack(expand=True, fill=tk.BOTH)

def open_file():
    filename = fd.askopenfilename()

def save_file():
    pass

root.mainloop()