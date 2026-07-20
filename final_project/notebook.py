import os
import tkinter as tk
from tkinter import ttk, messagebox as mb

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


def ensure_notes_folder():
    """Creates folder for notes if it doesn't
    already exist."""
    os.makedirs(NOTES_FOLDER, exist_ok=True)    


def get_notes_list():
    """Creates list of names of all files in 
    notes folder without .txt extension."""
    ensure_notes_folder()
    files_list = os.listdir(NOTES_FOLDER)
    notes_list = []
    for filename in files_list:
        notes_list.append(filename[0:-4])
    return notes_list


def get_note_path(note_title):
    return os.path.join(NOTES_FOLDER, note_title + ".txt")


def get_note_title(note_path):
    filename = os.path.basename(note_path)
    split_filename = os.path.splitext(filename)
    note_title = split_filename[0]
    return note_title


def write_text_file(path, mode, text):
    with open(path, mode) as file:
        file.write(text)


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


    def refresh_note_selection(self):
        # Clear existing note selection
        self.note_selection.delete(0, tk.END)

        # Insert new notes list
        notes_list = get_notes_list()
        for i in range(len(notes_list)):
            self.note_selection.insert(i, notes_list[i])        


    def create_home_frame(self):
        self.home_frame = ttk.Frame(self.root)

        # List of existing notes for user to choose from
        self.note_selection = tk.Listbox(self.home_frame)
        self.refresh_note_selection()
        self.note_selection.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=PADDING_SIZE, 
            pady=PADDING_SIZE, 
            sticky="nsew"
        )

        # Button to open selected note
        self.open_note_button = ttk.Button(
            self.home_frame,
            text="Open",
            command=self.open_note
        )
        self.open_note_button.grid(
            row=1, 
            column=0, 
            padx=PADDING_SIZE, 
            pady=PADDING_SIZE
        )

        # Button to delete selected note
        self.delete_note_button = ttk.Button(
            self.home_frame,
            text="Delete",
            command=self.delete_note
        )
        self.delete_note_button.grid(
            row=1,
            column=1,
            padx=PADDING_SIZE,
            pady=PADDING_SIZE
        )

        # Button to create new note
        self.new_note_button = ttk.Button(
            self.home_frame,
            text="New",
            command=self.new_note
        )
        self.new_note_button.grid(
            row=1, 
            column=2, 
            padx=PADDING_SIZE, 
            pady=PADDING_SIZE
        )

        # Button to close the program
        self.exit_button = ttk.Button(
            self.home_frame,
            text="Exit",
            command=self.exit_program
        )
        self.exit_button.grid(
            row=1, 
            column=3, 
            padx=PADDING_SIZE, 
            pady=PADDING_SIZE, 
            sticky="w"
        )

        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(3, weight=1)

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
            columnspan=2,
            padx=PADDING_SIZE,
            pady=PADDING_SIZE,
            sticky="ew"
        )

        # Box for note body
        self.text_box = tk.Text(self.editor_frame)
        self.text_box.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=PADDING_SIZE,
            sticky="nsew"
        )

        # Button to save contents of editor to a text file
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

        # Button to discard changes and return home
        self.discard_button = ttk.Button(
            self.editor_frame,
            text="Discard",
            command=self.show_home_frame
        )
        self.discard_button.grid(
            row=2,
            column=1,
            padx=PADDING_SIZE,
            pady=PADDING_SIZE,
            sticky="w"
        )

        self.editor_frame.grid_rowconfigure(1, weight=1)
        self.editor_frame.grid_columnconfigure(1, weight=1)

        self.editor_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


    def show_home_frame(self):
        self.refresh_note_selection()
        self.home_frame.tkraise()


    def show_editor_frame(self):
        self.editor_frame.tkraise()


    def get_selected_note(self):
        """Returns the path of the currently selected note."""
        notes_list = get_notes_list()

        # Get index of selected note
        try:
            selected_index = self.note_selection.curselection()[0]
        except IndexError:
            mb.showerror("Error", "Please select a note.")
            return None
        
        # Get path of selected note
        note_title = notes_list[selected_index]
        path = get_note_path(note_title)
        return path


    def open_note(self):
        """Opens the editor and populates it with currently selected note."""

        path = self.get_selected_note()
        note_title = get_note_title(path)

        # Clear editor and populate with note contents
        self.clear_editor()
        self.title_entry.insert(0, note_title)
        try:
            with open(path, "r") as file:
                self.text_box.insert(tk.END, file.read())
        except FileNotFoundError as e:
            mb.showerror("Error", f"Could not open file:\n{e}")

        self.show_editor_frame()


    def clear_editor(self):
        """Clears editor frame."""
        self.title_entry.delete(0, tk.END)
        self.text_box.delete("1.0", "end-1c")


    def new_note(self):
        """Opens empty editor."""
        self.clear_editor()
        self.show_editor_frame()


    def save_note(self):
        """Saves contents of editor into a text file with the name
        the user entered."""

        ensure_notes_folder()
        
        # Get title and note text
        title = self.title_entry.get()
        filename = create_filename(title)
        text = self.text_box.get("1.0", "end-1c")

        # Put in notes folder and give it user-entered title
        path = os.path.join(NOTES_FOLDER, filename)

        # Attempt to write to file
        try:
            write_text_file(path, "x", text)
            mb.showinfo("Saved", "File saved successfully!")
        except FileExistsError:
            overwrite = mb.askyesno("Overwrite file?",
                f"{filename} already exists. Would you like to overwrite it?")
            if overwrite:
                write_text_file(path, "w", text)
                mb.showinfo("Saved", "File saved successfully!")
            else:
                return
        except OSError as e:
            mb.showerror("Error", f"Could not save file:\n{e}")
            return
        
        self.show_home_frame()


    def delete_note(self):
        """Deletes the selected note."""
        #TODO: write function to delete selected note
        path = self.get_selected_note()
        if path is not None:
            delete = mb.askyesno("Delete file?",
                "Are you sure you want to delete this file?")
            if delete:
                os.remove(path)
            self.refresh_note_selection()

        
    def exit_program(self):
        self.root.destroy()


if __name__ == "__main__":
    app = NotesApp()