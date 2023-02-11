#include <iostream>

using namespace std;
// 指针的指针
int main(){

    int num = 10;
    int *p = &num;
    int **pp = &p;

    **pp = 20;

    cout << "num: " << num << endl;

    return 0;
}