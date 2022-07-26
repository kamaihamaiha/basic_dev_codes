#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

  string str("hello");
  if (str.begin() != str.end()) {   // 第一个字符改为大写
    auto it = str.begin();
    *it = toupper(*it);
  }
  cout << str << endl;

  // 把所有字母改为大写
  string str1("hello");
  for(auto it = str1.begin(); it != str1.end() && !isspace(*it); ++it) {
    *it = toupper(*it);
  }
  cout << str1 << endl;

  // 练习3.16
  vector<int> v1;
  vector<int> v2(10);
  vector<int> v3(10, 42);
  vector<int> v4{10};
  vector<int> v5{10, 42};
  vector<string> v6{10};
  vector<string> v7{10, "hi"};

  cout << "v1 size: " << v1.size() << endl;
  for(auto v: v1) {
    cout << v << ",";
  }
  cout << endl << "v2 size: " << v2.size() << endl;
  for(auto v: v2) {
    cout << v << ",";
  }
  cout << endl << "v3 size: " << v3.size() << endl;
  for(auto v: v3) {
    cout << v << ",";
  }
  cout << endl << "v4 size: " << v4.size() << endl;
  for(auto v: v4) {
    cout << v << ",";
  }
  cout << endl << "v5 size: " << v5.size() << endl;
  for(auto v: v5) {
    cout << v << ",";
  }
  cout << endl << "v6 size: " << v6.size() << endl;
  for(auto v: v6) {
    cout << v << ",";
  }
  cout << endl << "v7 size: " << v7.size() << endl;
  for(auto v: v7) {
    cout << v << ",";
  }

  // 练习3.23
  vector<int> nums = {1,2,3,4,5,6,7,8,9,10};
  for (auto it = nums.begin(); it != nums.end(); ++it) {
    *it = *it * 2;
  }
  for (auto num: nums) {
//    cout << num << endl;
  }

  return 0;
}