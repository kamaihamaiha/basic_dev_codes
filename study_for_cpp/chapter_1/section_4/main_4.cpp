#include <iostream>
int main(){

  // 使用 for
  bool useFor = false;

  // 练习 1.9 使用 while 循环，将 50 到 100 的整数相加
  int sum = 0;
  int start = 50;
  int end = 100;
  int value = start;

  if (useFor) {
    for(int i = start; i <= end; i++) {
      sum += i;
    }
  } else {
    while (value <= end) {
      sum += value;
      value++;
    }
  }


  std::cout << "sum: " << sum << std::endl;

  // 练习 1.10 使用递减运算符，在循环中按照递减顺序打印出 10 到 0 之间到整数
  std::cout << "练习 1.10" << std::endl;
  start = 10;
  end = 0;
  value = start;

  if (useFor) {
    for (int i = start; i >= end; --i) {
      std::cout << i << std::endl;
    }
  } else {
    while (value >= end) {
      std::cout << value << std::endl;
      value--;
    }
  }


  // 练习 1.11 提醒用户输入两个整数，打印出这两个整数所指定到返回内的所有整数
  std::cout << "请输入两个数：" << std::endl;
  std::cin >> start >> end;

  if (useFor) {
    if (start > end) {
      int temp = start;
      start = end;
      end = temp;
    }
    for (int i = start; i <= end; ++i) {
      std::cout << i << std::endl;
    }
  } else {
    if (start < end) {
      while (start <= end) {
        std::cout << start << std::endl;
        start++;
      }
    } else if (start > end) {
      while (start >= end) {
        std::cout << start << std::endl;
        start--;
      }
    } else {
      std::cout << start << std::endl;
    }
  }

  // 练习 1.16 读取数量不定的输入数据
  // 重置变量值（前面已经定义过了）
  value = 0;
  sum = 0;

  // 注意，如果是在 IDE 操作，Ctrl + D 有可能为 IDE 的快捷键，于是就冲突了。那么可以打开 Terminal，用命令编译、运行。
  std::cout << "请输入任意个数字，按下 Ctrl + D 停止输入：" << std::endl;
  while (std::cin >> value) {
    sum += value;
  }
  std::cout << "sum: " << sum << std::endl;

  return 0;
}

