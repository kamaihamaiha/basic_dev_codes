### 与旧代码的接口

[代码](../../chapter_3/section_5/main_5.cpp)


```c++
 // 使用 字符串字面值初始化 string 对象
  string s1("Hello");
  
  // C语言中字符数组
  const char s2[] = {'H', 'e', 'l', 'l', 'o', '\0'};
  const char s3[] = "Hello";
  
  // 混用 string 对象和 C 风格字符串
  string s4 = {'H', 'e', 'l', 'l', 'o', '\0'};
  
  // C 风格字符串，初始化想从 string 获取
  const char *s5 = s4.c_str();
```
注：如果执行完 `c_str()` 函数后，程序想一直都能使用其返回的数组，最好重新拷贝一份。

#### 使用数组初始化 vector 对象
```c++
 // 使用数组初始化 vector 对象
  int ia[] = {0, 1, 2, 3, 4, 5};
  vector<int> iva(begin(ia), end(ia));    // 将 ia 的全部元素都复制类
  vector<int> iva2(ia + 1, ia + 3);    // 只 复制 ia 的一部分：ia[1] 和 ia[2]
```
**建议：** 尽量使用标准库类型而非数组

- 尽量使用 vector 和 迭代器，避免使用内置数组和指针
- 尽量使用 string，避免使用 C 风格的基于数组的字符串