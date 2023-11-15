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


toggle = ui.toggle(["Light", "Dark"], value=d, on_change=toggle_theme)

with aui.breadcrumbs():
    with aui.breadcrumbs():
        aui.breadcrumbs_el("Home", icon="home", on_click=lambda: print("'Home' Clicked"))
        aui.breadcrumbs_el("System", icon="windows", on_click=lambda: print("'Windows' Clicked"))
        aui.breadcrumbs_el("Apps", icon="app", on_click=lambda: print("'Apps' Clicked"))

ui.run(native=True, dark=isDark())
