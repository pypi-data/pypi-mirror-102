from typing import List, Optional
from enum import Enum, auto

import PySimpleGUI as sg  # type: ignore
from tkinterweb import HtmlFrame  # type: ignore
from markdown import markdown
from sqlalchemy.orm import joinedload  # type: ignore

from ..app.types import AppData, DictWord  # type: ignore
from ..app.types import WindowEvents as WE  # type: ignore
from ..app.types import WindowInterface  # type: ignore
from ..app.db_models import DictWord as DbDictWord  # type: ignore
from ..app.icons import icon  # type: ignore
from .top_menu import GLOBAL_EVENTS, bind_menu_hotkeys  # type: ignore
from .top_menu import component_layout as top_menu_comp  # type: ignore
from .sidebar import component_layout as sidebar_comp  # type: ignore
from .pali_buttons import component_layout as pali_comp  # type: ignore
from .pali_buttons import PaliLowerKey, PaliUpperKey


class DictionarySearchWindow(WindowInterface):
    def __init__(self, app_data: AppData):
        self.app_data: AppData = app_data
        self.window: Optional[sg.Window] = None
        self.word_results: List[DictWord] = []
        self.word_history: List[DictWord] = []
        self.html_frame: Optional[HtmlFrame] = None
        self.show_inflections = False
        self.current_word: Optional[DictWord] = None

    def create_window(self):
        if self.window is not None:
            return

        sg.theme(self.app_data.theme)

        self.window = sg.Window('Simsapa - Dictionary Search',
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
            [sg.Text('Dictionary', font=self.app_data.body_font_large)],
            [sg.Image(data=icon('bx_search_alt_2', 24, invert=self.app_data.is_dark_theme()), size=(24, 24)),
             sg.Input(key=Key.Query,
                      size=(40, 1),
                      focus=True,
                      enable_events=True,
                      font=self.app_data.body_font_normalsize),
             pali_comp(Key.Query)],

            [sg.Column(
                [[sg.Text('', key=Key.Word,
                          size=(53, 1), auto_size_text=True,
                          font=self.app_data.body_font_large),
                  sg.Checkbox('Inflections', key=Key.Inflections,
                              default=False, enable_events=True,
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
            query = values[Key.Query] + self.window[event].metadata
            self.window[Key.Query].update(query)
            if len(query) > 3:
                self.handle_query(query)

        if event is Key.Results and len(values[Key.Results]):
            (idx,) = self.window[Key.Results].Widget.curselection()
            self.current_word = self.word_results[idx]
            self.show_current_word()

            self.word_history.append(self.current_word)
            words = list(map(lambda s: s.word, self.word_history))
            self.window[Key.History].update(words)

        if event is Key.History and len(values[Key.History]):
            (idx,) = self.window[Key.History].Widget.curselection()
            self.current_word = self.word_history[idx]
            self.show_current_word()

        if event is Key.Inflections:
            self.show_inflections = values[Key.Inflections]
            self.show_current_word()

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
        self.word_results = self.word_search_query(query)
        words = list(map(lambda s: s.word, self.word_results))
        if self.window is not None:
            self.window[Key.Results].update(words)

    def show_current_word(self):
        if self.window is None or self.current_word is None:
            return

        self.window[Key.Word].update(self.current_word.word)

        inflections = """
<div class="pls-inflection-root">
  <header class="pls-inflection-header">
    <summary>
      <div class="pls-inflection-summary-word-info" style="font-weight: bold;">pāli 2 – "i fem" (like āpatti)</div>
      <div class="pls-inflection-summary-definition">
        <span class="pls-inflection-summary-definition-pos">(fem)</span>&nbsp;
        <span class="pls-inflection-summary-definition-meaning">
          the canon of the Buddhist writings or the language in which it is written
        </span>
      </div>
    </summary>
  </header>
<table class="pls-inflection-table pls-inflection-type-declension" style="border: 1px solid black;">
  <thead>
    <tr>
      <td><span class="pls-inflection-table-title">i fem</span></td>
      <td colspan="2"><span class="pls-inflection-col-header">fem</span></td>
      </tr>
    <tr>
      <td><span class="pls-inflection-row-header"></span></td>
      <td><span class="pls-inflection-col-header">sg</span></td>
      <td><span class="pls-inflection-col-header">pl</span></td>
      </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <span class="pls-inflection-row-header">nom</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāli</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyo</div>
        <div class="pls-inflection-inflected-word">pālī</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">acc</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliṃ</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyo</div>
        <div class="pls-inflection-inflected-word">pālī</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">instr</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyā</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pālibhi</div>
        <div class="pls-inflection-inflected-word">pālībhi</div>
        <div class="pls-inflection-inflected-word">pālīhi</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">dat</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyā</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pālīnaṃ</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">abl</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyā</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pālibhi</div>
        <div class="pls-inflection-inflected-word">pālībhi</div>
        <div class="pls-inflection-inflected-word">pālīhi</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">gen</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyā</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pālīnaṃ</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">loc</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyaṃ</div>
        <div class="pls-inflection-inflected-word">pāliyā</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pālisu</div>
        <div class="pls-inflection-inflected-word">pālīsu</div>
        </td>
      </tr>
    <tr>
      <td>
        <span class="pls-inflection-row-header">voc</span>
      </td>
      <td>
        <div class="pls-inflection-inflected-word">pāli</div>
        </td>
      <td>
        <div class="pls-inflection-inflected-word">pāliyo</div>
        <div class="pls-inflection-inflected-word">pālī</div>
        </td>
      </tr>
    <tr>
      <td><span class="pls-inflection-row-header">in comps</span></td>
      <td colspan="6">
        <div class="pls-inflection-inflected-word">pāli</div>
        </td>
    </tr>
  </tbody>
</table>
</div>"""

        if self.html_frame is not None:
            def md_to_html(meaning):
                return markdown(meaning.definition_md)

            content_html = "".join(list(map(md_to_html, self.current_word.meanings)))

            content_html += "<p></p>"

            if self.show_inflections:
                content_html += inflections

            html = f"<body>{content_html}</body>"
            self.html_frame.load_html(html)
            self.html_frame.add_css(self.app_data.theme_css())

    def word_search_query(self, query):
        results = self.app_data.db_session \
                               .query(DbDictWord) \
                               .options(joinedload(DbDictWord.meanings)) \
                               .filter(DbDictWord.word.like(f"%{query}%")) \
                               .all()
        return results


class Key(Enum):
    NoEvents = auto()
    WindowMain = auto()
    HtmlFrame = auto()
    Query = auto()
    Word = auto()
    Inflections = auto()
    Results = auto()
    History = auto()
