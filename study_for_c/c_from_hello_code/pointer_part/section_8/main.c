#include <stdio.h>

int print(char *);

void funA();
void funB();
void funC();
void funD();

int main(){

  // 1. 声明函数指针，并指向函数 print
  int (*p)(char *) = print;

  // 调用函数：(*p) 对指针（函数指针）取值，得到函数，相当于是 print(char *)
  (*p)("Hello");

  // 也可以这么写
  p("Hello!");


  // 2. 函数指针数组
  void (*funArray[4])() = {funA, funB, funC, funD};
  for (int i = 0; i < sizeof(funArray); ++i) {
    funArray[i](); //  调用函数
  }
  return 0;
}

int print(char *pc) {
  int count = 0;
  while (*pc != '\0') {
    putchar(*pc);
    pc++;
    count++;
  }
  putchar('\n');

  return count;
}

void funA(){
  print("a");
}
void funB(){
  print("b");
}
void funC(){
  print("c");
}
void funD(){
  print("d");
}