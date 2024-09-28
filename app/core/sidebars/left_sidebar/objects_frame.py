import customtkinter as ctk
from tkinter import ttk

from CTkMessagebox import CTkMessagebox


class ObjectFrame(ctk.CTkFrame):
    def __init__(self, parent):
        self.sidebar = parent
        self.data = []

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
        self.grid_columnconfigure(3, weight=0)

        self.setup_table()

    def setup_table(self):
        self.table = ttk.Treeview(self, columns=('c1', 'c2', 'c3'), show='headings', height=5)

        # Настройка колонок
        self.table.heading('c1', text="№")
        self.table.heading('c2', text="Name")
        self.table.heading('c3', text="P Count")
        self.table.column('c1', width=20, stretch=False)
        self.table.column('c2', stretch=True)
        self.table.column('c3', width=60, stretch=False)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Размещение таблицы и скроллбара
        self.table.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        # Кнопки
        self.new_btn = ctk.CTkButton(self, text="New", command=self.new_item)
        self.edit_btn = ctk.CTkButton(self, text="Edit", command=self.edit_item)
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

    def find_min_num(self):
        if len(self.data) == 0: return 1
        occupied = {item[0] for item in self.data}

        first_available = 1
        while first_available in occupied:
            first_available += 1
        return first_available

    def new_item(self):
        self.data.append((self.find_min_num(), 'name', 0))
        self.update_table()

    def get_selected_row(self):
        selected_item = self.table.selection()
        if not selected_item: return False

        ids = []
        for item_id in selected_item:
            ids.append(item_id)
        return ids

    def edit_item(self):
        selected_items = self.get_selected_row()
        if not selected_items:
            CTkMessagebox(self, icon="cancel", title="EDIT ERROR", message="Nothing to edit!!!")
            return
        if len(selected_items) > 1: return

        selected_id = selected_items[0]
        row_values = self.table.item(selected_id)['values']
        if not row_values: return

        # Окно для редактирования
        edit_window = ctk.CTkToplevel(self)
        edit_window.geometry('300x200')
        edit_window.title("Edit Item")

        edit_window.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(edit_window, text="№").grid(row=0, column=0, padx=5, pady=10)
        num_entry = ctk.CTkEntry(edit_window)
        num_entry.grid(row=0, column=1, padx=10, pady=10)
        num_entry.insert(0, row_values[0])

        ctk.CTkLabel(edit_window, text="Name").grid(row=1, column=0, padx=5, pady=10)
        name_entry = ctk.CTkEntry(edit_window)
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        name_entry.insert(0, row_values[1])

        ctk.CTkLabel(edit_window, text="P Count").grid(row=2, column=0, padx=5, pady=10)
        count_entry = ctk.CTkEntry(edit_window)
        count_entry.grid(row=2, column=1, padx=5, pady=10)
        count_entry.insert(0, row_values[2])

        def save_edit():
            new_num = int(num_entry.get())
            new_name = name_entry.get()
            new_count = int(count_entry.get())

            # Обновляем данные в таблице
            self.delete_data_item(row_values[0])
            self.data.append((new_num, new_name, new_count))
            self.update_table()
            edit_window.destroy()

        save_btn = ctk.CTkButton(edit_window, text="Save", command=save_edit)
        save_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def delete_data_item(self, id_value):
        self.data = [item for item in self.data if item[0] != id_value]

    def delete_items(self):
        selected_items = self.get_selected_row()
        if not selected_items:
            CTkMessagebox(self, icon="cancel", title="DELETE ERROR", message="Nothing to delete!!!")
            return

        ids = []
        for item_id in selected_items:
            row_values = self.table.item(item_id)['values']
            if row_values: ids.append(row_values[0])

        for id_val in ids: self.delete_data_item(id_val)

        self.update_table()

    def get_objects(self):
        objects = [self.table.item(obj)['values'][1] for obj in self.table.get_children()]
        return objects
