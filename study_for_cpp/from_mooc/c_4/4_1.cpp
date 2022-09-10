#include <iostream>

using namespace std;

int main() {

  char c1 = 'yes';

  // 错误：字符串常量不能赋值给 char 变量
//  char c2 = "yes";
  const char* c3 = "yes";

  // 错误：字符类型不能赋值给 字符串创两
//  const char* c4 = 'yes ';
  cout << "c1: " << c1 << endl;
  return 0;
}