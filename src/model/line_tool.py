from .abc.tool import Tool
from ..abc.color import Color
from .abc.line_drawer import LineDrawer


class LineTool(Tool):
    def __init__(
        self,
        drawer_type,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        color: Color,
    ):
        super().__init__()
        self._drawer_type = drawer_type
        self.start = (start_x, start_y)
        self.end = (end_x, end_y)
        self.color = color

    def create(self):
        return self._drawer_type(self.start, self.end, self.color)
