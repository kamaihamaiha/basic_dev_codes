#include <iostream>

using namespace std;


class A {
 public:
  int i;

 public:
  A():i(10) {}
};

class B: public A{

};

int main(){

  A a;
  B b;

  cout << "a.i= " << a.i << ", b.i= " << b.i << endl;

  int *p = (int*)&a;
  cout << "address of a: " << p << ", value of a: " << *p << endl;

  *p = 20;
  cout << "value of a.i: " << a.i << endl;

  p = (int*)&b;
  cout << "address of b: " << p << ", value of b: " << *p << endl;
  return 0;
}