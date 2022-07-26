#include <iostream>

using namespace std;
/**
 * 内联函数：避免函数调用的开销
 * 一般用于优化规模较小、流程直接、频繁调用的函数
 * @return
 */
inline double calcArea(double radius);

int main(){
  cout << "请输入圆的半径:";
  int r;
  cin >> r;

  cout << "圆的面积: " << calcArea(r) << endl;

  return 0;
}

inline double calcArea(double radius) {
  return 3.14 * radius * radius;
}