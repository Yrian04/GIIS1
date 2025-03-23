from .abc.painter import Painter
from .abc.tool import Tool
from .painter.default_painter import DefaultPainter
from .canvas import Canvas


class PaintingManager:
    def __init__(self, painter: Painter = DefaultPainter()):
        self.painter = painter
    
    def use(self, tool: Tool, canvas: Canvas):
        drawer = tool.create()
        self.painter.draw(drawer, canvas)
