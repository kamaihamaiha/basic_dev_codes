#include <iostream>

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

    string s("kk");

    cout << "typeid.name of s is: " << typeid(s).name() << endl;
    cout << "typeid.name of s std::string: " << typeid(std::string).name() << endl;
    cout << "typeid.name of s Student: " << typeid(Student).name() << endl;

    if (typeid(s) == typeid(std::string)){
        cout << "s is a std::string object." << endl;
    }
}