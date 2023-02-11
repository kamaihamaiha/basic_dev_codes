#include <iostream>

using namespace std;
struct Student {
    char name[6];
    int born;
    bool male;
};
int main(){

    // allocate an int, default initializer(do nothing)
    int *p1 = new int;

    // allocate an int, initialized to 0
    int *p2 = new int();

    // allocate an int, initialized to 4
    int *p3 = new int(4);

    // allocate an int, initialized to 0
    int *P4 = new int{}; // C++11

    // allocate an int, initialized to 5
    int *p5 = new int{5}; // C++11

    // allocate a Student object, default initializer
    Student *pStu1 = new Student;

    // allocate a Student object, initialize the members
    Student *pStu2 = new Student{"Zhang", 2000, true}; // C++11

    // 下面的是 new[] 使用

    // allocate 16 int, default initializer(do nothing)
    int *pa1 = new int[16];

    // allocate 16 int, zero initialized
    int *pa2 = new int[16]();

    // allocate 16 int, zero initialized
    int *pa3 = new int[16]{}; //C++11

    // allocate 16 int, the first 3 elements are initialized to 1,2,3, the reset 0
    int *pa4 = new int[16]{1, 2, 3}; //C++11

    // allocate memory for 16 Student objects, default initialized
    Student *pStus1 = new Student[16];

    // allocate memory for 16 Student objects, the first two are initialized
    Student *pStus2 = new Student[16]{
            {"A", 2000, true},
            {"B", 2001, false}
    };
    return 0;
}