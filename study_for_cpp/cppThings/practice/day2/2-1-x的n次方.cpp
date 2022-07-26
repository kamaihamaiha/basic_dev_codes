#include <iostream>

using namespace std;
int power(int x, int n);

int main(){
  cout << "请输入一个整数:";
  int x;
  cin >> x;

  cout << "请输入次方数:";
  int n;
  cin >> n;

  int val = power(x, n);

  cout << x << "^" << n << "=" << val << endl;

  return 0;
}

/**
 * x 的 n 次方
 * @return
 */
int power(int x, int n) {
  int value = 1;
  while (n--) {
    value *= x;
  }
  return value;
}