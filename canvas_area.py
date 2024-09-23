import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk


class CanvasArea(ctk.CTkFrame):
    def __init__(self, parent):
        self.img_tk = None

        super().__init__(parent)
        self.canvas = ctk.CTkCanvas(self, bg='white')
        self.canvas.pack(expand=True, fill='both', pady=10)

        self.image = None
        self.img_obj = None

        self.is_dragging = None

        self.scale_factor = 1.0
        self.image_offset = [0, 0]
        self.drag_data = {"x": 0, "y": 0}
        self.k_drag = 0.5

        # Привязываем события к canvas
        self.canvas.bind("<MouseWheel>", self.on_scroll)
        self.canvas.bind("<Control-MouseWheel>", self.on_zoom)
        self.canvas.bind("<Shift-MouseWheel>", self.shift_scroll_drag)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_click)

        load_image_btn = ctk.CTkButton(self, text="Load Image", command=self.load_image)
        load_image_btn.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if file_path:
            self.image = Image.open(file_path)
            self.scale_factor = 1.0
            self.image_offset = [0, 0]
            self.show_image()

    def show_image(self):
        if self.image:
            img_resized = self.image.resize(
                (int(self.image.width * self.scale_factor), int(self.image.height * self.scale_factor)),
                Image.LANCZOS
            )
            self.img_tk = ImageTk.PhotoImage(img_resized)
            if self.img_obj is None:
                self.img_obj = self.canvas.create_image(0, 0, anchor='nw', image=self.img_tk)
            else:
                self.canvas.itemconfig(self.img_obj, image=self.img_tk)
            self.update_image_position()

    def update_image_position(self):
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()

        img_w = self.image.width * self.scale_factor
        img_h = self.image.height * self.scale_factor

        self.image_offset[0] = min(0, max(canvas_w - img_w, self.image_offset[0]))
        self.image_offset[1] = min(0, max(canvas_h - img_h, self.image_offset[1]))

        self.canvas.coords(self.img_obj, self.image_offset[0], self.image_offset[1])
        self.canvas.config(scrollregion=self.canvas.bbox(ctk.ALL))

    def on_zoom(self, event):
        scale = 1.0
        if event.delta > 0:
            scale = 1.2
        elif event.delta < 0:
            scale = 0.8

        new_scale_factor = self.scale_factor * scale
        if 0.1 < new_scale_factor < 20:
            self.scale_factor = new_scale_factor

        mouse_x, mouse_y = event.x, event.y
        canvas_x, canvas_y = self.canvas.canvasx(mouse_x), self.canvas.canvasy(mouse_y)

        self.image_offset[0] = canvas_x - (canvas_x - self.image_offset[0]) * scale
        self.image_offset[1] = canvas_y - (canvas_y - self.image_offset[1]) * scale

        self.show_image()

    def start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.is_dragging = False

    def on_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        if abs(dx) > 5 or abs(dy) > 5:  # Минимальный порог для начала перетаскивания
            self.is_dragging = True
        self.image_offset[0] += dx
        self.image_offset[1] += dy
        self.update_image_position()

        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def shift_scroll_drag(self, event):
        dx = event.delta * self.k_drag
        self.image_offset[0] += dx
        self.update_image_position()

    def on_scroll(self, event):
        dy = event.delta * self.k_drag
        self.image_offset[1] += dy
        self.update_image_position()

    def on_canvas_click(self, event):
        if self.is_dragging:
            return

        if not self.image:
            return

        canvas_x, canvas_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        img_x = (canvas_x - self.image_offset[0]) / self.scale_factor
        img_y = (canvas_y - self.image_offset[1]) / self.scale_factor

        if 0 <= img_x <= self.image.width and 0 <= img_y <= self.image.height:
            coord_message = f"Clicked at: ({int(img_x)}, {int(img_y)})"
            print(coord_message)
