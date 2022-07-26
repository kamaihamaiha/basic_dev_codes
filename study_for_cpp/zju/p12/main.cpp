#include <iostream>
#include <string>

using namespace std;

class Human {
 private:
  string name;

 public:
  Human(){}
  ~Human(){}

  void setName(string name) {
    this->name = name;
  }

  void hello(Human *human){
    // 访问别人的私有字段
    cout << "other name: " << human->name << endl;
  }
};


struct X;

struct Y {
  void f(X*); // 注意这里的参数必须是指针类型，如果是 X，此时还找不到 X 不知道 X 是什么
};

struct X {
 private:
  int i;

 public:
  void init();
  friend void g(X*, int);   // Global friend
  friend void Y::f(X *);    // Struct member friend, 授权 Y 的 f() 函数对 X 有访问权限
  friend struct Z;          // Entire struct is a friend。对整个类 Z 来说，X 都是 Z 的朋友
  friend void h();
};

// 下面是定义上面 X 中声明的方法

void X::init() {
  i = 1;
}

void g(X* x, int i) {
  x->i = i;
}

void Y::f(X *x) {
  x->i = 2;
}



int main(){

  // h1 对象可以通过 h2对象访问别人的 private 字段
  Human h1;
  Human h2;
  h2.setName("Bush");
  h1.hello(&h2);

  // 调用 Friend 函数


  return 0;
}