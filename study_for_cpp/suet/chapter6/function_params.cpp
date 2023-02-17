#include <iostream>

using namespace std;

int foo(int a){
    a += 1;
    return a;
}

int foo(int* pa){
    *pa = *pa + 1;
    pa +=1;
    *pa = 999;
    return 0;
}
int main(int argc, char **argv){

    int num = 10;
    int *p = &num;

    cout << "num: " << num << endl;
    foo(num);
    cout << "num: " << num << endl;

    cout << "p: " << p << endl;
    foo(p);
    cout << "p: " << p << endl;
    cout << "p next content: " << *(p+1) << endl;
    cout << "num: " << num << endl;


    return 0;
}