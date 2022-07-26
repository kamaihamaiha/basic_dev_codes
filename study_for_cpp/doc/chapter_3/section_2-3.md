### 处理 string 对象中的字符

[代码](../../chapter_3/section_2/main_for.cpp)

头文件 ``cctype`` 中定义类一组标准库函数处理字符。见书中表-3.3: P82

**建议**: 使用 C++ 版本的 C标准库头文件

- cctype 头文件其实是 C++ 为了兼容 C语言标准库 `ctype.h`，在 C++ 用 `cctype` 替代。

---

#### for 语句

##### 遍历：
```c++
string str("abcde");
for(auto c : str) {
  cout << c << endl;
}
```

##### 改变字符串中的字符：
如果要改变 string 对象中的字符的值，必须把循环变量定义成引用类型。
```c++
  // 把字符都改成大写
  string str("abcde");
  for(auto &c : str) {
    c = toupper(c);
  }
  cout << str << endl;
```

##### 只处理一部分字符
使用下标
```c++
  // 把第一个字符改为大写
  if (str.size() > 0) {
    str[0] = toupper(str[0]);
  }
  cout << str << endl;
```
注：检查下标合法性，下标类型建议设置为 `string::size_type`

##### 使用下标执行随机访问

```c++
const string hex_str = "0123456789ABCDEF";
  cout << "输入任意数字(0 - 15)之间的，输入 -1 结束" << endl;
  string res;
  string::size_type num;
  while (cin >> num ) {
    if (num == -1) break;
    res += hex_str[num];
  }
  cout << "十六进制数：" << res << endl;
```