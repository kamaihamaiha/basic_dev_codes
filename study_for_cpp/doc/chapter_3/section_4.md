### 迭代器介绍
[代码](../../chapter_3/section_4/main.cpp)   

访问 string 对象的字符或者 vector 对象的元素，还有另外一种方式：**迭代器**(iterator)

- 迭代器可以访问某个元素
- 迭代器也能从一个元素移动到另外一个元素

```c++
auto b = v.begin();   // 第一个元素
auto e = v.end();     // 尾元素的下一个位置
```
注：   
 - b、e 的类型由编译器决定。
 - 如果容器为空，begin 和 end 返回的是同一个迭代器，都是尾后迭代器

#### 迭代器运算符

| 运算符         | 含义                                                         |
| -------------- | ------------------------------------------------------------ |
| *iter          | 返回迭代器 iter 所指元素的引用                               |
| iter->mem      | 解引用 iter 并获取该元素的名为 mem 的成员，等价于 (*iter).mem |
| ++iter         | 指向下一个元素                                               |
| --iter         | 指向上一个元素                                               |
| iter1 == iter2 |                                                              |
| iter1 != iter2 |                                                              |

举例，改些 3.2.3 节的例子：
```c++
 string str("hello");
  if (str.begin() != str.end()) {   // 第一个字符改为大写
    auto it = str.begin();
    *it = toupper(*it);
  }
  cout << str << endl;
```

##### 从一个元素移动到另外一个元素

举例，把所有字母改为大写：
```c++
// 把所有字母改为大写
  string str1("hello");
  for(auto it = str1.begin(); it != str1.end() && !isspace(*it); ++it) {
    *it = toupper(*it);
  }
  cout << str1 << endl;
```

##### 迭代器类型
标注库类型使用 iterator 和 const_iterator 表示迭代器类型：
```c++
vector<int>::iterator it;       // it 能读能写 vector<int> 的元素
string::iterator its;           // its 能读能写 string 对象中的字符

vector<int>::const_iterator itc; // itc 只能读元素，不能写元素
string::const_iterator itsc;     // itsc 只能读元素，不能写元素
```
##### begin 和 end 运算符
begin 和 end 返回的具体类型由对象是否是常量决定，如果是常量返回 const_iterator；否则返回 iterator.

C++11 引入了两个新函数：cbegin 和 cend。返回值是确定的 const_iterator

##### 结合解引用和成员访问操作
解引用迭代器可以获取迭代器所指的对象。
`(*it).mem`  和 `it->mem` 等价

##### 有些操作会使得迭代器失效

如果操作会改变 vector 对象容量，比如 push_back 就会使 vector 对象的迭代器失效。

注：但凡使用了迭代器的循环体，都不要向迭代器所属的容器添加元素

---

#### 迭代器运算

| Iter + n      | 迭代器往后移动 n 个位置，仍是一个迭代器                      |
| ------------- | ------------------------------------------------------------ |
| iter - n      | 迭代器往前移动 n 个位置，仍是一个迭代器                      |
| Iter1 - iter2 | 两个迭代器之间距离                                           |
| >、>=、<、<=  | 迭代器关系运算符，比较迭代器指向的容器位置。参与运算的迭代器必须指向的同一个容器中的元素 |


