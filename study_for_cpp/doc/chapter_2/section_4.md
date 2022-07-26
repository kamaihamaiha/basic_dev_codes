## const 限定符

const 用来限定常量。
```c++
const int buf_size = 1024; // buf_size 一旦定义后，就不能再改变值了
```
- const 修饰的对象必须初始化
- 默认情况下，const 对象仅在文件内有效
- 如果想在多个文件共享，则前面要加：`extern` 关键字

### const 的引用

```c++
const int a = 12;
const int &ai = a;    // 正确：引用及其对应的对象都是常量

ai = 1;               // 错误：ai 不能再赋值
int &ai2 = a;         // 错误：ai2 是非常量引用，不能引用一个常量引用
```

const 引用的对象并不一定是 const 对象，如下：
```c++
int a = 1;
int &r1 = a;        // 引用 r1 绑定对象 a
const int &r2 = a;  // 引用 r2 也绑定对象 a，但是不能通过 r2 修改 a 的值
r1 = 0;
r2 = 0;             // 错误：不能通过 r2 改变 a 的值
```

### 指针和 const
指向常量的指针（pointer to const）:
```c++
const double pi = 3.14;
const double *ppi = &pi;  // ok
double *ppi2 = &pi;        // error: ppi2 是普通指针，不能指向常量 pi
*ppi = 3.1415;             // error: 不能通过 ppi 修改 pi 的值
```

#### const 指针

- 必须初始化
- 一旦初始化，它的值（就是存放在指针中的那个地址）不能改变

```c++
int err_code = 1;
int *const pe = &err_code;    // const 指针 pe 指向了 err_code，不能再指向别的对象了

const double pi = 3.14;
cont double *const cpi = &pi; // const 指针 cpi 指向了 const 对象 pi，既不能再指向别的对象，也不同通过自己改变 pi 的值。
```

### 顶层 const 和 底层 const

- 顶层 const(top-level const)：表示指针本身是常量
- 底层 const(low-level const)：表示指针所指的对象是常量

- 更一般的，顶层 const 可以表示任意的对象是常量、底层 const 与指针和引用等复合类型的基本部分有关。
- 比较特殊的是，指针类型既可以是 top 也可以是 low

```c++
int i = 0;
int *const p1 = &i;   // 顶层 const
const int ci = 1;     // 顶层 const
const int *cp = &ci;  // 底层 const，因为指针 cp 所指向的 ci 是常量，但是指针 cp 不是常量，可以改变。
const int *const p3 = cp; // 右边的 const 是顶层 const，左边的 const 是底层 const
```

执行拷贝对象时，顶层 const 和 底层 const 是有区别的。具体没看懂，暂时略过。。。

---

### constexpr 和 常量表达式

常量表达式(const expression)是指：值不会改变且在编译过程就能得到计算结果的表达式。如：
```c++
const int max_files = 20;        // yes
const int limit = max_files + 1; // yes
int staff_size = 10;             // no: 因为数据类型是普通 int 而非 const int
const int sz = get_size();       // no: 尽管 sz 本身是一个常量(const int)，但是它的具体值要到运行时才能获取到
```

**constexpr** 变量

C++11 中允许将变量声明为 **constexpr** 类型以便由编译器来验证变量的值是否是一个常量表达式。

- 声明为 constexpr 的变量一定是一个常量
- 且必须用常量表达式初始化

#### 字面值类型(literal type)

值显而易见、容易得到。如：算数类型、引用、指针。自定义类、IO库、string 都不是。

#### 指针和 constexpr

如果用 constexpr 修饰指针，constexpr 限制仅对指针有效，对指针指的对象无效。也就是说是一个 top-level const

```c++
const int *p1 = nullptr;      // 指向整型常量的指针
constexpr int *p2 = nullptr;  // 指向整数的常量指针
```

