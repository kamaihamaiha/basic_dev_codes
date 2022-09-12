#include <iostream>
#include <string>
#include <cctype>

using std::cin; using std::cout; using std::endl; using std::string;
int main(){

  string e;
  cout << e[0] << endl;

  // 遍历
  string str("abcd");
  for(char c : str) {
    cout << c << " 是否为标点符号：" << ispunct(c) << endl;
  }

  // 把字符都改成大写
  for(auto &c : str) {
    c = toupper(c);
  }
  cout << str << endl;

  // 只处理一部分字符：把第一个字符改为大写
  if (str.size() > 0) {
    str[0] = toupper(str[0]);
  }
  cout << str << endl;

  // 使用下标执行随机访问: 把输入的 0-15 之间的十进制数转换成十六进制数
  const string hex_str = "0123456789ABCDEF";
  cout << "输入任意数字(0 - 15)之间的，输入 -1 结束" << endl;
  string res;
  string::size_type num;
  while (cin >> num ) {
    if (num == -1) break;
    res += hex_str[num];
  }
  cout << "十六进制数：" << res << endl;
  return 0;
}

