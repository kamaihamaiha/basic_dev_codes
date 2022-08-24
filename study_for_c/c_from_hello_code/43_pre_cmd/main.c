#include <stdio.h>

#define PRICE 3

// 定义宏函数
// 改良前
#define SQUARE(x) x*x
// 改良后
#define SQUARE2(x) ((x)*(x))

#define HELLO(love) "I " love " You"
#define HELLO2(love) "I " #love " You"

int getTotal(int);

int main(){

  getTotal(1);
  getTotal(2);
  getTotal(3);

  // 调用宏函数
  int n = 2;
  printf("%d\n", SQUARE(n));        // 展开：n * n = 2 * 2 = 4
  printf("%d\n", SQUARE(n + 2)); // 展开：n + 2 * n + 2 = 2 + 2 * 2 + 2 = 8; 而不是预期的 16
  printf("%d\n", 100 / SQUARE(n));  // 展开：100 / 2 * 2 = 100; 而不是预期的 25
//  printf("%d\n", SQUARE(++n));   // 展开：++n * ++n 这样的表达式结果不确定

  printf("%d\n", SQUARE2(n));
  printf("%d\n", SQUARE2(n + 2));
  printf("%d\n", 100 / SQUARE2(n));

  // 调用宏 HELLO
  printf("%s\n", HELLO("love"));
  printf("%s\n", HELLO2("love"));
  return 0;
}

int getTotal(int count) {
  int ret = count * PRICE;
  printf("num: %d total: %d\n", count, ret);
  return ret;
}