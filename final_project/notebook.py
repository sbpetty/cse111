import os
import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as mb

PROGRAM_FOLDER = os.path.dirname(os.path.abspath(__file__))
NOTES_FOLDER = os.path.join(PROGRAM_FOLDER, "notes")
PADDING_SIZE = 10


def create_window(root, width, height):
    """Creates, sizes, and centers a tkinter window.

    root: the window object.
    width: the desired screen width.
    height: the desired screen height."""

    # Get aspect ratio of user's screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Get center coordinates of the window
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    # Initial window size and on-screen location
    root.geometry(f"{width}x{height}+{center_x}+{center_y}")


def create_filename(note_title):
    """Returns a stripped .txt filename given
    a note title. If title is empty, returns
    'Untitled.txt'."""
    note_title = note_title.strip()
    if not note_title:
        return "Untitled.txt"
    else:
        return note_title + ".txt"


def get_notes_list():
    files_list = os.listdir(NOTES_FOLDER)
    notes_list = []
    for filename in files_list:
        notes_list.append(filename[0:-4])
    return notes_list


class NotesApp:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Notebook")

        # Center and size window
        create_window(self.root, 1500, 1000)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.create_home_frame()

        self.create_editor_frame()

        self.show_home_frame()

        self.root.mainloop()


    def create_home_frame(self):
        self.home_frame = ttk.Frame(self.root)

        self.note_selection = tk.Listbox(self.home_frame)
        notes_list = get_notes_list()
        print(notes_list)
        for i in range(len(notes_list)):
            self.note_selection.insert(i, notes_list[i])
        self.note_selection.grid(row=0, column=0, padx=PADDING_SIZE, pady=PADDING_SIZE, sticky="nsew")

        self.new_note_button = ttk.Button(
            self.home_frame,
            text="New Note",
            command=self.new_note
        )
        self.new_note_button.grid(row=1, column=0, pady=PADDING_SIZE)

        self.exit_button = ttk.Button(
            self.home_frame,
            text="Exit",
            command=self.exit_program
        )
        self.exit_button.grid(row=2, column=0, pady=PADDING_SIZE)

        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


    def create_editor_frame(self):
        """Creates the environment for editing a note."""

        self.editor_frame = ttk.Frame(self.root)

        # Box for user to enter note title
        self.title_entry = tk.Entry(self.editor_frame)
        self.title_entry.grid(
            row=0,
            column=0,
            padx=PADDING_SIZE,
            pady=PADDING_SIZE,
            sticky="ew"
        )

        # Box for note body
        self.text_box = tk.Text(self.editor_frame)
        self.text_box.grid(
            row=1,
            column=0,
            padx=PADDING_SIZE,
            sticky="nsew"
        )

        self.save_button = ttk.Button(
            self.editor_frame,
            text="Save", 
            command=self.save_note
        )
        self.save_button.grid(
            row=2,
            column=0,
            padx=PADDING_SIZE,
            pady=PADDING_SIZE,
            sticky="w"
        )

        self.editor_frame.grid_rowconfigure(1, weight=1)
        self.editor_frame.grid_columnconfigure(0, weight=1)

        self.editor_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


    def show_home_frame(self):
        self.home_frame.tkraise()


    def show_editor_frame(self, note_title=None):
        self.editor_frame.tkraise()


    def new_note(self):
        self.title_entry.delete(0, tk.END)
        self.text_box.delete("1.0", "end-1c")
        self.show_editor_frame()


    def save_note(self):
        # Ensure notes folder exists
        os.makedirs(NOTES_FOLDER, exist_ok=True)
        
        # Get title and note text
        title = self.title_entry.get()
        filename = create_filename(title)
        text = self.text_box.get("1.0", "end-1c")

        # Put in notes folder and give it user-entered title
        path = os.path.join(NOTES_FOLDER, filename)

        # Attempt to write to file
        try:
            with open(path, "w") as file:
                file.write(text)
                mb.showinfo("Saved", "File saved successfully!")
        except OSError as e:
            mb.showerror("Error", f"Could not save file:\n{e}")\
        
        self.show_home_frame()

        
    def exit_program(self):
        self.root.destroy()


if __name__ == "__main__":
    app = NotesApp()