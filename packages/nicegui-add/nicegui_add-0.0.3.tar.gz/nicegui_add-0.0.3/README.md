# NiceGUI 补充 / Adds
补充`NiceGUI`未实现的一些组件

在使用`NiceGUI`的过程中，我查阅了组件库文档和`quasarchs`文档，但突然发现有些组件竟然没有实现，如`BreadCrumbs`，感觉还是挺重要的，就专门创了一个项目

## 安装 / Installation

```bash
# nicegui>=1.4.0
pip install nicegui-add
```

## 构建 / Build
本库是使用`Poetry`构建，更多需查询官方文档

```bash
poetry build
poetry publish --build
```

## 文档构建 / Documents Build
文档是使用`Sphinx`构建
```bash
cd docs
python make.py
```

>`make.py`
>```python
>import os
>
>make = "make.bat "
>
>os.system(make + "clear")
>os.system(make + "html")
>```



## 组件 / Elements
### Breadcrumbs 面包屑
> 类似于文件管理器上的导航栏

#### 用法 / Usage
```python
aui.breadcrumbs(separator: str = ...)
```
* separator为每个元件`BreadcrumbsEl`之间的隔开符，默认是`/`


```python
aui.breadcrumbs_el(text: str = ..., icon: str = ..., on_click=...)
```
* `text`为显示文本
* `icon`为显示图标
* `on_click`为被点击时的事件

#### 例子 / Example
```python
from nicegui import ui
from nicegui_add import aui

with aui.breadcrumbs():
    aui.breadcrumbs_el("Home", icon="home", on_click=lambda: print("'Home' Clicked"))
    aui.breadcrumbs_el("System", icon="windows", on_click=lambda: print("'Windows' Clicked"))
    aui.breadcrumbs_el("Apps", icon="apps", on_click=lambda: print("'Apps' Clicked"))
    
ui.run()
```
