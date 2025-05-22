## 表格

**基本结构:**

表格+行+单元格

- 表格: `<table>`
- 行: `<tr>`
    - table row
- 单元格: `<td>`
    - table data cell

- [代码: intro.html](../table_tag/intro.html)    

**完整结构:**

- 表格标题: `<caption>`
- 表头单元格: `<th>`
    - table header cell
- [代码: transcript.html](../table_tag/transcript.html)    

#### 注意

th和td在本质上都是单元格，但是并不代表两者可以互换，它们之间具有以下两种区别。显示上：浏览器会以“粗体”和“居中”来显示th标签中的内容，但是td标签不会。语义上：th标签用于表头，而td标签用于表行。


### 语义化

一个完整的表格包含：table、caption、tr、th、td。为了更深入地对表格进行语义化，HTML引入了thead、tbody和tfoot这三个标签。thead、tbody和tfoot把表格划分为三部分：表头、表身、表脚。有了这三个标签，表格语义更加良好，结构更清晰，也更具有可读性和可维护性。

- [代码: transcript_complete.html]()

**说明**:

表脚（tfoot）往往用于统计数据。对于thead、tbody和tfoot这三个标签，不一定全部都用上，例如tfoot就很少用。一般情况下，我们都是根据实际需要来使用这三个标签。thead、tbody和tfoot这三个标签也是表格中非常重要的标签，它从语义上区分了表头、表身和表脚，很多人容易忽略这三个标签。此外，thead、tbody和tfoot除了使得代码更具有语义之外，还有另外一个重要作用：方便分块来控制表格的CSS样式。

### 合并行，合并列

- rowspan
- colspan

[代码: span_demo.html](../table_tag/span_demo.html)

在实际开发中，合并行与合并列用得很少，如果忘了，等需要的时候回来这里查一下即可。


### 编程题

[代码: practice.html](../table_tag/practice.html)