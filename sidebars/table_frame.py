import customtkinter as ctk
from tkinter import ttk

from CTkMessagebox import CTkMessagebox


class TableFrame(ctk.CTkFrame):
    def __init__(self, parent, columns, headings, widths):
        self.data = []
        self.table = None
        self.new_btn = None
        self.edit_btn = None
        self.del_btn = None
        self.scrollbar = None

        self.columns = columns
        self.headings = headings
        self.widths = widths

        super().__init__(parent)
        self.setup_table()

    def new_item(self):
        pass

    def delete_object(self, parent_id, id):
        pass

    def edit_item(self):
        pass

    def setup_table(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.table = ttk.Treeview(self, columns=self.columns, show='headings', height=10)

        # Настройка колонок
        for col, head, width in zip(self.columns, self.headings, self.widths):
            self.table.heading(col, text=head)
            if width != 0:
                self.table.column(col, width=width, stretch=False)
            else:
                self.table.column(col, stretch=True)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        self.table.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.new_btn = ctk.CTkButton(self, text="New", command=self.new_item)
        self.edit_btn = ctk.CTkButton(self, text="Edit", command=self.edit_item)
        self.del_btn = ctk.CTkButton(self, text="Del", command=self.delete_items)

        self.new_btn.grid(row=1, column=0, padx=5, pady=5)
        self.edit_btn.grid(row=1, column=1, padx=5, pady=5)
        self.del_btn.grid(row=1, column=2, padx=5, pady=5)

    def delete_items(self):
        selected_items = self.get_selected_row()
        if not selected_items:
            CTkMessagebox(self, icon="cancel", title="DELETE ERROR", message="Nothing to delete!!!")
            return

        ids = []
        for item_id in selected_items:
            row_values = self.table.item(item_id)['values']
            if row_values:
                ids.append((row_values[0], row_values[1]))

        for parent_id, id in ids:
            self.delete_object(parent_id, id)
        self.update_table()

    def get_i_by_id(self, parent_id, id):
        i = -1
        n = 0
        for item in self.data:
            if item[0] == parent_id and item[1] == id:
                i = n
            n += 1
        return i

    def delete_data_by_id(self, parent_id, id):
        self.data = [item for item in self.data if not (item[0] == parent_id and item[1] == id)]

    def delete_data_by_parent_id(self, parent_id):
        self.data = [item for item in self.data if not (item[0] == parent_id)]

    def get_children(self, parent_id=0):
        return [item for item in self.data if item[0] == parent_id]

    def find_min_num(self):
        if len(self.data) == 0:
            return 1

        parents = {item for item in self.data if item[0] == 0}
        occupied = {item[1] for item in parents}

        first_available = 1
        while first_available in occupied:
            first_available += 1

        return first_available

    def get_selected_row(self):
        selected_item = self.table.selection()
        if not selected_item:
            return False

        ids = []
        for item_id in selected_item:
            ids.append(item_id)
        return ids

    def update_table(self):
        # Очистка таблицы
        for i in self.table.get_children():
            self.table.delete(i)

        # Объекты
        parents = self.get_children(0)
        for el in parents:
            parent_id, point_count = el[1], el[3]
            parent_item = self.table.insert('', 'end', values=el)

            children = self.get_children(parent_id)
            for child in children:
                self.table.insert(parent_item, 'end', values=child)
