#include <iostream>

using namespace std;

class Person {
 public:
  Person(): age(0), name("人"){
    cout << "Person::Person()" << endl;
  }
  ~Person(){
    cout << "~Person::Person()" << endl;
  }

  void print() {
    cout << "A::fun() name: " << name << ", age: " << age << endl;
  }

  void setAge(int age) {
    this->age = age;
  }
 private:
  int age;
  string name;
};

class Male: public Person {

 public:
  void f(){
    setAge(100);
    print();
  }
};

int main() {
  Male m;
  m.setAge(99);
  m.print();

  m.f();

  return 0;
}