#include <iostream>

/**
 * 引用
 */
int main(){

  int i = 0, &r1 = i;
  double d = 0, &r2 = d;

  r2 = 3.14;
  r2 = r1;

  // 练习 2.17. 输出结果为 10, 10
  int j, &rj = j;
  j = 5;
  rj = 10;
  std::cout << j << ", " << rj << std::endl;

  // 练习：2.18
  int a = 2;
  int *pa = &a;
  std::cout << a << ", pa= " << *pa << std::endl;
  *pa = 3;
  std::cout << a << ", pa= " << *pa << std::endl;
  pa = 0;
  std::cout << a << ", pa= " << (pa == nullptr) << std::endl;

  // 练习：2.19
  int b = 3;
  int *pb = &b;
  *pb = *pb * *pb;
  std::cout << *pb << std::endl;

  return 0;
}
