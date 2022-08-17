#include <stdio.h>
#include <string.h>

// strlen()
void demo1(){
  const char *str = "Hello";
  printf("str的长度：%lu\n", strlen(str));
}

// strcat()
void demo2(){
  // 申请9个空间，给拼接后的空间
  char dest[9] = "ILove";
  char src[] = "You";

  puts(dest);
  puts(src);

  strcat(dest, src);
  printf("%s\n", dest);
}

// strcpy
void demo3(){
  char des[12] = "Hello";
  const char *src = "World";

  strcpy(des, src);
  puts(des);
  puts(src);
}

// strcmp: 如果一致，返回 0
void demo4(){
  char *str1 = "a";
  char *str2 = "b";

  printf("比较结果：%d\n", strcmp(str1, str1));
  printf("比较结果：%d\n", strcmp(str1, str2));
}

int main(){

//  demo1();
//  demo2();
//  demo3();
  demo4();

  return 0;
}