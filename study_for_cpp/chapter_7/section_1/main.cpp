#include <iostream>

using namespace std;


struct Sales_data {

  // 新成员，一些操作. 这里的 const 是为了修改隐式 this 指针的类型
  std::string isbn() const {
    return bookNo;
  };

  Sales_data &combine(const Sales_data&);

  double avg_price() const;
  
  // 之前定义好的数据成员,参照：doc/chapter_2/section_6.md
  std::string bookNo;
  unsigned units_sold = 0;
  double sum = 0.0;
};

int main(){


  return 0;
}