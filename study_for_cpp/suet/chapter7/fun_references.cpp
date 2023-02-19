#include <iostream>

using namespace std;

int add(int, int);
int max(int, int);

// 初始化函数引用
int (&my_fun_add)(int, int) = add;
int (&my_fun_max)(int, int) = max;

int main(){

    cout << my_fun_add(1, 2) << endl;
    cout << my_fun_max(100, 2) << endl;


    return 0;
}

int add(int x, int y){
    return x + y;
}

int max(int x, int y){
    return x > y ? x : y;
}