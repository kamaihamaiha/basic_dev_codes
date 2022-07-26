#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  // 例题：整数 1-9 求平方
  vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9};
  for (auto &value : v) {
    value *= value;
  }
  // 输出新的值
  for(auto value : v) {
    cout << value << endl;
  }

  // 例题： 统计分数段，10 分一个阶段
  vector<unsigned> scores (11, 0); // 11 个分数段(0, 1, 2, ... 10) 0 代表 0-9 分，10 代表 100分
  unsigned score;
  while (cin >> score) {    // 读取分数
    if (score <= 100) {     // 满分 100 分
      if (score == 0) break;
      ++scores[score / 10]; // 当前分数段加1
    }
  }
  for (auto value : scores) {
    cout << value << ",";
  }
  cout << endl;
  return 0;
}