#pragma
#include "student.h"
#include <iostream>

using namespace std;

void Student::setGender(bool isMale) {
    male = isMale;
}

void Student::printInfo() {
    cout << "student name: " << name << endl;
    cout << "student born: " << born << endl;
    cout << "student gender: " << (male ? "male" : "femail") << endl;
}