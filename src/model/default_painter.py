from .abc.painter import Painter


class DefaultPainter(Painter):
    def draw(self, drawer, canvas):
        while drawer.draw(canvas):
            pass


