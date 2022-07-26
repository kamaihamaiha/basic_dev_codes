#include <iostream>

using namespace std;
int fact(int val);
int factWithInput();
int abs(int val);

int main(){

  int value = -6;

//  int ret  = factWithInput();

  cout << value << " 的绝对值：" << abs(value);
  return 0;
}

/**
 * 求阶乘
 * @param val
 * @return
 */
int fact(int val) {
  int ret = 1;
  while (val > 1) {
    ret *= val--;
  }
  return ret;
}

int factWithInput(){
  cout << "请输入一个数：" << endl;
  int val;
  std::cin >> val;

  int ret = fact(val);
  cout << val << " 的阶乘：" << ret;
  return fact(val);
}

/**
 * 求绝对值
 * @param val
 * @return
 */
int abs(int val) {
  if (val >= 0) return val;
  return val * -1;
}