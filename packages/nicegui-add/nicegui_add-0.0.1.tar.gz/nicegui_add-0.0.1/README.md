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

## 版本记录 / Version record

> `0.0.1`
>> `0011` 第一次发布，包含 `bar`, `breadcrumbs`, `breadcrumbs_el`, `space`, `toolbar`, `toolbar_title`组件