import customtkinter as ctk

from CTkMessagebox import CTkMessagebox

from table_frame import TableFrame

pose_mode_cols     = ('c1', 'c2', 'c3', 'c4')
pose_mode_headings = ('', '№', 'Name', 'Count')
pose_mode_widths   = (20, 30, 0, 40)


class ClassesConfigFrame(TableFrame):
    def __init__(self, parent):
        columns = ('c1', 'c2', 'c3', 'c4')
        headings = ('', '№', 'Name', 'Count')
        widths = (20, 30, 0, 40)

        super().__init__(parent, columns, headings, widths)

    def new_item(self):
        self.data.append((0, self.find_min_num(), 'name', 0))
        self.update_table()

    def delete_object(self, parent_id, id):
        if parent_id == 0:
            self.delete_data_by_parent_id(id)
            self.delete_data_by_id(parent_id, id)
        else:
            i = self.get_i_by_id(0, parent_id)
            item = list(self.data[i])
            item[3] -= 1
            self.data[i] = tuple(item)
            self.delete_data_by_id(parent_id, id)

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

        ctk.CTkLabel(edit_window, text="№").grid(row=0, column=0, padx=5, pady=10)
        ctk.CTkLabel(edit_window, text="Name").grid(row=1, column=0, padx=5, pady=10)
        ctk.CTkLabel(edit_window, text="P Count").grid(row=2, column=0, padx=5, pady=10)

        num_entry = ctk.CTkEntry(edit_window)
        name_entry = ctk.CTkEntry(edit_window)
        count_entry = ctk.CTkEntry(edit_window)

        num_entry.grid(row=0, column=1, padx=10, pady=10)
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        count_entry.grid(row=2, column=1, padx=5, pady=10)

        num_entry.insert(0, selected_values[1])
        name_entry.insert(0, selected_values[2])
        count_entry.insert(0, selected_values[3])

        if poboch:
            count_entry.configure(state='disabled', fg_color="#D3D3D3")

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