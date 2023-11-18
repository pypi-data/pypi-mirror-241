from nicegui import ui, run
from nicegui_add import aui
from darkdetect import isDark
from sys import exit

if isDark():
    d = "Dark"
else:
    d = "Light"


def toggle_theme():
    if toggle.value == "Dark":
        d = True
    else:
        d = False
    ui.dark_mode(d)


toggle = ui.toggle(["Light", "Dark"], value=d, on_change=toggle_theme)

with aui.intersection().props('transition="scale"'):
    for i in range(10):
        with ui.card():
            ui.avatar(icon="X")


ui.run(native=True, dark=isDark())
