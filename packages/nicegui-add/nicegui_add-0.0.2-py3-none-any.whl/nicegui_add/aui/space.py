from nicegui import element


class Space(element.Element):
    def __init__(self) -> None:
        """Space 工具栏

        这个组件是基于 Quasar 的 `Space <http://www.quasarchs.com/vue-components/space>`_ 组件.

        :param inset: 将插入应用于内容（对后续工具栏有用）
        """
        super().__init__('q-space')
        self._classes.append('nicegui-spcae')
