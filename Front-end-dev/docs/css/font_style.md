## 字体样式

**属性**

- font-family: 字体类型
- font-size:
- font-weight: 字体粗细
- font-style: 字体风格
- color

### font-family

语法
```css
font-family: 字体1, 字体2, ... 字体N
```
说明: 使用多个字体时，将按从左到右的顺序排列，并且以英文逗号（，）隔开。如果我们不定义font-family，浏览器默认字体类型一般是“宋体”。

[代码 font_demo](../../css_part/font_style/font_demo.html)

如果字体类型只有一个英文单词，不需要加双“”；如果是多个英文单词或者是中文，要加“”

如果指定了多个字体，则从左到右寻找，电脑支持那个就用哪个。

#### 比较美观的字体

- 中文字体: 微软雅黑,宋体
- 英文字体: Times New Roman, Arial, Verdana

### font-size
语法
```css
font-size:关键字/像素值;
```
- 关键字: small, medium, large; 实际开发中很少用
[代码 font_demo](../../css_part/font_style/font_demo.html)

### font-weight
语法
```css
font-weight:xxx;
```
2种取值: 
- 100~900 的数
- 关键字: normal, lighter, bold, bolder
  - 一般用 bold，其他几乎用不到
[代码 font_demo](../../css_part/font_style/font_demo.html)

### font-style
语法
```css
font-style:xxx;
```
取值: normal, italic, oblique
[代码 font_demo](../../css_part/font_style/font_demo.html)

### color
语法
```css
color:颜色值;
```
取值: 关键字/16进制RGB值
[代码 font_demo](../../css_part/font_style/font_demo.html)

---
小技巧: 浏览器解析css是按照顺序的，比如：用元素选择器定义颜色`color:red;` ，后面再用id选择器定义颜色`color:blue`。后面的会覆盖前面的，最终显示蓝色

---

[练习题 practice](../../css_part/font_style/practice.html)
