#include <iostream>
using namespace std;

union MyUN {
  struct {
    int x, y, z;
  } u;
  int k;
} un;
int main(){

  un.u.x = 1;
  un.u.y = 2;
  un.u.z = 3;
  un.k = 9; // 会覆盖掉 un.u.x 的值

  printf("%d %d %d %d\n", un.u.x, un.u.y, un.u.z, un.k);
  return 0;
}