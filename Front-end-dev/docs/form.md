## 表单

表单是我们接触动态页面的第一步。其中表单最重要的作用就是：在浏览器端收集用户的信息，然后将数据提交给服务器来处理。

[demo code: demo.html](../form_tag/demo.html)
### 表单标签
有五种：form、input、textarea、select和option

### 外观上，表单有8种

- 单行文本框
- 多行文本框
- 密码文本框
- 单选框
- 复选框
- 按钮
- 文件上传
- 下拉列表

#### form标签属性

- name: 区分表单用
- method: 指定表单数据使用哪一种http提交方法。method属性取值有两个，一个是get，另外一个是post。
- action: 指定表单数据提交到哪一个地址进行处理。
- target: 指定窗口的打开方式. 我们只会用到_blank这一个属性值。
- enctype: 指定表单数据提交的编码方式。一般情况下，我们不需要设置，除非你用到上传文件功能。

#### input标签

在HTML中，大多数表单都是使用input标签来实现的。

##### type属性取值

- text: 单行文本框
- password
- radio
- checkbox
- button/submit/reset
- file

##### 单行文本框

`<input type="text"/>`

**常用属性:**
- value: 默认值
- size: 文本框长度
- maxlength: 文本框最多输入字符数

##### 密码文本框
`<input type="password"/>`

##### 单选框
`<input type="radio"/>`

- 对于“同一组”的单选框，必须要设置一个相同的name，这样才会把这些选项归为同一个组上面;
- 为了得到更好的语义化，表单元素与后面的文本一般都需要借助label标签关联起来。
  - 见代码中的 年龄单选框
  - 见代码中的 年龄单选框