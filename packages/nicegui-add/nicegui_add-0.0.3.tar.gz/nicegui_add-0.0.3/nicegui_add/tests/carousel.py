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

with aui.carousel() as carousel:
    carousel.props("""
        v-model="slide"
        transition-prev="scale"
        transition-next="scale"
        swipeable
        animated
        control-color="white"
        navigation
        padding
        arrows
        height="300px"
        class="bg-primary text-white shadow-1 rounded-borders"
    """)
    with aui.carousel_slide() as slide:
        slide.props('name="style"')
        slide.classes("column no-wrap flex-center")
        ui.icon(name="style", size="56px")

ui.run(native=True, dark=isDark())
