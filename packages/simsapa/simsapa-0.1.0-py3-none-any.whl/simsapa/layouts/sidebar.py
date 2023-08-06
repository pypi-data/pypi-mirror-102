from enum import Enum, auto

import PySimpleGUI as sg  # type: ignore

from ..app.icons import icon  # type: ignore
from .top_menu import GLOBAL_EVENTS  # type: ignore


class Key(Enum):
    Suttas = auto()
    Dictionary = auto()


GLOBAL_EVENTS.append(Key.Suttas)
GLOBAL_EVENTS.append(Key.Dictionary)


def component_layout():
    return sg.Column(
        [[sg.Button(tooltip='Open a Sutta window',
                    image_data=icon('bxs_book_bookmark', 24),
                    image_size=(24, 24),
                    enable_events=True,
                    key=Key.Suttas)],
         [sg.Button(tooltip='Open a Dictionary window',
                    image_data=icon('bxs_book_content', 24),
                    image_size=(24, 24),
                    enable_events=True,
                    key=Key.Dictionary)],
         ],
        vertical_alignment='top',
        expand_y=True)
