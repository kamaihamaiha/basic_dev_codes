#include <iostream>
#include <string>
#include <cstring>

using namespace std;

// 3.5.4 节练习
int main(){

  const char c1[] = {'h', 'e', 'l', 'l', '0', '\0'};
  const char c2[] = {'h', 'e', 'l', 'l', '0', '\0'};
  const char *cp = c1;
  while (*cp) {
    cout << *cp << ",";
    ++cp;
  }
  cout << endl;

  // 比较大小
  const char c3[] = "Hello";
  const char c4[] = "Hello";
  int res = strcmp(c3, c4);
  if (res == 0) {
    cout << "c3 = c4" << endl;
  } else if (res < 0) {
    cout << "c3 < c4" << endl;
  } else {
    cout << "c3 > c4" << endl;
  }

  // 连接字符串
  char c5[] = "c5";
  const char c6[] = "c6";
  size_t size = strlen(c5) + strlen(c6);
  char c7[size];
  strcpy(c7, strcat(c5, c6));

  char *p7 = c7;
  while (*p7) {
    cout << *p7 << ",";
    p7+=1;
  }
  return 0;
}