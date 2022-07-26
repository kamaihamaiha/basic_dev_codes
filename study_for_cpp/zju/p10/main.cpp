#include <iostream>

using namespace std;

struct X {
  int i;
  float f;
  char c;
};

struct Y {
  float f;
  int i;
  Y(int a);
  Y();
};

int main(){

  // 结构体 X 数组，初始化
  X x_arr[3] = {{1, 1.0f, '1'}, {2, 2.0f, '2'}, {3, 3.0f, '3'}};

  // 结构体 Y 数组，初始化
  Y y_arr[2] = {
      Y(1)
  };

  cout << "y f: " << y_arr[1].f << endl;
  return 0;
}