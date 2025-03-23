import config
from ..model import CircleTool
from .abc.tool_manager import ToolManager


class CircleToolManager(ToolManager):
    def configure(self, view):
        center = view.input(config.center_circle_prompt)
        point = view.input(config.point_circle_prompt)
        return CircleTool(center, point, config.default_color)
