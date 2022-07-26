#include <iostream>

using namespace std;

// 4.9 节练习
int main(){

  int ia[] = {1, 2, 3};
  auto ia_size = sizeof(ia) / sizeof(*ia);

//  cout << "ia size: " << ia_size;

  // 练习4.28 输出每一种内置类型所占空间大小
  cout << "size of char: " << sizeof(char) << endl;
  cout << "size of wchar_t: " << sizeof(wchar_t) << endl;
  cout << "size of char16_t: " << sizeof(char16_t) << endl;
  cout << "size of char32_t: " << sizeof(char32_t) << endl;
  cout << "size of bool: " << sizeof(bool) << endl;
  cout << "size of short: " << sizeof(short) << endl;
  cout << "size of int: " << sizeof(int) << endl;
  cout << "size of long: " << sizeof(long) << endl;
  cout << "size of long long: " << sizeof(long long) << endl;
  cout << "size of float: " << sizeof(float) << endl;
  cout << "size of double: " << sizeof(double) << endl;

  // 练习4.29
  int x[10];
  int *p = x;
  cout << sizeof(x) / sizeof(*x) << endl;
  cout << sizeof(p) / sizeof(*p) << endl;

  return 0;
}