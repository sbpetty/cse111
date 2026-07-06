import os
import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as mb

NOTES_FOLDER = "notes"

root = tk.Tk()
root.title("Notebook")

window_width = 900
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

def ensure_notes_folder():
    os.makedirs(NOTES_FOLDER, exist_ok=True)

def open_file():
    filename = fd.askopenfilename()

def save_note():
    ensure_notes_folder()
    text = text_box.get("1.0", "end-1c")
    path = fd.asksaveasfilename(
        initialdir=os.path.abspath(NOTES_FOLDER),
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        initialfile="note.txt",
        title="Save note as..."
    )
    if not path:
        return

    try:
        with open(path, "w") as file:
            file.write(text)
            mb.showinfo("Saved", "File saved successfully!")
    except OSError as e:
        mb.showerror("Error", f"Could not save file:\n{e}")\

text_box = tk.Text()
text_box.pack(expand=True, fill=tk.BOTH)

save_button = ttk.Button(text="Save", command=save_note)
save_button.pack()

root.mainloop()