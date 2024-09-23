import customtkinter as ctk

from .objects_frame import PointFrame


class RightSidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        PointFrame(self).pack()
