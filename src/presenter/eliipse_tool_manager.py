import config
from ..model.ellipse_tool import EllipseTool
from .abc.tool_manager import ToolManager


class EllipseToolManager(ToolManager):
    def configure(self, view):
        first_point = view.input(config.upper_left_corner_ellipse_prompt)
        second_point = view.input(config.lower_right_corner_ellipse_prompt)
        upper_left_corner = (min(first_point[0], second_point[0]),
                             min(first_point[1], second_point[1]))
        lower_right_corner = (max(first_point[0], second_point[0]),
                              max(first_point[1], second_point[1]))
        return EllipseTool(upper_left_corner, lower_right_corner, config.standart_color)
