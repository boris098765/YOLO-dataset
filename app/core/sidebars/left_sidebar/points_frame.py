import customtkinter as ctk
from tkinter import ttk


class PointsFrame(ctk.CTkFrame):
    def __init__(self, parent, table_data=None):
        self.data = table_data
        self.table = None
        self.scrollbar = None

        self.new_btn = None
        self.edit_btn = None
        self.del_btn = None

        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.setup_table()

    def setup_table(self):
        self.table = ttk.Treeview(self, columns=('c1', 'c2'), show='headings')

        # Настройка колонок
        self.table.heading('c1', text="№")
        self.table.heading('c2', text="Name")
        self.table.column('c1', width=30, stretch=False)
        self.table.column('c2', stretch=True)

        # Скроллбар
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Размещение таблицы и скроллбара
        self.table.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.new_btn = ctk.CTkButton(self, text="New")
        self.edit_btn = ctk.CTkButton(self, text="Edit")
        self.del_btn = ctk.CTkButton(self, text="Del")

        self.new_btn.grid(row=1, column=0, padx=5, pady=5)
        self.edit_btn.grid(row=1, column=1, padx=5, pady=5)
        self.del_btn.grid(row=1, column=2, padx=5, pady=5)

