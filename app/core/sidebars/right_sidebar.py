import customtkinter as ctk
from tkinter import ttk


pose_mode_cols     = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
pose_mode_headings = ('№', 'Name', 'X', 'Y', 'Edit', 'Delete')
pose_mode_widths   = (40, 0, 30, 30, 40, 50)

class PointTable(ctk.CTkFrame):
    def __init__(self, parent, table_data=None):
        self.data = table_data
        self.table = None

        super().__init__(parent, fg_color='white')
        self.setup_table()

        if self.data:
            self.update_table()

    def setup_table(self):
        self.table = ttk.Treeview(self, columns=pose_mode_cols, show='headings')

        for col, head, width in zip(pose_mode_cols, pose_mode_headings, pose_mode_widths):
            self.table.heading(col, text=head)

            if width != 0:
                self.table.column(col, width=width, stretch=False)
            else:
                self.table.column(col, stretch=True)

        self.table.pack()

    def update_table(self):
        self.clear_table()
        if not self.data: return

        for values in self.data:
            self.table.insert('', 'end', values=values)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)


class RightSidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="Таблица точек / боксов").pack(padx=10, pady=5)

        self.table = PointTable(self)
        self.table.pack(padx=10, pady=5)
