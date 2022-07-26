#include <iostream>
#include "../section_5/Sales_item.h"

int main(){

  Sales_item sales_sum;
  Sales_item cur_sales;

  // 先读取第一条
  if (std::cin >> sales_sum) {
    while (std::cin >> cur_sales) {
      if (sales_sum.isbn() == cur_sales.isbn()) {
        sales_sum += cur_sales;
      } else {
        // 打印前一本的结果，然后重新累计
        std::cout << sales_sum << std::endl;
        sales_sum = cur_sales;
      }
    }
    // 打印最后一本书的结果
    std::cout << sales_sum << std::endl;
  } else {
    std::cerr << "输入错误!" << std::endl;
    return -1;
  }
  return 0;
}
