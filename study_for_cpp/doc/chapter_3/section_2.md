### 标准库类型 string

- **string**表示可变长的字符序列
- 使用 string 必须包含 string 头文件
- 作为标准库的一部分，string 定义在命名空间 std 中

必须要做的事情：
```c++
#include <string>
using std::string;
```
---

- 3.2.1 定义和初始化 string 对象
- 3.2.2 [string 对象上的操作](./section_2-2.md)
- 3.2.2 [处理 string 对象中的字符](./section_2-3.md)

---

#### 3.2.1 定义和初始化 string 对象

初始化方式：
```c++
string s;               // 默认初始化，s 是一个空串
string s2 = s;          // s2 是 s 的副本
string s3(s);           // s3 是 s 的副本。等价于上面的方式
string s4 = "cpp";      // s4 是字面值 "cpp" 的副本
string s5("cpp");       // 等价于上面
string s6(3, 'c');      // 初始化为 3个字符 'c' 组成的字符串
```

上面的初始化方式分为两种：**拷贝初始化** 和 **直接初始化**

- 拷贝初始化：使用 `=` 初始化
- 直接初始化：不使用 `=` 初始化