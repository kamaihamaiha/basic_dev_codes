#include <iostream>
#include "Sales_data.h"

int main(){

  double price = 0;
  Sales_data data1, data2;

  std::cout << "请输入第一本书的交易信息，ISBN、销售数量、单价：" << std::endl;
  std::cin >> data1.bookNo >> data1.units_sold >> price;
  data1.sum = data1.units_sold * price;

  std::cout << "请输入第二本书的交易信息，ISBN、销售数量、单价：" << std::endl;
  std::cin >> data2.bookNo >> data2.units_sold >> price;
  data2.sum = data2.units_sold * price;

  // 输出两个对象的和
  if (data1.bookNo == data2.bookNo) {
    double total_sum = data1.sum + data2.sum;
    unsigned total_units_sold = data1.units_sold + data2.units_sold;
    std::cout << "总交易细信息，ISBN：" << data1.bookNo << ", 售出：" << total_units_sold << "本，共收入："
    << total_sum << "$" << std::endl;
  } else {
    std::cerr << "ISBN 必须相同！" << std::endl;
    return -1;
  }

  return 0;
}