#include <iostream>
#include <string>
#include <cstddef>

using namespace std;

// 3.5.3 节练习
int main(){

  int iarr[] = {1,2,3,4,5};
  int *beg = iarr;
  int *end_arr = end(iarr);

  while (beg < end_arr) {
    *beg = 0;
    ++beg;
  }

  // 遍历查看
  for(auto v : iarr) {
    cout << v << ",";
  }
}