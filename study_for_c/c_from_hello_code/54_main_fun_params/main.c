#include <stdio.h>

int main(int argc, char **argv) {

  printf("参数个数: %d\n", argc);

  // 输出每个参数
  for (int i = 0; i < argc; ++i) {
    printf("%s\n", argv[i]);
  }
  return 0;
}