import customtkinter as ctk
from tkinter import ttk

from CTkMessagebox import CTkMessagebox

pose_mode_cols     = ('c1', 'c2', 'c3', 'c4')
pose_mode_headings = ('', '№', 'Name', 'P Count')
pose_mode_widths   = (20, 20, 0, 60)


class ObjectFrame(ctk.CTkFrame):
    def __init__(self, parent):
        # Формат данных:
        # parent_id, id, name, count
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
        self.table = ttk.Treeview(self, columns=('c1', 'c2', 'c3', 'c4'), show='headings', height=15)

        # Настройка колонок
        for col, head, width in zip(pose_mode_cols, pose_mode_headings, pose_mode_widths):
            self.table.heading(col, text=head)

            if width != 0: self.table.column(col, width=width, stretch=False)
            else: self.table.column(col, stretch=True)

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

    def get_i_by_id(self, parent_id, id):
        i = -1
        n = 0
        for item in self.data:
            if item[0]==parent_id and item[1]==id: i = n
            n+=1
        return i

    def delete_data_by_id(self, parent_id, id):
        self.data = [item for item in self.data if not (item[0] == parent_id and item[1] == id)]

    def delete_data_by_parent_id(self, parent_id):
        self.data = [item for item in self.data if not (item[0] == parent_id)]

    def get_children(self, parent_id=0):
        return [item for item in self.data if item[0]==parent_id]

    # Удалить значение в БД вместе с дочерними
    def delete_object(self, parent_id, id):
        if parent_id == 0:
            self.delete_data_by_parent_id(id)
            self.delete_data_by_id(parent_id, id)
        else:
            i = self.get_i_by_id(0, parent_id)
            item = list(self.data[i])
            print('old item:', item)
            item[3] -= 1
            print('new item:', item)
            self.data[i] = tuple(item)
            self.delete_data_by_id(parent_id, id)

    def delete_items(self):
        selected_items = self.get_selected_row()
        if not selected_items:
            CTkMessagebox(self, icon="cancel", title="DELETE ERROR", message="Nothing to delete!!!")
            return

        ids = []
        for item_id in selected_items:
            row_values = self.table.item(item_id)['values']
            if row_values: ids.append((row_values[0], row_values[1]))

        for parent_id, id in ids:
            self.delete_object(parent_id, id)
        self.update_table()

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

    def find_min_num(self):
        if len(self.data) == 0: return 1

        parents = {item for item in self.data if item[0]==0}
        occupied = {item[1] for item in parents}

        first_available = 1
        while first_available in occupied:
            first_available += 1

        return first_available

    def new_item(self):
        self.data.append((0, self.find_min_num(), 'name', 0))
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
        if len(selected_items) > 1:
            CTkMessagebox(self, icon="cancel", title="EDIT ERROR", message="Too much to edit!!!")
            return

        selected_id = selected_items[0]
        selected_values = self.table.item(selected_id)['values']
        if not selected_values: return

        parent_id, obj_id = selected_values[:2]
        poboch = (parent_id != 0)

        # Окно для редактирования
        edit_window = ctk.CTkToplevel(self)
        edit_window.geometry('300x200')
        edit_window.title("Edit Item")

        edit_window.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(edit_window, text="№").grid(row=0, column=0, padx=5, pady=10)
        num_entry = ctk.CTkEntry(edit_window)
        num_entry.grid(row=0, column=1, padx=10, pady=10)
        num_entry.insert(0, selected_values[1])

        ctk.CTkLabel(edit_window, text="Name").grid(row=1, column=0, padx=5, pady=10)
        name_entry = ctk.CTkEntry(edit_window)
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        name_entry.insert(0, selected_values[2])

        ctk.CTkLabel(edit_window, text="P Count").grid(row=2, column=0, padx=5, pady=10)
        count_entry = ctk.CTkEntry(edit_window)
        count_entry.grid(row=2, column=1, padx=5, pady=10)
        count_entry.insert(0, selected_values[3])

        if poboch:
            count_entry.configure(state='disabled')

        def save_edit():
            new_id = int(num_entry.get())
            new_name = name_entry.get()
            new_count = int(count_entry.get())

            new_data = (parent_id, new_id, new_name, new_count)

            # Обновляем данные в таблице
            data_id = self.get_i_by_id(parent_id, obj_id)
            self.data[data_id] = new_data

            # Если это родитель, обновляем количество дочерних элементов
            if not poboch and new_count != selected_values[3]:
                self.data = [item for item in self.data if item[0] != obj_id]  # Удаление старых детей
                for i in range(new_count):
                    self.data.append((obj_id, i+1, '', 0))  # Добавляем новые дочерние элементы

            self.update_table()
            edit_window.destroy()

        save_btn = ctk.CTkButton(edit_window, text="Save", command=save_edit)
        save_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def get_objects(self):
        objects = [self.table.item(obj)['values'][1] for obj in self.table.get_children()]
        return objects
