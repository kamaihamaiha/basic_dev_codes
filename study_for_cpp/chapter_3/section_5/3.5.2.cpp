#include <iostream>
#include <string>
#include <cstddef>

using namespace std;

// 3.5.2 节练习
int main(){

  constexpr size_t size = 10;
  int ia[size] = {};

  for (size_t i = 0; i < size; ++i) {
    ia[i] = i;
  }

  for (auto v : ia) {
    cout << v << ",";
  }
  return 0;
}