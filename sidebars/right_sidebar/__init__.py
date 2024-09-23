import customtkinter as ctk
from customtkinter import CTkFont

from .objects_frame import ObjectsFrame


class RightSidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        boxes_label = ctk.CTkLabel(self, text="Таблица точек / боксов", font=CTkFont(size=18))

        boxes_label.pack(padx=5, pady=5)
        ObjectsFrame(self).pack(padx=10, pady=5)
