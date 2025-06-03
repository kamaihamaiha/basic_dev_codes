## CSS

Cascading Style Sheet(层叠样式表)，控制网页外观

### css & css3
CSS是从CSS1.0、CSS2.0、CSS2.1以及CSS3.0这四个版本一路升级而来的。其中，CSS2.1是CSS2.0的修订版，CSS3.0是CSS的最新版本。

### 内容简介
在学习中，我们只需要做出基本的CSS效果就可以了。如果你要想达到真正前端工程师的水平，必须学习CSS进阶部分。

### css引入方式
- 外部样式表
- 内部样式表
- 行内样式表

在实际开发中，一般都是使用外部样式表

#### 外部样式表
- 外部样式表是最理想的CSS引入方式。在实际开发中，为了提升网站的性能和可维护性，一般都是使用外部样式表
- CSS代码和HTML代码单独放在不同的文件中，然后在HTML文档中使用link标签来引用CSS样式表

在 html 的 ``<head></head>``标签使用 ``<link/>`` 标签引用css

```html
<link rel="stylesheet" type="text/css" href="css样式文件路径">
```
rel: relative

[代码 intro_extro.html](../../css_part/intro_external.html)

#### 内部样式表
也是在 ``<head></head>`` 内部，把css代码写在 ``<style></style>`` 中
```html
<style type="text/css">
    ...
</style>
```
[代码 intro_inner.html](../../css_part/intro_inner.html)

#### 行内样式表

在标签的style属性定义

[代码 intro_inner.html](../../css_part/intro_inner.html)
