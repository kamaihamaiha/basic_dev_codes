#include <iostream>
using namespace std;

int add(int origin);
void print(int value);
int callCount();

int main(){

  for (size_t i = 0; i < 8; ++i) {
//    print(add(i));
    print(callCount());
  }
  return 0;
}

/**
 * 练习 6.7。含有：形参、局部变量、局部静态变量
 * @param origin
 * @return
 */
int add(int origin){
  int a;
  static size_t count = 0;
  a = origin + 1;
  count++;
  return count;
}

void print(int value) {
  cout << value << endl;
}

/**
 * 练习 6.7 第一次被调用返回 0，以后每次调用返回值加1
 * @return
 */
int callCount(){
  static size_t count = 0;
  return count++;
}

