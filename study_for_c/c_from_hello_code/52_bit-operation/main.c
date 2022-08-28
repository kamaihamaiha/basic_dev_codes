#include <stdio.h>

// 十进制转二进制
void printBinary(unsigned char dec);

int main(){

 /* for (int i = 0; i < 16; ++i) {
    printBinary(i);
  }*/

  char c1 = 170;
  char c2 = 102;
  printBinary(c1);
  printBinary(c2);
  printf("%hhu\n", c1 & c2);
  printBinary(c1 & c2);
  return 0;
}

void printBinary(unsigned char dec) {
  char bits[8] = {0};
  int count = 0;
  int quotient;  // 除数
  int remainder; // 余数

  while (dec > 0) {
    quotient = dec / 2;
    remainder = dec % 2;
    bits[sizeof(bits) - (++count)] = remainder;

    dec = quotient;
  }

  // print
  for (int i = 0; i < sizeof(bits); ++i) {
    printf("%d", bits[i]);
  }
  printf("\n");
}