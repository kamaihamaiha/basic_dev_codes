#include <iostream>

typedef int myint;

typedef unsigned char vec3b[3]; // 代表：unsigned char 类型的 3个元素的数组

typedef struct _rgb_struct {
    unsigned char r;
    unsigned char g;
    unsigned char b;

} rgb_struct;

int main(){

    // 使用上面定义的 typedef
    myint num = 1;

    vec3b color = {123, 100, 200};

    rgb_struct rgb = {0, 200, 139};

    return 0;
}