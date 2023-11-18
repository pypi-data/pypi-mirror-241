from nicegui import element


class Bar(element.Element):
    def __init__(self, inset: bool = None) -> None:
        """ToolBar 工具栏

        这个组件是基于 Quasar 的 `QBar <http://www.quasarchs.com/vue-components/bar>`_ 组件.

        :param inset: 将插入应用于内容（对后续工具栏有用）
        """
        super().__init__('q-bar')
        self._classes.append('nicegui-bar')

        self._props["inset"] = inset

