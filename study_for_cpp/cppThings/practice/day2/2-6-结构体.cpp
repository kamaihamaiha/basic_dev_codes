#include <iostream>

using namespace std;

struct Student {
  int age;
  char name[20];
  char gender;
};

int main(){
  Student student = {13, "二师兄", 'M'};

  cout << "name: " << student.name << ", age: " << student.age << ", 性别: " << student.gender << endl;
  return 0;
}