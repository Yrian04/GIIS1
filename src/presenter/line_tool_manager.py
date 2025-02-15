import config
from .abc.tool_manager import ToolManager
from ..model import LineTool


class LineToolManager(ToolManager):
    def __init__(self, drawer_type):
        super().__init__()
        self._drawer_type = drawer_type

    def configure(self, view):
        x1, y1 = view.input(config.start_line_prompt) 
        x2, y2 = view.input(config.end_line_prompt)

        return LineTool(self._drawer_type, x1, y1, x2, y2, config.standart_color) 