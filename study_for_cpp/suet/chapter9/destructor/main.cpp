#include <iostream>

using namespace std;

class Student {
private:
    const char* name;
    int born;
    bool male;

public:
    Student(){
        name = "unknown";
        cout << name << ": Student(const char* _name)" << endl;
    };

    Student(const char* _name):born(1999), male(true){
        name = _name;
        cout << name << ": Student(const char* _name)" << endl;
    }

    ~Student(){
        cout << name << ": ~Student()" << endl;
    }
};

int main(){

    {
        Student stu1;
        Student stu2("宋江");
        Student stu3 = Student("晁盖");
    }
    Student *stu4 = new Student("林冲");

    Student *stus = new Student[3]{
            {Student()}, {Student("孙悟空")}, {Student("猪八戒")}
    };

    delete stu4;
    delete[] stus;
    return 0;
}