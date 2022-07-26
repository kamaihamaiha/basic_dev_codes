#include <iostream>

using namespace std;

class A {
 private:
  int i;

 public:
  A(){
    cout << "A::A()" << endl;
  }

  ~A(){
    cout << "A::~A(), i= " << this->i << endl;
  }

  void setValue(int v) {
    this->i = v;
  }



};

int main(){

  // Dynamic Arrays
  int *p_some = new int [10];

  delete[] p_some;

  A *a_10 = new A[10];
  for (int i = 0; i < 10; ++i) {
    a_10[i].setValue(i + 1);
  }
  delete[] a_10;
  return 0;
}