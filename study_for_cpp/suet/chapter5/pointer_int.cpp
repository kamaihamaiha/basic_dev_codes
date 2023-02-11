#include <iostream>

using namespace std;

void show(int*, int*, int);
// 指针，简单的 int*
int main(){

    int num = 10;
    int *p1 = NULL, *p2 = NULL;

    p1 = &num;
    p2 = &num;

    show(p1, p2, num);

    cout << "change num value is 99:" << endl;
    *p1 = 99;

    show(p1, p2, num);


    return 0;
}

void show(int* p1, int* p2, int num){
    cout << "p1: " << p1 << ", content: " << *p1 << endl;
    cout << "p2: " << p2 << ", content: " << *p2 << endl;
    cout << "num: " << num << endl;
}