from .abc.tool_manager import ToolManager
from ..model import LineTool

import config


class LineToolManager(ToolManager):
    def __init__(self, drawer_type):
        super().__init__()
        self._drawer_type = drawer_type

    def configure(self, view):
        x1, y1 = view.input('Нажмите на начало отрезка.') 
        x2, y2 = view.input('Нажмите на конец отрезка.')

        return LineTool(self._drawer_type, x1, y1, x2, y2, config.standart_color) 