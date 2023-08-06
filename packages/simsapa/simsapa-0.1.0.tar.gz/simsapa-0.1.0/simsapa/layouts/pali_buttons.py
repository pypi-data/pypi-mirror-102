from enum import Enum, auto

import PySimpleGUI as sg  # type: ignore


def component_layout(input_key: str):
    def to_button(k):
        return sg.Button(
            button_text=k.value,
            key=k,
            metadata=k.value,
            size=(1, 1),
            auto_size_button=False,
            enable_events=True,
            button_color=(
                sg.theme_input_text_color(),
                sg.theme_input_background_color(),
            ),
        )

    lower_case_row = list(map(to_button, PaliLowerKey))
    upper_case_row = list(map(to_button, PaliUpperKey))

    return sg.Column(
        [lower_case_row,
         upper_case_row],
        vertical_alignment='top')


class PaliLowerKey(Enum):
    Letter_0 = "ā"
    Letter_1 = "ī"
    Letter_2 = "ū"
    Letter_3 = "ṃ"
    Letter_4 = "ṁ"
    Letter_5 = "ṅ"
    Letter_6 = "ñ"
    Letter_7 = "ṭ"
    Letter_8 = "ḍ"
    Letter_9 = "ṇ"
    Letter_10 = "ḷ"


class PaliUpperKey(Enum):
    Letter_0 = "Ā"
    Letter_1 = "Ī"
    Letter_2 = "Ū"
    Letter_3 = "Ṃ"
    Letter_4 = "Ṁ"
    Letter_5 = "Ṅ"
    Letter_6 = "Ñ"
    Letter_7 = "Ṭ"
    Letter_8 = "Ḍ"
    Letter_9 = "Ṇ"
    Letter_10 = "Ḷ"
