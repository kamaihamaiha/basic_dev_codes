#include <stdio.h>

void convertCap();
void convertCap2();

// 反转字符串
void revertStr(char*);

int main(){

  // 定义字符指针
  char *str = "Hello!\n";

  // 定义字符数组
  char str2[] = "Hello\n";
  printf("%s", str);
  printf("%s", str2);

  // 通过字符数组，修改第一个字符
  str2[0] = 'h';
  printf("%s", str2);

  // 转化成大写
//  convertCap();
//  convertCap2();

  char str3[] = "hello";
  revertStr(str3);

  return 0;
}

void convertCap() {
  char str[] = "hello";
  for (int i = 0; i < sizeof(str); ++i) {
    if (str[i] != 0) { // 或者写成 str[i] != '\0'
      str[i] -= 32;
    }
  }
  printf("%s\n", str);
}

void convertCap2(){
  char str[] = "hello";
  char *p = str;
  while (*p) { // 或者写成 *p != 0 或者 *p != '\0'
    *p -= 32;
    p++;
  }

  puts(str);
}

void revertStr(char *str) {
  char *pHead = str;
  char *pTail = str;

  // 交换前
  printf("交换前：%s\n", str);

  // pTail 移动到最后一个字符
  while (*pTail) {
    pTail++;
  }
  pTail--;

  // 开始交换
  while (pHead <= pTail) {
    char temp = *pHead;
    *pHead = *pTail;
    *pTail = temp;

    // 交换完，分别移动
    pHead++;
    pTail--;
  }

  printf("交换后：%s\n", str);

}