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

    def click():
        ui.notify("Clicked")

    aui.breadcrumbs_el("C", "home")
    aui.breadcrumbs_el("Windows", on_click=click)
    aui.breadcrumbs_el("System32")
    aui.breadcrumbs_el("Boot")

ui.run(native=True, dark=isDark())
