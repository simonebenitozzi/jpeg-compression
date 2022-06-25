import sys
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

from Part2.bin.GUI.helper import execute
from Part2.resources.constants import RESOURCES_DIRECTORY


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Jpeg Compression')
        self.geometry("350x150")

        self.__f_label = ttk.Label(self, text="f:")
        self.__d_label = ttk.Label(self, text="d:")

        self.__f_entry = tk.Entry(self)
        self.__d_entry = tk.Entry(self)
        self.__button_explore = ttk.Button(self,
                                           text="Browse Files",
                                           command=self.__browse_files)

        self.__button_execute = ttk.Button(self,
                                           text="Execute",
                                           command=self.__execute)

        self.__file_path = None
        self.__d = None
        self.__f = None

        self.__create_widgets()

    def __create_widgets(self):
        self.__f_label.grid(row=0, column=0, padx=20, pady=10)
        self.__d_label.grid(row=1, column=0, padx=20, pady=10)

        self.__f_entry.grid(column=1, row=0, padx=20, pady=10)
        self.__d_entry.grid(column=1, row=1, padx=20, pady=10)

        self.__button_explore.grid(row=0, column=2, padx=20, pady=10)
        self.__button_execute.grid(row=1, column=2, padx=20, pady=10)

    def __browse_files(self):
        self.__file_path = filedialog.askopenfilename(initialdir=RESOURCES_DIRECTORY,
                                                      title="Select a File",
                                                      filetypes=(("Bmp files",
                                                                  "*.bmp*"),))

    def __execute(self):
        if self.__f_entry.get() == "" or self.__d_entry.get() == "" or self.__file_path is None:
            tkinter.messagebox.showerror(title="Missing Value!",
                                         message="Insert value inside entry and choose an image!")
            return

        if not (self.__d_entry.get().isnumeric() or self.__d_entry.get().isnumeric()):
            tkinter.messagebox.showerror(title="Value Error!", message="Insert only numbers!")
            return

        f = int(self.__f_entry.get())
        d = int(self.__d_entry.get())

        if not (0 < d < (2 * f - 2)):
            tkinter.messagebox.showerror(title="Value Error!", message="Insert true value!")
            return

        execute(self.__file_path, f, d)
