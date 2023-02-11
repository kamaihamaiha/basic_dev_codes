#include <iostream>
#include <stdio.h>

using namespace std;

struct Student {
    char name[4];
    int born;
    bool male;
};

void showInfo(Student* stu);

int main(){

    Student stu = {"kk", 2000, true};
    Student *pStu = &stu;

    showInfo(pStu);
    // change stu member content
    pStu->born = 1991;
    strncpy(pStu->name, "Ki", 4);
    showInfo(pStu);

    // print out the addresses
    printf("Address of stu: %p\n", pStu);  // C style
    cout << "Address of stu: " << pStu << endl; // C++ style
    cout << "Address of member name: " << &(pStu->name) << endl;
    cout << "Address of member born: " << &(pStu->born) << endl;
    cout << "Address of member male: " << &(pStu->male) << endl;
    cout << "sizeof(pStu): " << sizeof(pStu) << endl;

    return 0;
}

void showInfo(Student* stu){
    cout << stu->name << " was born in " << (*stu).born << ". Gender: " << (stu->male ? "male" : "female") << endl;
}