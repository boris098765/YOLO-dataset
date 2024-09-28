import structlog
from structlog.typing import FilteringBoundLogger

logger: FilteringBoundLogger = structlog.get_logger()


class ImageEditorApp:
    def __init__(self, appearance_mode: str, title: str, size_x: int, size_y: int) -> None:
        self.left_sidebar = None
        self.right_sidebar = None
        self.canvas = None

        self.appearance_mode = appearance_mode
        self.title = title
        self.size_x = size_x
        self.size_x = size_y

        self._setup()

    def _setup(self) -> None:
        self.grid_config = [
            {'row': 0, 'weight': 1},
            {'column': 0, 'weight': 1, 'minsize': 200},
            {'column': 1, 'weight': 1, 'minsize': 600},
            {'column': 2, 'weight': 1, 'minsize': 350}
        ]

        self._initialize_components()

    def _initialize_components(self):
        self.left_sidebar = self._create_component("LeftSidebar")
        self.right_sidebar = self._create_component("RightSidebar")
        self.canvas = self._create_component("CanvasArea")

        self._place_components()

    def _create_component(self, component_name: str):
        logger.info(f"Creating component: {component_name}")
        return component_name

    def _place_components(self):
        components = [
            {'component': self.left_sidebar, 'row': 0, 'column': 0, 'sticky': 'ns', 'padx': 5, 'pady': 10},
            {'component': self.right_sidebar, 'row': 0, 'column': 2, 'sticky': 'ns', 'padx': 5, 'pady': 10},
            {'component': self.canvas, 'row': 0, 'column': 1, 'sticky': 'nsew', 'padx': 5, 'pady': 10},
        ]

        for component in components:
            logger.info(f"Placing component: {component['component']}", position=component)