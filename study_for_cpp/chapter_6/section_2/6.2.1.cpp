#include <iostream>

using namespace std;

void swapValue(int *va, int *vb);

int main(){

  int x = 1, y = 2;
  int *p = &x, *q = &y;
  swapValue(p, q);

  cout << "*p: " << *p << ", *q: " << *q << endl;
  return 0;
}

void swapValue(int *va, int *vb){
  int temp = *va;
  *va = *vb;
  *vb = temp;

  cout << "*va: " << *va << ", *vb: " << *vb << endl;
}