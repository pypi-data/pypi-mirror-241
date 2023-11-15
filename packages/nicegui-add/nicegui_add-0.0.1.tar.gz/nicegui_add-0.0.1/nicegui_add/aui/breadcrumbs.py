from nicegui import element
from nicegui.elements.mixins.text_element import TextElement
from nicegui.events import handle_event, ClickEventArguments


class Breadcrumbs(element.Element):
    def __init__(self, separator: str = "/", gutter: str = "sm") -> None:
        super().__init__('q-breadcrumbs')
        self._classes.append('nicegui-breadcrumbs')

        self._props["separator"] = separator
        self._props["gutter"] = gutter


class BreadcrumbsEl(element.Element):
    def __init__(self,
                 label: str = None,
                 icon: str = None,
                 tag: str = None,
                 on_click=None
                 ) -> None:
        super().__init__(tag="q-breadcrumbs-el")
        self._classes.append('nicegui-breadcrumbs-el')
        if label:
            self._props["label"] = label
        if icon:
            self._props["icon"] = icon
        if tag:
            self._props["tag"] = tag
        if on_click:
            self.on('click', lambda _: handle_event(on_click, ClickEventArguments(sender=self, client=self.client)), [])
