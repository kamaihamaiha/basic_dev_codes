### 成员方访问运算符

[代码](../../chapter_4/main_6.cpp)

ptr->mem 等价于 (*ptr).mem: 

- `->` 作用于指针类型
- `.` 作用于对象类型
```c++
string s1 = "hello";
string *p = &s1;

auto n = s1.size();   // 点运算符
n = (*p).size();      // 点运算符
n = p->size();        // 箭头运算符
```