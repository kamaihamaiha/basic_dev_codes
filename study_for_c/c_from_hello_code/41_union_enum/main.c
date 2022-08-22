#include <stdio.h>

enum MsgType
struct Message{
  enum MsgType type;
  union {
    int n;
    float f;
    char *str;
  };
};


// union 用法举例
void demo_union(struct Message msg);

// 枚举
enum Car {
  BYD = 100, // 从 100 开始
  BMW,
  Audio,
  Toyota
};

enum MsgType {
  eInteger,
  eFloat,
  eChar
};

int main(){

  // 结构
  struct {
    char c;       // 1 Byte
    short s;      // 2 Byte
    long long ll; // 8 Byte
  }s;             // total: 16 Byte 因为有「内存对齐」

  // 联合：共用一块内存空间
  union {
    char c;       // 1 Byte
    short s;      // 2 Byte
    long long ll; // 8 Byte
  }u;             // total: 8 Byte. 联合的 size 就是成员中最大的成员的 size，值会覆盖其他的成员

  // 分别打印 struct 和 union 的 size
  printf("size of struct s: %d\n", sizeof(s));
  printf("size of union u: %d\n", sizeof(u));

  struct Message msg;
  msg.type = eInteger;
  msg.n = 99;

  demo_union(msg);

  // 打印枚举的值
  printf("Car BYD: %d\n", BYD);
  printf("Car Audio: %d\n", Audio);
  return 0;
}

void demo_union(struct Message msg) {
  switch (msg.type) {
    case eInteger:
      printf("%d\n", msg.n);
      break;
    case eFloat:
      printf("%f\n", msg.f);
      break;
    case eChar:
      printf("%s\n", msg.str);
      break;
  }
}