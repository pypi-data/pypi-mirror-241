from nicegui import element


class ButtonGroup(element.Element):
    def __init__(self) -> None:
        """ButtonGroup 按钮组

        这个组件是基于 Quasar 的 `QBar <http://www.quasarchs.com/vue-components/button-group>`_ 组件.
        """
        super().__init__('q-button-group')
        self._classes.append('nicegui-button-group')


