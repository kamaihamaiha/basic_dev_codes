### sizeof 运算符
[4.9 节练习代码](../../chapter_4/4.9.cpp)   

sizeof 运算符返回一条表达式或者一个类型名字所占的字节数，是 `size_t` 类型。

#### 运算对象有两种形式

- `sizeof (type)`
- `sizeof expr`
    - 表达式 expr 结果类型的大小
    
##### 注意事项

- sizeof(数组): 整个数组空间大小
- sizeof(string 或者 vector): 只返回该类型固定部分大小，不会计算对象中元素占用了多少空间。

**一个应用举例：**
```c++
int ia[] = {1, 2, 3};
size_t ia_size = sizeof(ia) / sizeof(*ia);  // 计算数组的元素个数
```

