import customtkinter as ctk
from customtkinter import CTkFont

from .objects_frame import ClassesConfigFrame
from .model_name_frame import ModelNameFrame


class LeftSidebar(ctk.CTkFrame):
    def __init__(self, parent):
        self.model_frame = None
        self.obj_frame = None
        self.points_label = None
        self.points_frame = None

        super().__init__(parent)

        # Имя модели
        self.model_frame = ModelNameFrame(self)

        # Конфигурация объектов
        obj_label = ctk.CTkLabel(self, text="Классы:", font=CTkFont(size=18))
        self.obj_frame = ClassesConfigFrame(self)

        self.model_frame.pack(padx=5, pady=5)
        obj_label.pack(padx=10, pady=5)
        self.obj_frame.pack(padx=10, pady=5)
