#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

  // 练习 3.14
  vector<int> vi;
  int num;

  cout << "输入数字，按下 -1 结束:" << endl;
  while (cin >> num) {
    if (num == -1) break;
    vi.push_back(num);
  }
  cout << "size: " << vi.size() << endl;

  // 练习 3.15
  vector<string> vs;
  string str;
  while (cin >> str) {
    vs.push_back(str);
  }
  cout << "vs size: " << vs.size() << endl;
  return 0;
}