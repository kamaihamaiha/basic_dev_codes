#include <iostream>

using namespace std;


int main(){

    int value1 = 100;
    const int value2 = 200;

    int *pv1 = const_cast<int *> (&value1);

    // const int 取它的指针，使用 const_cast 把 const 特性去掉
    int *pv2 = const_cast<int *> (&value2);

    // 也可以用引用方式把 const 去掉. 但是还是不能修改 value2 的值
    int& vr = const_cast<int &> (value2);
    vr++;
    cout << "vr: " << vr << endl;
    cout << "value2: " << value2 << endl;

    int *P1 = &value1;
    const int *p2 = &value2;

    (*pv1)++;
    (*pv2)++;

    cout << "value1: " << value1 << endl; // 101
    cout << "value2: " << value2 << endl; // 200
    cout << "*pv2: " << *pv2 << endl; // 202
    cout << "vr: " << vr << endl; // 202

    return 0;
}