import structlog
from structlog.typing import FilteringBoundLogger

logger: FilteringBoundLogger = structlog.get_logger()


class CanvasArea:
    def __init__(self, parent):
        self.img_tk = None
        self.canvas = None
        self.image = None
        self.img_obj = None
        self.is_dragging = False
        self.scale_factor = 1.0
        self.image_offset = [0, 0]
        self.drag_data = {"x": 0, "y": 0}
        self.k_drag = 0.5

        self._setup()

    def _setup(self):
        self.canvas = self._create_canvas(parent=self)
        self.canvas.bindings = self._bind_events(self.canvas)
        logger.info("Canvas and events set up successfully.")

        load_image_btn = self._create_button("Load Image", self.load_image)
        self._pack_widget(load_image_btn)

    def _create_canvas(self, parent):
        logger.info("Creating canvas")
        return "CanvasWidget"

    def _bind_events(self, canvas):
        logger.info("Binding events to canvas")
        return {
            "MouseWheel": self.on_scroll,
            "Control-MouseWheel": self.on_zoom,
            "Shift-MouseWheel": self.shift_scroll_drag,
            "B1-Motion": self.on_drag,
            "Button-1": self.start_drag,
            "ButtonRelease-1": self.on_canvas_click
        }

    def _create_button(self, text, command):
        logger.info(f"Creating button: {text}")
        return {"text": text, "command": command}

    def _pack_widget(self, widget):
        logger.info(f"Packing widget: {widget}")

    def load_image(self):
        file_path = "image_path_placeholder"  # Replace with actual file dialog logic
        if file_path:
            logger.info(f"Loading image from: {file_path}")
            self.image = "ImageDataPlaceholder"
            self.scale_factor = 1.0
            self.image_offset = [0, 0]
            self.show_image()

    def show_image(self):
        if self.image:
            logger.info(f"Displaying image with scale factor: {self.scale_factor}")
            self.img_tk = "ResizedImagePlaceholder"
            if self.img_obj is None:
                self.img_obj = "ImageObjectCreated"
            else:
                logger.info("Updating existing image object")
            self.update_image_position()

    def update_image_position(self):
        logger.info("Updating image position on canvas")
        # Logic to update image position

    def on_zoom(self, event):
        logger.info(f"Zoom event triggered: {event}")
        # Logic for zooming

    def start_drag(self, event):
        logger.info(f"Starting drag event: {event}")
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.is_dragging = False

    def on_drag(self, event):
        logger.info(f"Dragging event: {event}")
        # Logic for dragging

    def shift_scroll_drag(self, event):
        logger.info(f"Shift scroll drag event: {event}")
        # Logic for shift scroll drag

    def on_scroll(self, event):
        logger.info(f"Scroll event: {event}")
        # Logic for scrolling

    def on_canvas_click(self, event):
        if self.is_dragging:
            return
        logger.info(f"Canvas clicked at: {event}")
        # Logic for handling canvas click
