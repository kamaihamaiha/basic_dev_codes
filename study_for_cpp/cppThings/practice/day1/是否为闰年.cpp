#include <iostream>

using namespace std;

int main(){
  int year;
  bool isLeapYear;

  cout << "Enter the year: ";
  cin >> year;

  isLeapYear = ( (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 );

  cout << (isLeapYear ? "是" : "不是") << "闰年" << endl;
  return 0;
}