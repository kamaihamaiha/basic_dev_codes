﻿// demo-1.cpp :

#include <stdio.h>

int main()
{
    
    char *pc;
    short *ps;
    int *pi;
    long *pl;
    long long *pll;
    float *pf;
    double *pd;

    // 先给指针赋值 100
    pc = (char*)100;
    ps = (short*)100;
    pi = (int*)100;
    pl = (long*)100;
    pll = (long long*)100;
    pf = (float*)100;
    pd = (double*)100;

    int *pInt = pi;

    pc = pc + 1;
    ps = ps + 1;
    pi = pi + 1;
    pl = pl + 1;
    pll = pll + 1;
    pf = pf + 1;
    pd = pd + 1;

    // print
    printf("pc=%u\n", pc);
    printf("ps=%u\n", ps);
    printf("pi=%u\n", pi);
    printf("pl=%u\n", pl);
    printf("pll=%u\n", pll);
    printf("pf=%u\n", pf);
    printf("pd=%u\n", pd);

    for(int i = 1; i <= 4; i ++) {
        printf("pInt + %d address is %u\n",i, pInt + i);
    }


    // 同类型指针减法运算
    int arr[10];
    printf("&arr[0] = %d\n", &arr[0]);
    printf("&arr[5] = %d\n", &arr[5]);
    printf("&arr[5] - &arr[0] = %d\n", &arr[5] - &arr[0]);
}

