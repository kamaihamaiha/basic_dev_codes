#include <iostream>
#include <stdlib.h>

using namespace std;

int sum(int a, int b);

int add(int a, int b);

// 定义函数指针
int (*sum_ptr)(int a, int b);

// 最后一个参数为：函数指针
void qsort(void *ptr, size_t count, size_t size, int(*comp)(const void*, const void*));

int main(){

    // 函数指针 sum_ptr 指向函数 sum()，第一种写法
    sum_ptr = sum;

    // 使用指针函数，第一种写法
    cout << sum_ptr(1, 99) << endl;

    // 函数指针 sum_ptr 指向函数 add()，第二种写法，用 &
    sum_ptr = &add;

    // 使用指针函数，第二种写法
    cout << (*sum_ptr)(10, 100) << endl;


    return 0;
}

int sum(int a, int b){
    return a + b;
}

int add(int a, int b){
    return a + b;
}