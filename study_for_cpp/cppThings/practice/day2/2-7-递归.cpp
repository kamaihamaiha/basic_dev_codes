#include <iostream>

using namespace std;

int add(int x);

int main(){
  int x;
  cout << "Please input a num:";
  cin >> x;

  int value = add(x);
  cout << "value: " << value << endl;
  return 0;
}
/**
 * 求 1 ~ X 之间的值的总和
 * @param x
 * @return
 */
int add(int x) {
  if (x > 0) return x + add(x - 1);
  return 0;
}