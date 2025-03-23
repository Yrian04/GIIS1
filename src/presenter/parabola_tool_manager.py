import config
from ..model import ParabolaTool, ParabolaDirection
from .abc.tool_manager import ToolManager


class ParabolaToolManager(ToolManager):
    def configure(self, view):
        top = view.input(config.top_parabola_prompt)
        point = view.input(config.direction_parabola_prompt)
        delta = point[0] - top[0], point[1] - top[1]
        a = max(delta, key=abs)

        direction: ParabolaDirection
        if a > 0:
            if delta.index(a) == 0:
                direction = 'right'
            elif delta.index(a) == 1:
                direction = 'up'
        elif delta.index(a) == 0:
            direction = 'left'
        elif delta.index(a) == 1:
            direction = 'down'
        
        return ParabolaTool(top, abs(a), config.default_color, direction)

