#include <iostream>

int main(){

  // 例子代码
  std::cout << "Enter two numbers:" << std::endl;
  int value1 = 0, value2 = 0;

  std::cin >> value1 >> value2;
  std::cout << "数之和：" << value1 << " + " << value2 << " = " << value1 + value2 << std::endl;

  // 练习1：打印 hello world
  std::cout << "hello world!";
  std::cout << std::endl;

  // 练习2：乘法运算
  std::cout << "Enter two numbers:" << std::endl;
  int v1 = 0, v2 = 0;
  std::cin >> v1;
  std::cin >> v2;

  std::cout << "两数之积：" << v1 << "*" << v2 << "= " << v1 * v2;
  std::cout << std::endl;

  return 0;
}
