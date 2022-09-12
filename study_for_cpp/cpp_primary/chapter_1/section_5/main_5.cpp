#include "Sales_item.h"
#include <iostream>


int main (){

  Sales_item book;
//   读入 ISBN 号、售出的册数以及销售价格
  std::cin >> book;

  // 输出
  std::cout << book << std::endl;

  // 2 个对象相加
  Sales_item book1, book2;
  std::cin >> book1 >> book2;
  std::cout << book1 + book2 << std::endl;

  // 练习 1.20 读取一组书籍到销售记录，将每条记录打印到标准输出上
  while (std::cin >> book) {
    // print
    std::cout << "isbn: " << book.isbn() << ", price: " << book.avg_price() << std::endl;
  }

  // 练习 1.21 读取两个 ISBN 相同的 Sales_item 对象，输入他们的和
  Sales_item sale1, sale2;
  std::cin >> sale1 >> sale2;
  if (sale1.isbn() == sale2.isbn()) {
    std::cout << sale1 + sale2 << std::endl;
  } else {
    std::cerr << "ISBN 必须相同！" << std::endl;
  }

  // 练习 1.22 读取多个具有相同 ISBN 的销售记录，输入所有记录的和
  Sales_item sales_sum;
  Sales_item cur_sale;

  while (std::cin >> cur_sale) {
    if (sales_sum.isbn() != cur_sale.isbn()) {
      sales_sum = cur_sale;
    } else {
      sales_sum = sales_sum + cur_sale;
    }
  }
  std::cout << sales_sum << std::endl;

  // 练习 1.23 读取多条销售记录，并统计每个 ISBN（每本书）有几条销售记录
  int count = 0;
  int loop = 0;
  Sales_item curr_sale;
  Sales_item tem_scle;
  while (std::cin >> curr_sale) {
    if (tem_scle.isbn() != curr_sale.isbn()) {
      if (loop != 0) {
        // 统计
        std::cout << tem_scle.isbn() << " 数量：" << count << std::endl;
      }
      tem_scle = curr_sale;
      count = 1;
    } else {
      count++;
    }
    loop++;
  }
  // 都是一种书
  std::cout << tem_scle.isbn() << " 数量：" << count << std::endl;
  return 0;
}
