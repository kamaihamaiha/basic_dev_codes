#include <iostream>
#include <string>
#include <iterator>

using namespace std;

int main(){

  string nums[] = {"one", "two", "three"};
  string *p = &nums[0];     // p 指向 nums 的第一个元素
  string *p2 = nums;        // 等价于上面。

  // begin 和 end 函数
  int ia[] = {1,2,3};
  int *beg = begin(ia); // 指向首元素的指针
  int *last = end(ia);  // 指向尾元素下一个地址的指针

  // 指针运算
  constexpr size_t sz = 5;
  int iar[sz] = {1, 2, 3, 4, 5};
  int *p3 = iar;          // p3 指向 iar[0]
  int *p4 = p3 + 4;       // p4 指向 iar[4]
  int *p5 = iar + 1;      // p5 指向 iar[1]

  // 指针相减. n 的类型为：ptrdiff_t
  auto n = end(iar) - begin(iar);

  // 指针比较
  int *b = iar, *e = iar + sz;
  while (b < e) {
    ++b;
  }

  // 解引用和指针运算的交互
  int iar2[] = {1,2,3,4};
  int last2 = *(iar2 + 3);   // 把 last 初始化为 iar2[3]，也就是 4
  int last3 = *iar2 + 3;     // 等价于 last3 = iar2[0] + 3

  // 下标和指针
  int iar3[] = {1,2,3,4,5};
  int *p6 = iar3;
  int i = *(p6 + 2);    // 等价于 i = iar3[2]
  int *p7 = &iar3[2];   // p7 指向 iar3[2] 元素
  int j = p7[1];        // j 的值就是 iar3[3] 元素的值
  int k = p7[-2];       // k 的值就是 iar3[0] 元素的值

  return 0;
}