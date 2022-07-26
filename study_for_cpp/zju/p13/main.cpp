#include <iostream>

using namespace std;

struct A {
  int i;
  int *p;

 public:
  // A() 后面，对成员变量初始化，就是初始化列表
  A():p(0) {}
  ~A(){}
};

class Point {
 private:
  const float x, y;

 public:
  // 初始化列表
  Point(float xa = 0.0, float ya = 0.0): y(ya), x(xa) {}
};

int main(){

  return 0;
}