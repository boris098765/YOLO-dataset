import customtkinter as ctk
from customtkinter import CTkFont

from tkinter import ttk

pose_mode_cols     = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
pose_mode_headings = ('№', 'Name', 'X', 'Y', 'Edit', 'Delete')
pose_mode_widths   = (40, 0, 30, 30, 40, 50)


class PointFrame(ctk.CTkFrame):
    def __init__(self, parent):
        self.table = None

        super().__init__(parent)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.setup_table()

    def setup_table(self):
        label = ctk.CTkLabel(self, text="Таблица точек / боксов", font=CTkFont(size=18))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.table = ttk.Treeview(self, columns=pose_mode_cols, show='headings')

        for col, head, width in zip(pose_mode_cols, pose_mode_headings, pose_mode_widths):
            self.table.heading(col, text=head)

            if width != 0: self.table.column(col, width=width, stretch=False)
            else: self.table.column(col, stretch=True)

        self.table.grid(row=1, column=0, columnspan=2)

        ctk.CTkButton(self, text="New").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkButton(self, text="Del").grid(row=2, column=1, padx=5, pady=5)