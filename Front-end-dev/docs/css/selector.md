## 选择器

针对CSS初学者的，最实用的五种选择器

- 元素选择器
- id选择器
- class选择器
- 后代选择器
- 群组选择器

**语法**
```css
选择器
{
    属性1: vlaue1;
    ...
    属性n: vlauen;
}
```

### 元素选择器
举例
```css
div {
    width: 10px;
    height: 20px;
}
```
[代码 type_selector.html](../../css_part/selector/type_selector.html)

### id选择器
举例
```css
#box {
    width: 10px;
    height: 20px;
}
```
对于id选择器，id名前面必须要加上前缀#，否则该选择器无法生效。在id名前面加上#，表示这是一个id选择器。
[代码 id_selector.html](../../css_part/selector/id_selector.html)

### class选择器
举例
```css
.box {
    width: 10px;
    height: 20px;
}
```
class名前面必须要加上前缀。（英文点号），否则该选择器无法生效。在类名前面加上. 表明这是一个class选择器。
[代码 class_selector.html](../../css_part/selector/class_selector.html)

### 后代选择器
父元素和后代元素必须要用空格隔开，从而表示选中某个元素内部的后代元素。
举例
```css
#p c {
    color: red;
}
```
[代码 descendant_selector.html](../../css_part/selector/descendant_selector.html)

### 群组选择器
群组选择器，指的是同时对几个选择器进行相同的操作
举例
```css
h3, p, div {
    color: red;
}
```
[代码 group_selector.html](../../css_part/selector/group_selector.html)

---

[练习题 practice.html](../../css_part/selector/practice.html)

想要选中所有的div和p
