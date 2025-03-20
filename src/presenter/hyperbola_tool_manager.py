import config
from ..model.hyperbola_tool import HyperbolaTool
from .abc.tool_manager import ToolManager


class HyperbolaToolManager(ToolManager):
    def configure(self, view):
        center = view.input(config.center_hyperbola_prompt)
        point = view.input(config.point_hyperbola_prompt)
        dx = point[0] - center[0]
        dy = point[1] - center[1]
        a = abs(dx)
        b = abs(dy)
        return HyperbolaTool(center, a, b, config.standard_color)