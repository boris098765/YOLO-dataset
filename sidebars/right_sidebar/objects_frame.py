import customtkinter as ctk
from tkinter import ttk

pose_mode_cols     = ('c1', 'c2', 'c3', 'c4')
pose_mode_headings = ('№', 'Name', 'X', 'Y')
pose_mode_widths   = (30, 0, 30, 30)


class ObjectsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        self.table = None
        self.scrollbar = None

        super().__init__(parent)
        self.setup_table()

    def setup_table(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.table = ttk.Treeview(self, columns=pose_mode_cols, show='headings', height=10)

        for col, head, width in zip(pose_mode_cols, pose_mode_headings, pose_mode_widths):
            self.table.heading(col, text=head)

            if width != 0: self.table.column(col, width=width, stretch=False)
            else: self.table.column(col, stretch=True)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        # Кнопки
        btn_new = ctk.CTkButton(self, text="New")
        btn_edit = ctk.CTkButton(self, text="Edit")
        btn_del = ctk.CTkButton(self, text="Del")

        self.table.grid(row=0, column=0, columnspan=3, sticky='nsew')
        scrollbar.grid(row=0, column=3, sticky='ns')
        btn_new.grid(row=1, column=0, padx=5, pady=5)
        btn_edit.grid(row=1, column=1, padx=5, pady=5)
        btn_del.grid(row=1, column=2, padx=5, pady=5)