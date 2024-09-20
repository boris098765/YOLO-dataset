import customtkinter as ctk
from customtkinter import CTkFont

from .objects_frame import ObjectFrame
from .points_frame import PointsFrame
from .model_name_frame import ModelNameFrame


class LeftSidebar(ctk.CTkFrame):
    def __init__(self, parent):
        self.model_frame = None
        self.obj_label = None
        self.obj_frame = None
        self.points_label = None
        self.points_frame = None

        super().__init__(parent)

        # Имя модели
        self.model_frame = ModelNameFrame(self)

        # Конфигурация объектов
        self.obj_label = ctk.CTkLabel(self, text="Objects:", font=CTkFont(size=18))
        self.obj_frame = ObjectFrame(self)

        # Конфигурация точек
        self.points_label = ctk.CTkLabel(self, text="Points:", font=CTkFont(size=18))
        self.objects_menu = ctk.CTkOptionMenu(self)
        self.points_frame = PointsFrame(self)

        self.model_frame.pack(padx=5,  pady=5)
        self.obj_label.pack(padx=10, pady=5)
        self.obj_frame.pack(padx=15, pady=5)
        self.points_label.pack(padx=10, pady=5)
        self.objects_menu.pack(padx=10, pady=5)
        self.points_frame.pack(padx=15, pady=5)

    def update_menu(self):
        obj_names = self.obj_frame.get_objects()
        self.objects_menu.configure(values=obj_names)
