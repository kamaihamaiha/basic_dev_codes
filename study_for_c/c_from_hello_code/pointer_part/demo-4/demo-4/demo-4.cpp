#include <stdio.h>

void fun1();

void fun2();

int* fun3();

void fun4(int**, int**);

int main()
{
    // 多级指针示例
    fun1();
    fun2();

    int *p = fun3();
    printf("%d\n", *p);

    fun3();
    printf("%d\n", *p);

    fun3();
    printf("%d\n", *p);

    // 返回多个值
    int *a = NULL;
    int *b = NULL;

    fun4(&a, &b);
    // 打印 a b 的值
    if (a != NULL && b != NULL)
    {
        printf("a=%d b=%d\n", *a, *b);
    }
    

    return 0;
}

/**
 * 多级指针
 * 
 */
void fun1() {
    int n = 123;
    int *np = &n;

    printf("pn = %u\n", np);
    printf("&pn = %u\n", &np);
}

/**
 * 指针数组
 * 
 */
void fun2() {

    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5] = {11, 22, 33, 44, 55};
    int arr3[5] = {111, 222, 333, 444, 555};

    // 定义指针数组
    int *pToArr[3];
    pToArr[0] = arr1;
    pToArr[1] = arr2;
    pToArr[2] = arr3;

    for(int i = 0; i < 3; i++) {
        // 具体的某个数组的首地址
        int **p = pToArr + i;
        for(int j = 0; j < 5; j++) {
            // *P 就是某一个数组
            printf("%d ", *(*p + j));
        }
        printf("\n");
    }
}

int* fun3(){

    static int n = 1;
    n++;
    return &n;
}

void fun4(int **a, int **b){
    static int x = 100;
    static int y = 100;

    *a = &x;
    *b = &y;
}




