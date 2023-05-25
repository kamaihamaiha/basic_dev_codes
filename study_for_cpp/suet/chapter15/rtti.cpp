#include <iostream>
#include <stdio.h>

using namespace std;

class Person {
protected:
    string name;

public:
    Person(string name = ""): name(name){}
    ~Person(){}

    virtual string getInfo(){
        return name;
    }

};

class Student: public Person{
private:
    string studentId;

public:
    Student(string name = "", string studentId = ""): Person(name), studentId(studentId){

    }
    ~Student(){};

    string getInfo(){
        return name + ": " + studentId;
    }
};

int main(){

    Person p = Person("kk");
    Student s = Student("zkx", "123");

    Person *pp = &s;
    Person &pr = s;

    Student *sp = (Student*) &p; // danger!

    cout << "s info: " << s.getInfo() << endl;
    cout << "pp info: " << pp->getInfo() << endl;
    cout << "sp info: " << sp->getInfo() << endl;

    // dynamic_cast
    sp = dynamic_cast<Student*>(&p); // safe
    pp = dynamic_cast<Person*>(&s);

    ::printf("address of sp: %p\n", sp); // 因为 Person 要转成 Student，实际上地址就是 NULL
    ::printf("address of pp: %p\n", pp);

    return 0;
}