from ..abc.event import Event

import config

from ..view import MainView
from ..model import (
    PaintingManager,
    LineDDADrawer, 
    Canvas,
    Color,
    DebagPainter, 
    DefaultPainter,
    LineBresenhamDrawer,
    LineWuDrawer,
)
from .abc.tool_manager import ToolManager
from .line_tool_manager import LineToolManager
from .circle_tool_manager import CircleToolManager
from .eliipse_tool_manager import EllipseToolManager
from .parabola_tool_manager import ParabolaToolManager
from .hyperbola_tool_manager import HyperbolaToolManager


class MainPresenter:
    def __init__(
        self,
        canvas: Canvas,
        view: MainView,
        painting_manager: PaintingManager | None = None,
    ):
        self._canvas = canvas
        self._canvas.callback = self._canvas_callback
        self._view = view
        self._debug_mode = False
        self._debug_step = config.debug_step
        self._painting_manager = painting_manager if painting_manager is not None else PaintingManager()
        
        subscribe_map = {
            'Main.Debug.Debug mode': self._debug_checkbutton_click_handler,
            'Main.Insert.Line.DDA': self._get_figure_handler(LineToolManager(LineDDADrawer)),
            'Main.Insert.Line.Bresenham': self._get_figure_handler(LineToolManager(LineBresenhamDrawer)),
            'Main.Insert.Line.Wu': self._get_figure_handler(LineToolManager(LineWuDrawer)),
            'Main.Insert.Quadratic curve.Circle': self._get_figure_handler(CircleToolManager()),
            'Main.Insert.Quadratic curve.Ellipse': self._get_figure_handler(EllipseToolManager()),
            'Main.Insert.Quadratic curve.Parabola': self._get_figure_handler(ParabolaToolManager()),
            'Main.Insert.Quadratic curve.Hyperbola': self._get_figure_handler(HyperbolaToolManager()),
        }
        
        for tag, callback in subscribe_map.items():
            self._view.subscribe(tag, callback)

    def _canvas_callback(self, x: int, y: int, color: Color):
        self._view.set_cell(x, y, color)

    def _debug_painter_callback(self):
        self._view.show_info(config.debug_info)
        result = self._view.debug_wait()
        self._view.show_info(config.start_info_str)
        return result

    def _debug_checkbutton_click_handler(self, event: Event):
        self._debug_mode = not self._debug_mode
        self._painting_manager.painter = DebagPainter(self._debug_painter_callback, self._debug_step) if self._debug_mode else DefaultPainter()
        self._view.on_change_debug_mode(self._debug_mode)

    def _get_line_handler(self, line_drawer_type):
        def handler(event: Event):
            tool = LineToolManager(line_drawer_type).configure(self._view)
            self._painting_manager.use(tool, self._canvas)
        return handler

    def _circle_handler(self, event: Event):
        tool = CircleToolManager().configure(self._view)
        self._painting_manager.use(tool, self._canvas)

    def _ellipse_handler(self, event: Event):
        tool = EllipseToolManager().configure(self._view)
        self._painting_manager.use(tool, self._canvas)

    def _parabola_handler(self, event: Event):
        tool = ParabolaToolManager().configure(self._view)
        self._painting_manager.use(tool, self._canvas)

    def _hyperbola_handler(self, event: Event):
        tool = HyperbolaToolManager().configure(self._view)
        self._painting_manager.use(tool, self._canvas)
        
    def _get_figure_handler(self, tool_manager: ToolManager):
        def handler(event: Event):
            tool = tool_manager.configure(self._view)
            self._painting_manager.use(tool, self._canvas)
        
        return handler
