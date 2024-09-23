import customtkinter as ctk


class ModelNameFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="transparent")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self, text="Model name:").grid(row=0, column=0, padx=5)
        self.model_name = ctk.CTkEntry(self, placeholder_text="MyModel")
        self.model_name.grid(row=0, column=1, padx=5)