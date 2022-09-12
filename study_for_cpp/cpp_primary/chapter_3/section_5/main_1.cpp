#include <iostream>
#include <string>

using namespace std;

// 数组：定义和初始化
int main(){

  int arr1[10];     // 含有 10 个整数的数组
  int *arr2[10];    // 含有 10 个整型指针的数组

  // 显示初始化数组元素
  int a1[3] = {1, 2, 3};
  int a2[] = {1, 2, 3};
  int a3[5] = {1, 2, 3};          // 等价于 a3[5] = {1, 2, 3, 0, 0};
  string a4[3] = {"hi", "hell"};  // 等价于 a4[3] = {"hi", "hell"， ""};

  // 字符数组的特殊性
  char ca1[] = {'a', 'b', 'c'};       // 实际有 4 个字符，末尾有个空字符
  char ca2[] = {'a', 'b', 'c', '\0'}; // 显式的空字符：\0
  char ca3[] = "cpp";                 // 实际有 4 个字符，末尾有个空字符
//  char ca4[5] = "hello";              // error: 没有空间存放空字符了


  return 0;
}