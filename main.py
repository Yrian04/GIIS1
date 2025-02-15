from src.presenter.main_presenter import MainPresenter
from src.model.canvas import Canvas
from src.view.main_window import MainWindow
import config

window = MainWindow()
canvas = Canvas(config.canvas_size)
presenter = MainPresenter(canvas, window)
window.set_size(*config.canvas_size)
window.mainloop()
