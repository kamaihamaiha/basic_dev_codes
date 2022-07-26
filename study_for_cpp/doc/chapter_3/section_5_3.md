### 指针和数组
[代码](../../chapter_3/section_5/main_3.cpp)

指针和数组有非常紧密的关系。

```c++
string nums[] = {"one", "two", "three"};
string *p = &nums[0];     // p 指向 nums 的第一个元素
string *p2 = nums;        // 等价于上面。
```
**数组的一个特性**：   
在很多用到数组名字的地方，编译器会自动地将其替换为指向数组首个元素的指针。

在一些情况下，数组的操作实际上是指针的操作：
```c++
int ia[] = {1,2,3};
auto ia2(ia);       // ia2 是一个整型指针，指向 ia 的第一个元素
// 实际上编译执行的是如下操作：
auto ia2(&ia[0]);
```

**指针也是迭代器：**
```c++
int ia[] = {1,2,3,4};
int *p = ia;          // p指向 ia 的第一个元素 ia[0]
++p;                  // p指向 ia 的第二个元素 ia[1]
```
尾元素之后的地址：
```c++
// ia 接上
int *e = ia[4];     // ia[4] 并不是存在的元素，而是 e指向 ia 最后一个元素后面的地址。
                    // 就是为了提供地址初始化 e
```
**标准库函数 begin 和 end**

定义在头文件：`iterator` 中，使用如下：
```c++
// begin 和 end 函数
int ia[] = {1,2,3};
int *beg = begin(ia); // 指向首元素的指针
int *last = end(ia);  // 指向尾元素下一个地址的指针
```
**指针运算**

给指针加/减某整数值，结果仍为指针。指针也可以执行迭代器支持的运算：解引用、递增、比较等

```c++
constexpr size_t sz = 5;
int iar[sz] = {1, 2, 3, 4, 5};
int *p3 = iar;          // p3 指向 iar[0]
int *p4 = p3 + 4;       // p4 指向 iar[4]
int *p5 = iar + 1;      // p5 指向 iar[1]
```
指针相减，得到的类型：**ptrdiff_t**，定义在头文件 `cstddef` 中，是带符号类型。
```c++
auto n = end(iar) - begin(iar);
```

指针比较：
```c++
int *b = iar, *e = iar + sz;
while (b < e) {
  ++b;
}
```
注：如果指针分别指向不相关的对象，则不能比较

**解引用和指针运算的交互**
```c++
int iar2[] = {1,2,3,4};
int last2 = *(iar2 + 3);   // 把 last 初始化为 iar2[3]，也就是 4
int last3 = *iar2 + 3;     // 等价于 last3 = iar2[0] + 3
```

**下标和指针**
```c++
int iar3[] = {1,2,3,4,5};
int *p6 = iar3;
int i = *(p6 + 2);    // 等价于 i = iar3[2]
int *p7 = &iar3[2];   // p7 指向 iar3[2] 元素
int j = p7[1];        // j 的值就是 iar3[3] 元素的值
int k = p7[-2];       // k 的值就是 iar3[0] 元素的值
```

