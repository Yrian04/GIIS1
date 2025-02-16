from ..abc.event import Event

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
from .line_tool_manager import LineToolManager
from .circle_tool_manager import CircleToolManager
import config

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

        self._view.subscribe('Main.Debug.Debug mode', self._debug_checkbutton_click_handler)
        self._view.subscribe('Main.Insert.Line.DDA', self._get_line_handler(LineDDADrawer))
        self._view.subscribe('Main.Insert.Line.Bresenham', self._get_line_handler(LineBresenhamDrawer))
        self._view.subscribe('Main.Insert.Line.Wu', self._get_line_handler(LineWuDrawer))
        self._view.subscribe('Main.Insert.Quadratic curve.Circle', self._circle_handler)

    def _canvas_callback(self, x: int, y: int, color: Color):
        self._view.set_cell(x, y, color)

    def _debug_painter_callback(self):
        self._view.show_info(config.debug_info)
        result = self._view.debug_wait()
        self._view.show_info(config.start_info_str)
        return result

    def _debug_checkbutton_click_handler(self, event: Event):
        self._debug_mode = not self._debug_mode
        self._painting_manager.painter = DefaultPainter() if not self._debug_mode else DebagPainter(self._debug_painter_callback, self._debug_step)
        self._view.on_change_debug_mode(self._debug_mode)

    def _get_line_handler(self, line_drawer_type):
        def handler(event: Event):
            tool = LineToolManager(line_drawer_type).configure(self._view)
            self._painting_manager.use(tool, self._canvas)
        return handler

    def _circle_handler(self, event: Event):
        tool = CircleToolManager().configure(self._view)
        self._painting_manager.use(tool, self._canvas)
