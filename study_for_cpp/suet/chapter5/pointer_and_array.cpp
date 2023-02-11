#include <iostream>
#include <stdio.h>

using namespace std;
struct Student {
    char name[4];
    int born;
    bool male;
};

int main(){

    Student stds[128];

    // 三个地址都是一样的
    printf("&stds = %p\n", &stds);
    printf("stds = %p\n", stds);
    printf("&stds[0] = %p\n", &stds[0]);

    return 0;
}