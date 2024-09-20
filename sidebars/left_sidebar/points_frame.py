import customtkinter as ctk
from tkinter import ttk

from CTkMessagebox import CTkMessagebox


class PointsFrame(ctk.CTkFrame):
    def __init__(self, parent, table_data=None):
        self.sidebar = parent
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
        self.del_btn = ctk.CTkButton(self, text="Del", command=self.delete_items)

        self.new_btn.grid(row=1, column=0, padx=5, pady=5)
        self.edit_btn.grid(row=1, column=1, padx=5, pady=5)
        self.del_btn.grid(row=1, column=2, padx=5, pady=5)

    def update_table(self):
        for i in self.table.get_children():
            self.table.delete(i)

        sorted_data = sorted(self.data, key=lambda x: x[0])
        for obj in sorted_data:
            self.table.insert('', 'end', values=obj)

        self.sidebar.update_menu()

    def get_selected_row(self):
        selected_item = self.table.selection()
        if not selected_item: return False

        ids = []
        for item_id in selected_item:
            ids.append(item_id)
        return ids

    def delete_data_item(self, id_value):
        self.data = [item for item in self.data if item[0] != id_value]

    def delete_items(self):
        selected_items = self.get_selected_row()
        if not selected_items:
            CTkMessagebox(self, icon="cancel", title="DELETE ERROR", message="Nothing to delete!!!")
            return
