from nicegui import element
from nicegui.elements.mixins.text_element import TextElement


class ToolBar(element.Element):
    def __init__(self, inset: bool = None) -> None:
        """ToolBar 工具栏

        这个组件是基于 Quasar 的 `QToolBar <http://www.quasarchs.com/vue-components/toolbar>`_ 组件.

        :param inset: 将插入应用于内容（对后续工具栏有用）
        """
        super().__init__('q-toolbar')
        self._classes.append('nicegui-toolbar')

        self._props["inset"] = inset


class ToolBarTitle(TextElement):
    def __init__(self, text: str = "", shrink: bool = None) -> None:
        """ToolBarTitle 工具栏标题（建议配合ToolBar使用）

        这个组件是基于 Quasar 的 `QToolbarTitle <http://www.quasarchs.com/vue-components/toolbar>`_ 组件.

        :param text: 标题文本
        :param shrink: 默认该组件会铺满可用空间，可以用这个关闭
        """
        super().__init__(tag="q-toolbar-title", text=text)
        self._props["shrink"] = shrink
