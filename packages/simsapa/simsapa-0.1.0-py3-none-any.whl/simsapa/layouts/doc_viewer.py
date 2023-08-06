import tkinter as tk
from enum import Enum, auto
from typing import Optional

import fitz  # type: ignore
import PySimpleGUI as sg  # type: ignore
from PIL import Image, ImageTk  # type: ignore

from ..app.types import AppData  # type: ignore
from ..app.types import WindowInterface  # type: ignore
from ..app.types import WindowEvents as WE  # type: ignore
from .top_menu import GLOBAL_EVENTS, bind_menu_hotkeys  # type: ignore
from .top_menu import component_layout as top_menu_comp  # type: ignore


class DocViewerWindow(WindowInterface):
    def __init__(self, app_data: AppData):
        self.app_data: AppData = app_data
        self.window: Optional[sg.Window] = None

        self.file_path = ""
        self.doc = None
        self.page_count = 0
        self.dlist_tab = None
        self.title = ""

        root = tk.Tk()
        self.max_width = root.winfo_screenwidth() - 20
        self.max_height = root.winfo_screenheight() - 135
        self.max_size = (self.max_width, self.max_height)

        root.destroy()
        del root

        self.cur_page = 0
        self.data = None
        self.clip_pos = None

        # now define the buttons / events we want to handle
        self.enter_buttons = [chr(13), "Return:13"]
        self.quit_buttons = ["Escape:27", chr(27)]
        self.next_buttons = ["Next", "Next:34", "MouseWheel:Down"]
        self.prev_buttons = ["Prev", "Prior:33", "MouseWheel:Up"]
        self.Up = "Up:38"
        self.Left = "Left:37"
        self.Right = "Right:39"
        self.Down = "Down:40"
        self.zoom_buttons = ["Zoom", self.Up, self.Down, self.Left, self.Right]

        # all the buttons we will handle
        self.my_keys = self.enter_buttons + self.next_buttons + self.prev_buttons + self.zoom_buttons

        # old page store and zoom toggle
        self.old_page = 0
        self.old_zoom = False

        self.zoom_pressed = False
        self.zoom = False


    def create_window(self):
        if self.window is not None:
            return

        sg.theme(self.app_data.theme)

        self.window = sg.Window('Simsapa - Doc Viewer',
                                self.window_layout(),
                                finalize=True,
                                resizable=True,
                                default_element_size=(30, 1),
                                default_button_element_size=(12, 1),
                                return_keyboard_events=True)
        bind_menu_hotkeys(self.window)

    def window_layout(self):
        layout = [
            top_menu_comp(),
            [sg.Column(layout=self.component_layout(),
                       key=Key.WindowMain,
                       vertical_alignment='top',
                       expand_x=False,
                       expand_y=True)]
        ]
        return layout

    def component_layout(self):
        layout = [
            [sg.Text('Doc Viewer', font=self.app_data.body_font_large)],
            [sg.Button('Open...', key=Key.OpenFile, font=self.app_data.body_font_normalsize)],
            [
                sg.ReadButton('Next'),
                sg.ReadButton('Prev'),
                sg.Text('Page:'),
                sg.InputText(str(self.cur_page + 1), size=(5, 1), key="-PageNumber-"),
                sg.Text('(%i)' % self.page_count),
                sg.ReadButton('Zoom'),
                sg.Text('(toggle on/off, use arrows to navigate while zooming)'),
            ],
            [sg.Image(data=self.data, key="-ImageElem-")],
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

        if event is Key.OpenFile:
            self.open_file()

        if self.doc is not None:
            if event in self.enter_buttons:
                try:
                    self.cur_page = int(values['-PageNumber-']) - 1  # check if valid
                    while self.cur_page < 0:
                        self.cur_page += self.page_count
                except Exception:
                    self.cur_page = 0  # this guy's trying to fool me

            if event in self.next_buttons:
                self.cur_page += 1

            if event in self.prev_buttons:
                self.cur_page -= 1

            if event == self.Up:
                self.zoom = (self.clip_pos, 0, -1)

            if event == self.Down:
                self.zoom = (self.clip_pos, 0, 1)

            if event == self.Left:
                self.zoom = (self.clip_pos, -1, 0)

            if event == self.Right:
                self.zoom = (self.clip_pos, 1, 0)

            if event == "Zoom":
                self.zoom_pressed = True
                self.zoom = (self.clip_pos, 0, 0)

            # sanitize page number
            if self.cur_page >= self.page_count:  # wrap around
                self.cur_page = 0

            while self.cur_page < 0:  # pages > 0 look nicer
                self.cur_page += self.page_count

            if self.zoom_pressed and self.old_zoom:
                self.zoom = self.zoom_pressed = self.old_zoom = False

            self.data, self.clip_pos = self.get_page(self.cur_page, zoom=self.zoom, max_size=self.max_size, first=False)

            self.window["-ImageElem-"].update(data=self.data)
            self.old_page = self.cur_page
            self.old_zoom = self.zoom_pressed or self.zoom

            # update page number field
            if event in self.my_keys:
                self.window["-PageNumber-"].update(str(self.cur_page + 1))

        return (WE.NoOp, None)

    def close_window(self):
        if self.window is not None:
            self.window.close()
            self.window = None

    def copy(self) -> Optional[str]:
        return None

    def paste(self, text: str):
        return None

    def open_file(self):
        self.file_path = sg.popup_get_file(
            'Document Browser', 'Document file to open',
            # no_window=True,
            file_types=(
                ("PDF Files", "*.pdf"),
                ("Epub Files", "*.epub"),
                ("HTML", "*.htm*"),
            )
        )
        if self.file_path != "":
            self.doc = fitz.open(self.file_path)
            self.page_count = len(self.doc)

            # allocate storage for page display lists
            self.dlist_tab = [None] * self.page_count

            self.title = "PyMuPDF display of '%s', pages: %i" % (self.file_path, self.page_count)

            self.data, self.clip_pos = self.get_page(self.cur_page, zoom=False, max_size=self.max_size, first=True)

    def get_page(self, pno, zoom=False, max_size=None, first=False):
        """Return a PNG image for a document page number.
        """
        dlist = self.dlist_tab[pno]  # get display list of page number
        if not dlist:                # create if not yet there
            self.dlist_tab[pno] = self.doc[pno].getDisplayList()
            dlist = self.dlist_tab[pno]
        r = dlist.rect  # the page rectangle
        clip = r
        # ensure image fits screen:
        # exploit, but do not exceed width or height
        zoom_0 = 1
        if max_size:
            zoom_0 = min(1, max_size[0] / r.width, max_size[1] / r.height)
            if zoom_0 == 1:
                zoom_0 = min(max_size[0] / r.width, max_size[1] / r.height)
        mat_0 = fitz.Matrix(zoom_0, zoom_0)

        if not zoom:             # show total page
            pix = dlist.getPixmap(matrix=mat_0, alpha=False)
        else:
            # mp = r.tl + (r.br - r.tl) * 0.5     # page rect center
            w2 = r.width / 2
            h2 = r.height / 2
            clip = r * 0.5
            tl = zoom[0]          # old top-left
            tl.x += zoom[1] * (w2 / 2)
            tl.x = max(0, tl.x)
            tl.x = min(w2, tl.x)
            tl.y += zoom[2] * (h2 / 2)
            tl.y = max(0, tl.y)
            tl.y = min(h2, tl.y)
            clip = fitz.Rect(tl, tl.x + w2, tl.y + h2)

            mat = mat_0 * fitz.Matrix(2, 2)      # zoom matrix
            pix = dlist.getPixmap(alpha=False, matrix=mat, clip=clip)

        if first:                     # first call: tkinter still inactive
            img = pix.getPNGData()    # so use fitz png output
        else:                         # else take tk photo image
            pilimg = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img = ImageTk.PhotoImage(pilimg)

        return img, clip.tl           # return image, clip position


class Key(Enum):
    NoEvents = auto()
    WindowMain = auto()
    OpenFile = auto()
