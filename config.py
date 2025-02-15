from src.view.abc.window import Command, CheckButton
from src.abc.color import Color

main_pack_args = {
    'fill': 'x'
}

canvas_args = {
    'bg': 'white',
}

info_label_args = {
    'background': 'light goldenrod',
    'height': 0,   
}

button_args = {
    'text': 'Next'
}

info_pack_args = {
    'side': 'right',
}

main_menu_struct = {
    'File': {},
    'Edit': {},
    'View': {},
    'Insert': {
        'Line': {
            'DDA': Command(),
            'Bresenham': Command(),
            'Wu': Command()
        },
    },
    'Debug':{
        'Debug mode': CheckButton(),
    },
}


main_title = "main menu"
start_info_str = 'Information'
debug_info = 'Press Next button.'

standart_color = Color.from_hex('#fff000')

cell_size = 20
canvas_size = (30, 40)

debug_step = 1
