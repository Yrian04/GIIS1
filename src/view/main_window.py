from dataclasses import dataclass

import tkinter as tk

import config
from .abc.main_view import MainView
from .abc.window import Window


GRID = 'grid'


@dataclass(frozen=True)
class MainWindowTags:
    NEXT_STEP_BUTTON_CLICK = 'next-step-button-click'


class MainWindow(Window, MainView):
    def __init__(self):
        Window.__init__(self)
        MainView.__init__(self)
        self.title(config.main_title)
        self.menu = self._build_menu()
        self.config(menu=self.menu)

        self.canvas = tk.Canvas(**config.canvas_args)
        self.canvas.pack(**config.main_pack_args)

        self._build_info_frame().pack(**config.main_pack_args)
        self.next_step_button.config(state='disabled')
    
    def set_size(self, height, width):
        self.canvas.config(
            height=height*config.cell_size,
            width=width*config.cell_size
        )

    def set_cell(self, x, y, color):
        x *= config.cell_size
        y *= config.cell_size
        self.canvas.create_rectangle(
            x, 
            y, 
            x + config.cell_size,
            y + config.cell_size,
            fill=str(color),
            width=0,
        )

    def on_change_debug_mode(self, mode):
        if mode:
            self.next_step_button['state'] = 'normal'
            self._draw_grid()
        else:
            self.next_step_button['state'] = 'disabled'
            self.canvas.delete(GRID)

    def debug_wait(self):
        wait_var = tk.IntVar(self, 0)
        def button_handler():
            nonlocal wait_var
            wait_var.set(1)

        self.next_step_button.config(command=button_handler)
        self.wait_variable(wait_var)
        return True

    def show_info(self, messange):
        self.info_str.set(messange)
    
    def _draw_grid(self):
        x_start = 0
        y_start = 0
        x_end = config.cell_size * config.canvas_size[1]
        y_end = config.cell_size * config.canvas_size[0]

        for x in range(x_start, x_end + 1, config.cell_size):
            self.canvas.create_line(x, y_start, x, y_end, tags=GRID)

        for y in range(y_start, y_end + 1, config.cell_size):
            self.canvas.create_line(x_start, y, x_end, y, tags=GRID)

    def _build_info_frame(self) -> tk.Frame:
        info_frame = tk.Frame(self)
        
        self.add_tag(MainWindowTags.NEXT_STEP_BUTTON_CLICK)
        self.next_step_button = tk.Button(**config.button_args)
        self.next_step_button.pack(**config.info_pack_args)

        self.info_str = tk.StringVar(info_frame, config.start_info_str)
        self.info_label = tk.Label(self, **config.info_label_args, textvariable=self.info_str)
        self.info_label.pack(**config.info_pack_args)

        return info_frame
