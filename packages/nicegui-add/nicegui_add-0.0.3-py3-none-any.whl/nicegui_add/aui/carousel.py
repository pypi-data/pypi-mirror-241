from nicegui import element
from nicegui.elements.mixins.text_element import TextElement


class Carousel(element.Element):
    def __init__(self) -> None:
        """Carousel 转盘

        这个组件是基于 Quasar 的 `QCarousel <http://www.quasarchs.com/vue-components/carousel>`_ 组件.
        """
        super().__init__('q-carousel')
        self._classes.append('nicegui-carousel')


class CarouselSlide(element.Element):
    def __init__(self, text: str = "", shrink: bool = None) -> None:
        """CarouselSlide 工具栏标题（建议配合ToolBar使用）

        这个组件是基于 Quasar 的 `QCarouselSlide <http://www.quasarchs.com/vue-components/carousel>`_ 组件.

        """
        super().__init__(tag="q-carousel-slide")
        self._classes.append('nicegui-carousel-slide')
