#include <iostream>
#include <string>

using namespace std;

class Person {
public:
    string name;

    Person(string n): name(n){}

    virtual void print(){
        cout << "Name: " << name << endl;
    }
};

class Student: public Person {
public:
    string id;

    Student(string n, string i): Person(n), id(i){}
    void print(){
        cout << "Name: " << name;
        cout << ". ID: " << id << endl;
    }
};

class Person2 {
public:
    string name;

    Person2(string n): name(n){}

    virtual void print() = 0; // 纯虚函数，没有函数体。因此 Person2 使用时不要创建对象，仅仅用来作为继承使用
};

void printObjectInfo(Person &p){
    p.print();
}

int main(){

    {
        Student stu("zhang", "2023");
        printObjectInfo(stu);
    }

    {
        Person *p = new Student("li", "2023");
        p->print();
        delete p;
    }

    return 0;
}