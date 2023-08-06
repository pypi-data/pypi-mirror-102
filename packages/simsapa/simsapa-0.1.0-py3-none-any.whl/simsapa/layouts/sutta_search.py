from typing import List, Optional
from enum import Enum, auto

import PySimpleGUI as sg  # type: ignore
from tkinterweb import HtmlFrame  # type: ignore

from ..app.types import WindowInterface  # type: ignore
from ..app.types import AppData, Sutta  # type: ignore
from ..app.types import WindowEvents as WE  # type: ignore
from ..app.db_models import RootText as DbSutta  # type: ignore
from ..app.icons import icon  # type: ignore
from .top_menu import GLOBAL_EVENTS, bind_menu_hotkeys  # type: ignore
from .top_menu import component_layout as top_menu_comp  # type: ignore
from .sidebar import component_layout as sidebar_comp  # type: ignore
from .pali_buttons import component_layout as pali_comp  # type: ignore
from .pali_buttons import PaliLowerKey, PaliUpperKey


class SuttaSearchWindow(WindowInterface):
    def __init__(self, app_data: AppData) -> None:
        self.app_data: AppData = app_data
        self.window: Optional[sg.Window] = None
        self.sutta_results: List[Sutta] = []
        self.sutta_history: List[Sutta] = []
        self.html_frame: Optional[HtmlFrame] = None

    def create_window(self):
        if self.window is not None:
            return

        sg.theme(self.app_data.theme)

        self.window = sg.Window('Simsapa - Sutta Search',
                                self.window_layout(),
                                finalize=True,
                                resizable=True,
                                default_element_size=(30, 1),
                                default_button_element_size=(12, 1))
        bind_menu_hotkeys(self.window)

        if self.html_frame is None:
            self.html_frame = HtmlFrame(self.window[Key.HtmlFrame].Widget,
                                        vertical_scrollbar=True,
                                        messages_enabled=False)
            self.html_frame.load_html('<body></body>')
            self.html_frame.add_css(self.app_data.theme_css())
            self.html_frame.pack(fill="both", expand=True)

    def window_layout(self):
        layout = [
            top_menu_comp(),
            [sidebar_comp(),
             sg.Column(layout=self.component_layout(),
                       key=Key.WindowMain,
                       vertical_alignment='top',
                       expand_x=False,
                       expand_y=True)]
        ]
        return layout

    def component_layout(self):
        layout = [
            [sg.Text('Suttas', font=self.app_data.body_font_large)],
            [sg.Image(data=icon('bx_search_alt_2', 24, invert=self.app_data.is_dark_theme()), size=(24, 24)),
             sg.Input(key=Key.Query,
                      size=(40, 1),
                      focus=True,
                      enable_events=True,
                      font=self.app_data.body_font_normalsize),
             pali_comp(Key.Query)],

            [sg.Column(
                [[sg.Text('', key=Key.Title, size=(30, 1), auto_size_text=True,
                          font=self.app_data.body_font_large)],
                 [sg.Text('', key=Key.Refcode, size=(20, 1), auto_size_text=True,
                          font=self.app_data.body_font_normalsize)],
                 ],
                vertical_alignment='top',
                expand_x=True)],

            [sg.Column(
                [[sg.Column(layout=[],
                            key=Key.HtmlFrame,
                            vertical_alignment='top',
                            expand_x=True,
                            expand_y=True)],
                 ],
                vertical_alignment='top',
                expand_x=True,
                expand_y=True),

             sg.Column(
                 [[sg.Text('Results')],
                  [sg.Listbox(
                      [],
                      key=Key.Results,
                      size=(30, 20),
                      enable_events=True,
                      select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                      font=self.app_data.body_font_smaller)
                   ],

                  [sg.Text('History')],
                  [sg.Listbox(
                      [],
                      key=Key.History,
                      size=(30, 20),
                      enable_events=True,
                      select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                      font=self.app_data.body_font_smaller)
                   ]
                  ],
                 vertical_alignment='top',
                 expand_x=True,
                 expand_y=True)],
        ]

        return layout

    def handle_events(self):
        if self.window is None:
            return

        event, values = self.window.read(timeout=100, timeout_key=Key.NoEvents)

        if event is sg.WINDOW_CLOSED or event in GLOBAL_EVENTS:
            return (event, values)

        if event is Key.NoEvents:
            return (WE.NoOp, None)

        if event is Key.Query and len(values[Key.Query]) > 3:
            self.handle_query(values[Key.Query])

        if type(event) is PaliLowerKey or type(event) is PaliUpperKey:
            self.window[Key.Query].Widget.insert('insert', self.window[event].metadata)
            query = self.window[Key.Query].Widget.get()
            if len(query) > 3:
                self.handle_query(query)

        if event is Key.Results and len(values[Key.Results]):
            (idx,) = self.window[Key.Results].Widget.curselection()
            sutta = self.sutta_results[idx]
            self.show_sutta(sutta)

            self.sutta_history.append(sutta)
            titles = list(map(lambda s: s.title, self.sutta_history))
            self.window[Key.History].update(titles)

        if event is Key.History and len(values[Key.History]):
            (idx,) = self.window[Key.History].Widget.curselection()
            self.show_sutta(self.sutta_history[idx])

        return (WE.NoOp, None)

    def close_window(self):
        if self.window is not None:
            self.window.close()
            self.window = None
            self.html_frame = None

    def copy(self) -> Optional[str]:
        if self.window is None:
            return None

        try:
            text = self.window[Key.Query].Widget.selection_get()
        except Exception:
            text = None

        return text

    def paste(self, text: str):
        if self.window is None or text == "":
            return

        self.window[Key.Query].Widget.insert('insert', text)
        query = self.window[Key.Query].Widget.get()
        if len(query) > 3:
            self.handle_query(query)

    def handle_query(self, query: str):
        self.sutta_results = self.sutta_search_query(query)
        titles = list(map(lambda s: s.title, self.sutta_results))
        if self.window is not None:
            self.window[Key.Results].update(titles)

    def show_sutta(self, sutta: Sutta):
        if self.window is None:
            return

        self.window[Key.Title].update(sutta.title)
        self.window[Key.Refcode].update(sutta.uid)

        if self.html_frame is not None:
            html = f"<body>{sutta.content_html}</body>"
            self.html_frame.load_html(html)
            self.html_frame.add_css(self.app_data.theme_css())

    def sutta_search_query(self, query):
        results = self.app_data.db_session \
                               .query(DbSutta) \
                               .filter(DbSutta.content_html.like(f"%{query}%")) \
                               .all()
        return results


class Key(Enum):
    NoEvents = auto()
    WindowMain = auto()
    HtmlFrame = auto()
    Query = auto()
    Results = auto()
    History = auto()
    Title = auto()
    Refcode = auto()
