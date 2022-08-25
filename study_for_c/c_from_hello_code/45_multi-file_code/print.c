#include <stdio.h>
#include "print.h"

// 实现 print

void print(const char *str){
  while (*str != '\0') {
    putchar(*str);
    str++;
  }
}