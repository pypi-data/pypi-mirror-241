from nicegui import element


class Intersection(element.Element):
    def __init__(self) -> None:
        """ToolBar 工具栏

        这个组件是基于 Intersection 的 `QIntersection <http://www.quasarchs.com/vue-components/intersection>`_ 组件.
        """
        super().__init__('q-intersection')
        self._classes.append('nicegui-intersection')

