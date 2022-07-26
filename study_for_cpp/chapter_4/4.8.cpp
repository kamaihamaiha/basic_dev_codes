#include <iostream>
#include <bitset>

using namespace std;
// 4.8 节练习
int main(){

  // 'q' << 6
  char c = 'q';
  int v = c;
  auto v_move = c << 6;

  cout << "char value: " << c << endl;
  cout << "char value(8位二进制表示): " << bitset<8>(c)<< endl;
  cout << "int value: " << v << endl;
  cout << "int v_move value: " << v_move << endl;
  cout << "int value(十进制): " << dec << v << endl;
  cout << "int value(八进制): " << oct << v << endl;
  cout << "int value(十六进制): " << hex << v << endl;
  cout << "int value(二进制): " << bitset<32>(v)<< endl;
  cout << "int v_move value(二进制): " << bitset<32>(v_move)<< endl;

  // 4.27 练习
  unsigned long u1 = 3, u2 = 7;
  cout << "u1 & u2 = " << (u1 & u2) << endl;
  cout << "u1 | u2 = " << (u1 | u2) << endl;
  // 注意：下面 2 个都是逻辑运算，不是位运算
  cout << "u1 && u2 = " << (u1 && u2) << endl;
  cout << "u1 || u2 = " << (u1 || u2) << endl;
  return 0;
}