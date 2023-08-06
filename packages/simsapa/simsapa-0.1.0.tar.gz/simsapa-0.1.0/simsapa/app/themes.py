import PySimpleGUI as sg  # type: ignore

# SOLARIZED HEX
# --------- -------
# base03    #002b36
# base02    #073642
# base01    #586e75
# base00    #657b83
# base0     #839496
# base1     #93a1a1
# base2     #eee8d5
# base3     #fdf6e3
# yellow    #b58900
# orange    #cb4b16
# red       #dc322f
# magenta   #d33682
# violet    #6c71c4
# blue      #268bd2
# cyan      #2aa198
# green     #859900


SolarizedDark = {
    "BACKGROUND": "#002b36",
    "TEXT": "#fafafa",
    "INPUT": "#586e75",
    "TEXT_INPUT": "#ffffff",
    "SCROLL": "#073642",
    "BUTTON": ("#eee8d5", "#268bd2"),
    "PROGRESS": ("#268bd2", "#eee8d5"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}

SolarizedLight = {
    "BACKGROUND": "#fdf6e3",
    "TEXT": "#0a0a0a",
    "INPUT": "#D6DBDB",
    "TEXT_INPUT": "#0a0a0a",
    "SCROLL": "#eee8d5",
    "BUTTON": ("#fafafa", "#b58900"),
    "PROGRESS": ("#2aa198", "#eee8d5"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}


def load_themes():
    sg.theme_add_new("SolarizedDark", SolarizedDark)
    sg.theme_add_new("SolarizedLight", SolarizedLight)
