#include <iostream>
#include "A.h"

using namespace std;


void A::f() {
  int j = 10; // 本地变量
  i = 10;     // 成员变量
}

int main(){

  A a;
  a.f();


  return 0;
}