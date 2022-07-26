#include <iostream>
#include <string>
#include <vector>

using namespace std;
using std::vector;

// 4.6 节练习
int main (){

  vector<string> vs = {"hello", "he"};

  auto iter = vs.begin();
  *iter++;


  return 0;
}