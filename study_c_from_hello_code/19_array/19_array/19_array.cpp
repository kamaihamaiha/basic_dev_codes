#include <stdio.h>
#include <memory.h>
// 19_array.cpp : 
// 两个数组如何复制元素数据
// 方法一：遍历，逐个元素复制
// 方法二：内存复制 memcpy 函数, 用 memory.h

int main()
{
    char c[2];

    // = 右边是：初始化列表
    int arr[4] = { 1, 2, 3, 4 };

    // 让初始化列表来决定数组的长度
    int arr2[] = { 1, 2, 3, 4, 5 };

    // copy 数组
    int arr3[5] = {}; // 初始化数组 arr3 5个元素初始值都为 0
    int arr4[5] = { 1, 2, 3, 4, 5 };

    memcpy(arr3, arr4, sizeof(arr3));

    for (int i = 0; i < 5; i++) {
        printf("%d ", arr3[i]);
    }


    return 0;
}

