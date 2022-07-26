### 3.1 命名空间的 using 声明
[代码](../../chapter_3/section_1/main.cpp)   

前面用到的标注输入输出：`std::cout` 和 `std::cin` 等写法比较繁琐，还要加前缀：`std::`   

用 **using声明**，可无需再加前缀，形式如下：   
``using namespace::name;``

**代码举例：**
```c++
#include <iostream>
// using 声明，当使用名字 cin 时，从命名空间 std 中获取它
using std::cin
int main(){
  int i;
  cin >> i;
  
  return 0;
}
```

#### 用到的每个名字都需要独立的 using 声明

```c++
#include <iostream>
// using 声明
using std::cin; using std::cout; using std::endl;
int main(){
    int i;
    cin >> i;
    cout << i << endl;
    return 0;
}
```

#### 头文件不应包含 using 声明

