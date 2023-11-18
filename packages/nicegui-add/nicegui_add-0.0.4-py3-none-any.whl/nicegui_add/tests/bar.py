from nicegui import ui, run, app
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


with aui.bar().style("width:100%") as bar:
    aui.space()
    ui.button(icon="close", on_click=lambda: app.native.main_window.destroy()).props("flat dense")

toggle = ui.toggle(["Light", "Dark"], value=d, on_change=toggle_theme)

ui.run(native=True, dark=isDark())
