## 处理类型

- 类型别名
- auto 类型说明符
- decltype 类型指示符

### 类型别名(type alias)

使用关键字：**typedef**
```c++
typedef double wages;     // wages 是 double 的同义词
typedef wages base, *p;   // base 是 double 的同义词，p 是 double* d的同义词
```

### 指针、常量和类型别名

枯燥、难懂、暂时略过...

### auto 类型说明符
枯燥、难懂、暂时略过...

### decltype 类型指示符

有时会有这种情况：想从表达式的类型推断要定义的变量的类型，但是不想用该表达式的值初始化变量。

于是 C++11 引入了 **decltype**：选择并返回操作数的数据类型。在此过程中，编译器分析表达式   
并得到它的类型，却不实际计算表达式的值。
```c++
decltype(f()) sum = x;    // sum 的类型就是函数 f() 的返回类型
```


