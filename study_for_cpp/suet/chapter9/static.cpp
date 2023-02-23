#include <iostream>

using namespace std;

class Student {
private:
    const char* name;
    int born;
    // 声明
    static int total_count; // C++17 可以直接在前面加上 inline，就不需要在外部定义了

public:
    Student(){
        total_count++;
    };

    Student(const char* _name):born(1999){
        this->name = _name;
        total_count++;
    }

    ~Student(){
        total_count--;
    }

    int getBorn() const {
        return born;
    }


    static int getTotalCount(){
        return total_count;
    }
};

// 定义
int Student::total_count = 0;

int main(){

    Student st1;
    Student st2("纣王");
    Student st3 = Student("周文王");
    Student *st4 = new Student("姜子牙");

    cout << "stu num: " << Student::getTotalCount() << endl;

    delete st4;
    cout << "stu num: " << Student::getTotalCount() << endl;

    return 0;
}