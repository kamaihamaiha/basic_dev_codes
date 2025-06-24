## 超链接样式


- 超链接伪类
- 深入了解:hover
- 鼠标样式

### 超链接伪类

在CSS中，可以使用“超链接伪类”来定义超链接在鼠标点击的不同时期的样式。

- a:link
  - 默认的样式
- a:visited
  - 访问后的样式
- a:hover
  - 鼠标经过时的样式
- a:active
  - 鼠标点击时的样式

定义这四个伪类，必须按照link、visited、hover、active的顺序进行，不然浏览器可能无法正常显示这四种样式。请记住，这四种样式定义顺序不能改变;

[代码 demo1](../../css_part/hyperlink_style/demo1.html)

实际开发中只会用到 未访问时状态和鼠标经过时状态:
```css
a:{xxx}
a:hover{xxx}
```
[代码 demo2](../../css_part/hyperlink_style/demo2.html)


### 深入了解:hover

:hover伪类可以定义任何一个元素在鼠标经过时的样式！注意，是任何元素喔。

```css
元素:hover{xxx}
```
[代码 demo_hover](../../css_part/hyperlink_style/demo_hover.html)
