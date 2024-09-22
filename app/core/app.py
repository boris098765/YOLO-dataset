import customtkinter as ctk

from .file_init import create_folders
from canvas_area import CanvasArea
from sidebars import LeftSidebar, RightSidebar


class ImageEditorApp(ctk.CTk):
    def __init__(self):
        self.left_sidebar = None
        self.right_sidebar = None
        self.canvas = None

        super().__init__()
        ctk.set_appearance_mode("dark")

        self.title("YOLOv8 Posing Dataset Editor")
        self.geometry("1200x650")

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1, minsize=200)
        self.grid_columnconfigure(1, weight=1, minsize=600)
        self.grid_columnconfigure(2, weight=1, minsize=350)

        self.left_sidebar = LeftSidebar(self)
        self.canvas = CanvasArea(self)
        self.right_sidebar = RightSidebar(self)

        self.left_sidebar.grid(row=0, column=0, sticky='ns', padx=5, pady=10)
        self.canvas.grid(row=0, column=1, sticky='nsew', padx=5, pady=10)
        self.right_sidebar.grid(row=0, column=2, sticky='ns', padx=5, pady=10)

def gg():
    create_folders()

    app = ImageEditorApp()
    app.mainloop()
