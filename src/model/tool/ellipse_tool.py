from ..color import Color
from ..abc.tool import Tool
from ..drawer.ellipse_drawer import EllipseDrawer


class EllipseTool(Tool):
    def __init__(
        self,
        upper_left_corner: tuple[int, int],
        lower_right_corner: tuple[int, int],
        color: Color
    ):
        super().__init__()
        delta = lower_right_corner[0] - upper_left_corner[0], lower_right_corner[1] - upper_left_corner[1]
        self.radius = int(delta[0] / 2 + .5), int(delta[1] / 2 + .5) 
        self.center = upper_left_corner[0] + self.radius[0], upper_left_corner[1] + self.radius[1]        
        self.color = color

    def create(self):
        return EllipseDrawer(*self.center, *self.radius, self.color)
