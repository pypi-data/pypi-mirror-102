from enum import Enum

import PySimpleGUI as sg  # type: ignore


class Key(Enum):
    NewWindow = 'New Window     Ctrl+N'
    CloseWindow = 'Close Window   Ctrl+W'
    Quit = 'Quit           Ctrl+Q'
    Copy = 'Copy    Ctrl+C'
    Paste = 'Paste   Ctrl+V'
    Suttas = 'Suttas        F5'
    Dictionary = 'Dictionary    F6'
    SortCount = 'Sort, Count   F7'
    Inflections = 'Inflections   F8'
    DocViewer = 'Doc Viewer    F9'
    ThemeLight = 'Light::set-light-theme'
    ThemeDark = 'Dark::set-dark-theme'
    About = 'About...'


menu_def = [['&File', ['&'+Key.NewWindow.value,
                       '&'+Key.CloseWindow.value,
                       '&'+Key.Quit.value]],
            ['&Edit', ['&'+Key.Copy.value,
                       '&'+Key.Paste.value]],
            ['&Windows', ['&'+Key.Suttas.value,
                          '&'+Key.Dictionary.value,
                          # '&'+Key.SortCount.value,
                          # '&'+Key.Inflections.value,
                          '&'+Key.DocViewer.value,
                          ]],
            ['&Themes', ['&'+Key.ThemeLight.value,
                         '&'+Key.ThemeDark.value]],
            ['&Help',
             '&'+Key.About.value]]

# NOTE: Don't bind Control+c and Control-v to Copy and Paste. The OS will
# handle those key bindings. It is enough to handle the menu event.

MENU_HOTKEYS = [
    {'key': '<Control-n>', 'event': Key.NewWindow.value},
    {'key': '<Control-w>', 'event': Key.CloseWindow.value},
    {'key': '<Control-q>', 'event': Key.Quit.value},
    {'key': '<F5>', 'event': Key.Suttas.value},
    {'key': '<F6>', 'event': Key.Dictionary.value},
    # {'key': '<F7>', 'event': Key.SortCount.value},
    # {'key': '<F8>', 'event': Key.Inflections.value},
    {'key': '<F9>', 'event': Key.DocViewer.value},
]

GLOBAL_EVENTS = list(map(lambda hk: hk['event'], MENU_HOTKEYS))
GLOBAL_EVENTS.append(Key.Copy.value)
GLOBAL_EVENTS.append(Key.Paste.value)
GLOBAL_EVENTS.append(Key.About.value)
GLOBAL_EVENTS.append(Key.ThemeLight.value)
GLOBAL_EVENTS.append(Key.ThemeDark.value)


def bind_menu_hotkeys(window: sg.Window):
    for hk in MENU_HOTKEYS:
        window.bind(hk['key'], hk['event'])


def component_layout():
    return [sg.Menu(menu_def, tearoff=False, pad=(200, 1))]
