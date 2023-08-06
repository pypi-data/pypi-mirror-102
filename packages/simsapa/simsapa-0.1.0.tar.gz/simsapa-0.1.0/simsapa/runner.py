from pathlib import Path

import PySimpleGUI as sg  # type: ignore

from .app.types import AppData  # type: ignore
from .app.types import WindowEvents as WE  # type: ignore
from .app.themes import load_themes  # type: ignore

from .layouts.top_menu import Key as MenuKey  # type: ignore
from .layouts.sidebar import Key as SidebarKey  # type: ignore

from .layouts.sutta_search import SuttaSearchWindow  # type: ignore
from .layouts.dictionary_search import DictionarySearchWindow  # type: ignore
from .layouts.doc_viewer import DocViewerWindow  # type: ignore


def main():
    load_themes()
    sg.theme('SolarizedLight')

    paths = [
        Path.cwd().joinpath("appdata.sqlite3"),
        Path.home().joinpath(".config/simsapa/assets/appdata.sqlite3"),
    ]

    db_path = None

    for p in paths:
        if p.is_file():
            db_path = p

    if db_path is None:
        print("ERROR: Cannot find appdata.sqlite3")
        exit(1)

    app_data = AppData(db_path)

    app_windows = [SuttaSearchWindow(app_data)]

    for w in app_windows:
        w.create_window()

    running = True
    while running:
        for w in app_windows:
            (event, values) = w.handle_events()

            if event in [sg.WINDOW_CLOSED, MenuKey.CloseWindow.value]:
                w.close_window()
                app_windows.remove(w)
                if len(app_windows) == 0:
                    running = False
                continue

            if event is WE.NoOp:
                continue

            if event == MenuKey.Quit.value:
                running = False
                continue

            if event == MenuKey.NewWindow.value:
                new_w = SuttaSearchWindow(app_data)
                new_w.create_window()
                app_windows.append(new_w)

            if event in [MenuKey.Suttas.value, SidebarKey.Suttas]:
                new_w = SuttaSearchWindow(app_data)
                new_w.create_window()
                app_windows.append(new_w)

            if event in [MenuKey.Dictionary.value, SidebarKey.Dictionary]:
                new_w = DictionarySearchWindow(app_data)
                new_w.create_window()
                app_windows.append(new_w)

            if event == MenuKey.DocViewer.value:
                new_w = DocViewerWindow(app_data)
                new_w.create_window()
                app_windows.append(new_w)

            if event == MenuKey.About.value:
                w.window.disappear()
                sg.popup('Simsapa Dhamma Reader', 'Version 0.1.0',
                         'PySimpleGUI Version', sg.version,  grab_anywhere=True)
                w.window.reappear()

            if event in [MenuKey.ThemeLight.value, MenuKey.ThemeDark.value]:
                if event == MenuKey.ThemeLight.value:
                    app_data.theme = 'SolarizedLight'
                else:
                    app_data.theme = 'SolarizedDark'

                w.close_window()
                w.create_window()

            if event == MenuKey.Copy.value:
                text = w.copy()
                if text is not None:
                    w.window.TKroot.clipboard_clear()
                    w.window.TKroot.clipboard_append(text)

            if event == MenuKey.Paste.value:
                try:
                    text = w.window.TKroot.clipboard_get()
                except Exception:
                    text = None

                if text is not None:
                    w.paste(text)

            # sg.Print(event, values)

    for w in app_windows:
        w.close_window()
