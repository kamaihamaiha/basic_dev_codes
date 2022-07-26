#include <iostream>

using namespace std;

class A {
 public:
  A(): i(8) {}
  virtual void f() {
    cout << "A::f() " << i << endl;
  }

  int i;
};

class B: public A {
 public:
  B(): j(20){}
  virtual void f() {
    cout << "B::f() " << j << endl;
  }

  int j;
};

int main (){

  A a;
  B b;
  a.f();

  A* pa = &a;
  // A 的 f()
  pa->f();


  int *p = (int*)&a;
  int *q = (int*)&b;

  *p = *q;
  // B 的 f()
  pa->f();

  return 0;
}