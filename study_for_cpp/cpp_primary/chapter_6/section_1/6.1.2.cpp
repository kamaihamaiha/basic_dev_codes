#include <iostream>
#include "Chapter6.h"

using namespace std;

int main() {

  fact(9);

  return 0;
}

// 定义函数
int fact(int val){
  int ret = 1;
  while (val > 1) {
    ret *= val--;
  }
  return ret;
}

