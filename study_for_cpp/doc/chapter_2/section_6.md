### 自定义数据结构
[代码](../../chapter_2/section_6/main.cpp)
- 定义 Sales_date 类型
- 使用 Sales_date 类
- 编写自己的头文件

---

#### 定义 Sales_date 类型

```c++
struct Sales_data {
  std::string bookNo;
  unsigned units_sold = 0;
  double sum = 0.0;
};
```

#### 使用 Sales_date 类

```c++
#include <iostream>

struct Sales_data {
  std::string bookNo;
  unsigned units_sold = 0;
  double sum = 0.0;
};

int main(){

  double price = 0;
  Sales_data data1, data2;

  std::cout << "请输入第一本书的交易信息，ISBN、销售数量、单价：" << std::endl;
  std::cin >> data1.bookNo >> data1.units_sold >> price;
  data1.sum = data1.units_sold * price;

  std::cout << "请输入第二本书的交易信息，ISBN、销售数量、单价：" << std::endl;
  std::cin >> data2.bookNo >> data2.units_sold >> price;
  data2.sum = data2.units_sold * price;

  // 输出两个对象的和
  if (data1.bookNo == data2.bookNo) {
    double total_sum = data1.sum + data2.sum;
    unsigned total_units_sold = data1.units_sold + data2.units_sold;
    std::cout << "总交易细信息，ISBN：" << data1.bookNo << ", 售出：" << total_units_sold << "本，共收入："
    << total_sum << "$" << std::endl;
  } else {
    std::cerr << "ISBN 必须相同！" << std::endl;
    return -1;
  }

  return 0;
}
```

#### 编写自己的头文件

- 头文件通常包含那些只能被定义一次的实体，如类、const 和 constexpr 变量。
- 头文件也能包含其他头文件
- 头文件包含了多次：使用类包含头文件 a.h(此头文件包含 string.h)，使用类也包含类 string.h，那么需要做适当处理
- 头文件一旦改变，相关的源文件必须重新编译以获取更新过的声明

##### 预处理器概述

确保头文件多次包含仍能安全工作的常用技术是**预处理器**(preprocessor)

`#include` 从 C语言继承，在编译前执行的一段程序，可以部分地改变我们所写的程序，当与处理器   
看到 `#include`标记时就会用指定的头文件的内容替代`#include`

**头文件保护符**(header guard)
依赖于预处理变量，预处理变量有两种变量：已定义和未定义。

- `#define`指令把一个名字设定为预处理变量
- `#indef`: 是否已定义。如果检查结果为真，则往下执行，直到遇到 `#endif` 指令为止
- `#inndef`: 是否未定义。如果检查结果为真，则往下执行，直到遇到 `#endif` 指令为止
- `#endif`:

```c++

#ifndef STUDY_FOR_CPP_CHAPTER_2_SECTION_6_SALES_DATA_H_
#define STUDY_FOR_CPP_CHAPTER_2_SECTION_6_SALES_DATA_H_

struct Sales_data {
  std::string bookNo;
  unsigned units_sold = 0;
  double sum = 0.0;
};

#endif //STUDY_FOR_CPP_CHAPTER_2_SECTION_6_SALES_DATA_H_

```

