### string 对象上的操作
[代码](../../chapter_3/section_2/main.cpp)
**大部分的 string 操作：**

| 操作           | 含义                                                  |
| -------------- | ----------------------------------------------------- |
| os << s        | 将 s 写到输出流 os 中，返回 os                        |
| is >> s        | 从 is 中读取字符串赋值给 s，字符串已空白分隔，返回 is |
| getline(is, s) | 从 is 读取一行赋值给 s，返回 is                       |
| s.empty()      | 判断是否为空                                          |
| s.size()       | 字符个数                                              |
| s[n]           | 返回 s 中第 n 个字符的引用                            |
| s1 + s2        | 连接                                                  |
| s1 = s2        | s2 替代 s1                                            |
| s1 == s2       | 是否相等                                              |
| s1 != s2       | 是否不相等                                            |
| <, <=, >, >=   | 比较在字典中的顺序，区分大小写                        |

- 读写 string 对象
- 读取未知数量的 string 对象
- 使用 getline 读取一整行
- string 的 empty 和 size 操作
- string::size_type 类型
- 比较 string 对象
- 两个 string 对象相加
- 字面值和 string 对象相加

---

#### 读写 string 对象

```c++
  ...
  // 空字符串
  string s;
  // 从输入中读取字符串到 s
  cin >> s;
  // 输出
  cout << s << endl;
  ...
```
注：string 会自动忽略开头的空白(空格符、换行符、制表符等)，从第一个真正的字符开始，知道遇见下一处空白为止。

#### 读取未知数量的 string 对象

```c++
string word;
  cout << "请输入任意内容：" << endl;
  while (cin >> word) {
    cout << word << endl;
    cout << "继续输入：" << endl;
  }
```

#### 使用 getline 读取一整行
```c++
string line;
  cout << "读取一整行,请输入任意内容：" << endl;
  while (getline(cin, line)) {
    cout << line << endl;
  }
```
#### string 的 empty 和 size 操作
```c++
string line;
  cout << "读取一整行,请输入任意内容：" << endl;
  while (getline(cin, line)) {
    if (!line.empty()) { // 判断，不是空行才输出
      if (line.size() >= 3) { // 一行的长度超过 3 才输出
        cout << line << endl;
      }
    }
  }
```

#### string::size_type 类型
string.size() 返回的类型是 **string::size_type**   

string 类和其他大多数标准库类型都定义了几种配套的类型。这些配套类型体现了标准库类型与机器无关的特性，   
**size_type**就是其中的一种，具体使用是，通过作用域操作符来表明名字 size_type 是在类 string 中定义的。

注：size() 返回的是 unsigned 整数，因此切记不要和 int 型的数比较。如果 int 数是负数，判断结果是错误的

#### 比较 string 对象

```c++
string s1 = "Hello";
string s2 = "Hello kk"; // s2 比 s1 大
string s3 = "Hill"      // s3 比 s2 大
```
#### 两个 string 对象相加
```c++
string a = "A", b = "B";
string s1 = a + b;        // s1的内容是：AB
```
#### 字面值和 string 对象相加

```c++
string a = "A", b = "B";
string s = a + "," + b;   // s的内容是：A,B
string s2 = "a" + "b";    // 错误，因为运算符 + 两边要至少有一个是 string 对象
string s3 = "a" + "b" + a;// 错误: 不能把字面值直接相加
string s4 = "a" + ("b" + a); // ok: 因为 ("b" + a) 是 string 对象
```

注意：因为某些历史原因，也为了兼容 C语言，C++ 中的字符串字面值并不是标准库类型 string 的对象。