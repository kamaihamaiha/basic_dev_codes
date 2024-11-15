## 内置数据类型

### 常见数据类型

- 数字: int, float, complex
- 文本: str
- 序列: list, tuple, range
- 映射: dict

### 列表的常见操作

- [code demo1](./list_demo.py)
- [code demo2](./list_demo2.py)
- [code demo3](./list_demo3.py)

### 元组

tuple

### 集合
- set 和 frozenset
- 里面的元素不重复

#### 创建

- `{...}`
- 集合推导式
- `set()` 构造器

#### set对象常见操作

- `len(s)`
- `x in s`
- `set <= other`: 检测set集合中的每个元素是否在 other 中
- `set < other`: 检测set集合是否为 other 的真子集
- `add()`, `remove()`, `pop()`, `clear()`

### 字典
[code demo](./dict_demo.py)
- 整数1和浮点数1.0 会被当作相同的键
- 定义字典
  - 用`{}`
  - 用`dict()`
  - 用字典推到式
- 删除
  - del dict
  - del dict(key)

#### 字典的常见操作

- 内置函数
- 高级用法
- 与其他数据类型的混合使用
  - list(), dict(), str()
  - 合并两个列表为字典: `dict(zip(列表1, 列表2))`




