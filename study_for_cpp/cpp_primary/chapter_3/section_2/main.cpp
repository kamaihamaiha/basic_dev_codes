#include <iostream>
#include <string>

using std::cin; using std::cout; using std::endl; using std::string;

int main(){

  // region 空字符串
  string s;
  // 从输入中读取字符串到 s
  cin >> s;
  // 输出
  cout << s << endl;

  // endregion

  // region 读取数不定的 string 对象
  string word;
  cout << "请输入任意内容：" << endl;
  /*while (cin >> word) {
    cout << word << endl;
    cout << "继续输入：" << endl;
  }*/
  // endregion

  // region getline() 读取一整行
  string line;
  cout << "读取一整行,请输入任意内容：" << endl;
  while (getline(cin, line)) {
    if (!line.empty()) { // 判断，不是空行才输出
      if (line.size() >= 3) { // 一行的长度超过 3 才输出
        cout << line << endl;
      }
    }
  }
  // endregion
  string a = "a";
  string as = "1" + ("2" + a);
  return 0;
}