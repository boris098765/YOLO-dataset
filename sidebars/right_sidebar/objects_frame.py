from CTkMessagebox import CTkMessagebox

from table_frame import TableFrame


class ObjectsFrame(TableFrame):
    def __init__(self, parent):
        columns = ('c1', 'c2', 'c3', 'c4', 'c5')
        headings = ('', '№', 'Name', 'X', 'Y')
        widths = (20, 30, 0, 50, 50)

        super().__init__(parent, columns, headings, widths)

    def new_item(self):
        self.data.append((0, self.find_min_num(), 'name', 0, 0))
        self.update_table()

    def delete_object(self, parent_id, id):
        if parent_id == 0:
            self.delete_data_by_parent_id(id)
            self.delete_data_by_id(parent_id, id)
        else:
            pass # TODO: доделать

    def edit_item(self):
        pass
