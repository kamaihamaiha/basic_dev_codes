#include <iostream>
#include <string>

using namespace std;

// 成员访问运算符
int main(){

  string s1 = "hello";
  string *p = &s1;

  auto n = s1.size();
  n = (*p).size();
  n = p->size();



  return 0;
}