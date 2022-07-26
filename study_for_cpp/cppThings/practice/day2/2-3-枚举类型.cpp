#include <iostream>

using namespace std;

enum Weekday {
  Mon, Tue, Wed, Thu, Fri, Sat, Sun
};

int main(){
  enum Weekday today = Mon;
  for (int i = today; i <= Sun; ++i) {
    cout << "i: " << i << endl;
  }
  return 0;
}