#include <iostream>

using namespace std;

class Animal {
 private:
  int weight;

 public:
  Animal(int w):weight(w) {
    cout << "Animal::Animal()" << endl;
  }

  ~Animal(){
    cout << "~Animal::Animal()" << endl;
  }

  void print(){
    cout << "Animal::f()" << weight << endl;
  }
  void set(int w) {
    weight = w;
  }

  void hello(){
    cout << "Animal::hello()" << endl;
  }
  void hello(string msg){
    cout << "Animal::hello(msg)" << endl;
  }
};

class Kitty : public Animal {
 public:
  Kitty(): Animal(16) {
    cout << "Kitty::Kitty()" << endl;
  }
  ~Kitty() {
    cout << "Kitty::~Kitty()" << endl;
  }
  void f() {
    set(10);
    print();
  }
  void hello(){
    cout << "Kitty::hello()" << endl;
  }
};

int main(){

  Kitty k;
  k.f();
  k.hello();

  return 0;
}