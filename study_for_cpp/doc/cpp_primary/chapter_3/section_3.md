### 标准库类型 vector

vector 表示对象的集合，也称作**容器**(container)。

使用时，要引入头文件，然后 using 声明
```c++
#include <vector>
using std::vector;
```
C++ 有**类模板** 和 **函数模板**，vector 是类模板。但是模板本身不是类或函数。

vector 使用举例：
```c++
vector<int> ivec;
vector<Sales_item> Sales_vec;
```

---

- [3.3.1 定义和初始化 vector 对象](./section_3_1.md)
- [3.3.2 向 vector 对象添加元素](./section_3_2.md)
- [3.3.3 其他 vector 操作](./section_3_3.md)