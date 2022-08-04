#include <stdio.h>

void swap(int *, int *);

void swap2(void*, void*, int size);

int main()
{
    int a = 1;
    int b = 2;

    printf("a=%d\n", a);
    printf("b=%d\n", b);

    swap2(&a, &b, sizeof(a));

    printf("a=%d\n", a);
    printf("b=%d\n", b);

    
    return 0;
}

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void swap2(void* x, void* y, int size) {
    char temp[128];
    char *xc = (char*)x;
    char *yc = (char*)y;

    for (size_t i = 0; i < size; i++)
    {
        temp[i] = xc[i];
    }
    
    for (size_t i = 0; i < size; i++)
    {
        xc[i] = yc[i];
    }

    for (size_t i = 0; i < size; i++)
    {
        yc[i] = temp[i];
    }

}
