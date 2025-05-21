## 基本标签

### html 结构

- 文档声明
- html标签对
- head标签对
- body标签对

- [一个简单的页面](../basic_tag/index.html)

### head标签

只有6个标签可以放在head标签内

- title, meta, link, style, script, base

#### title 标签

- 定义网页标题，就是现实在浏览器的tab地方

#### meta 标签

- 定义页面特殊信息
- name 属性
- http-equiv 属性: 有2个作用
  - 定义网页所使用的编码: `<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>`
    - 在html5标准中，可简写为: `<meta charset="utf-8"/>`
    - 这个标签告诉浏览器，该页面使用的编码是 utf-8
    - 实际开发中，为了确保不出现乱码，要在每一个页面中加上这句话
  - 定义网页自动刷新跳转: `<meta http-equiv="refresh" content="6;url=http://www.google.com"/>`
    - 表示当前页面在6s之后自动跳转到谷歌首页

#### style 标签

定义元素 css样式

`<style type="text/css">
  这里写css样式
</style>
`

#### script 标签
定义页面的 JavaScript 代码或者引入外部JavaScript文件


#### link 标签
引入外部样式文件(css文件)

#### base 标签
没意义，忽略


### body 标签

- [举例： 静夜思](../basic_tag/quiet_night_thoughts.html)