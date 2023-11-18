from nicegui import ui
from nicegui_add import aui
from darkdetect import isDark

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


with aui.toolbar().props('class=""'):
    ui.button(icon="menu").props('flat round')
    aui.toolbar_title("ToolBarTitle")
    toggle = ui.toggle(["Light", "Dark"], value=d, on_change=toggle_theme)

ui.run(native=True, dark=isDark())
