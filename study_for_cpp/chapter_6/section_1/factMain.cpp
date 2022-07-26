#include <iostream>
#include "Chapter6.h"

using namespace std;

int main(){

  cout << "请输入一个整数: " << endl;
  int val;
  cin >> val;
  cout << val << "的阶乘为：" << fact(val) << endl;
}