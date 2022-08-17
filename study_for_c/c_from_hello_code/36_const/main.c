#include <stdio.h>

void demo1();
void demo2();

int main(){

  demo2();
  return 0;
}

void demo1() {
  char const str[] = "Hello\n";
  puts(str);

  // str 为 const，不能修改，这么写会报错
  str[0] = 'h';
  puts(str);
}

// const 修饰指针指向数据
void demo2(){
  const char *pstr = "hello\n"; // 加上 const 修饰，在编译时就会报错
  pstr[0] = 'H';
  puts(pstr);
}