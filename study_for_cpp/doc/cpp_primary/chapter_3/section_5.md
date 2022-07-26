### 数组

[代码](Codes/basic_dev_codes/study_for_cpp/cpp_primary/chapter_3/section_5/main_1.cpp)
- 定义和初始化内置数组
- 访问数组元素
- [指针和数组](Codes/basic_dev_codes/study_for_cpp/doc/cpp_primary/chapter_3/section_5_3.md)
- [C 风格字符串](Codes/basic_dev_codes/study_for_cpp/doc/cpp_primary/chapter_3/section_5_4.md)
- [与旧代码的接口](Codes/basic_dev_codes/study_for_cpp/doc/cpp_primary/chapter_3/section_5_5.md)

---

#### 定义和初始化内置数组

```c++
int arr1[10];     // 含有 10 个整数的数组
int *arr2[10];    // 含有 10 个整型指针的数组
```

##### 显示初始化数组元素
```c++
 int a1[3] = {1, 2, 3};
 int a2[] = {1, 2, 3};
 int a3[5] = {1, 2, 3};          // 等价于 a3[5] = {1, 2, 3, 0, 0};
 string a4[3] = {"hi", "hell"};  // 等价于 a4[3] = {"hi", "hell"， ""};
```

##### 字符数组的特殊性

```c++
char ca1[] = {'a', 'b', 'c'};       // 实际有 4 个字符，末尾有个空字符
char ca2[] = {'a', 'b', 'c', '\0'}; // 显式的空字符：\0
char ca3[] = "cpp";                 // 实际有 4 个字符，末尾有个空字符
char ca4[5] = "hello";              // error: 没有空间存放空字符了
```

##### 不允许拷贝和赋值

不能把数组的内容拷贝给其他数组作为其初始值，也不能用数组为其他数组赋值。

---

#### 访问数组元素

使用数组下标访问，通常定义为 **size_t**类型：是一种机器相关的无符号类型。   
在 `cstddef`头文件中定义了这个类型，这文件是 C标准库 `stddef.h` 头文件   
的 C++语言版本。