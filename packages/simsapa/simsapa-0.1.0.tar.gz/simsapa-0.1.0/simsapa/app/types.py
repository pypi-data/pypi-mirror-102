import os.path
from enum import Enum
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from typing import Any, Dict, Optional, Tuple


class AppData:
    def __init__(self, db_path: str):
        db_conn = None
        if os.path.isfile(db_path):
            try:
                engine = create_engine(f"sqlite+pysqlite:///{db_path}", echo=False, future=True)
                db_conn = engine.connect()
                Session = sessionmaker(engine)
                Session.configure(bind=engine)
                db_session = Session()
            except Exception as e:
                print(e)
                exit(1)
        else:
            print(f"ERROR: Can't connect to database: {db_path}")
            exit(1)

        self.db_conn = db_conn
        self.db_session = db_session
        self.body_font_normalsize = ('Helvetica', 13)
        self.body_font_large = ('Helvetica', 18)
        self.body_font_smaller = ('Helvetica', 11)
        self.theme = 'SolarizedLight'
        self.body_light_css = 'body { color: #0a0a0a; background-color: #FBECC3; }'
        self.body_dark_css = 'body { color: #fafafa; background-color: #001A21; }'

    def is_dark_theme(self) -> bool:
        return self.theme == 'SolarizedDark'

    def is_light_theme(self) -> bool:
        return not self.is_dark_theme()

    def theme_css(self):
        if self.is_light_theme():
            return self.body_light_css
        else:
            return self.body_dark_css


class WindowInterface:
    def create_window(self) -> None:
        pass

    def handle_events(self) -> Tuple[Optional[Any], Optional[Dict[Any, Any]]]:
        pass

    def close_window(self) -> None:
        pass

    def copy(self) -> Optional[str]:
        pass

    def paste(self, text: str) -> None:
        pass


class WindowEvents(Enum):
    NoOp = 1


class DictWord:
    def __init__(self, word: str):
        self.word = word
        self.definition_md = ''


class Sutta:
    def __init__(self, uid: str, title: str, content_html: str):
        self.uid = uid
        self.title = title
        self.content_html = content_html
