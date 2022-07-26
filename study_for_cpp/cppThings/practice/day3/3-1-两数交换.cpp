#include <iostream>

using namespace std;

void swap(int &a, int &b);

int main(){
  int x = 1, y = 2;
  int &a = x;
  int &b = y;

  ::swap(a, b);

  cout << "a: " << a << ", b: " << b << endl;

  return 0;
}

void swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}