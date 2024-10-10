#include <stdio.h>

int main()
{

    int arr[5] = {1, 2, 3, 4, 5};

    int *p = &arr[0];
    int *p2 = arr;

    printf("%d\n", *p);
    printf("%d\n", *(p + 1));
    printf("%d\n", *(p + 2));
    printf("%d\n", *(p + 3));
    printf("%d\n", *(p + 4));
    printf("%p\n", p);
    printf("%p\n", arr);
    printf("%p\n", &arr[0]);
    printf("第二个元素:%d\n", *(arr + 1));

    return 0;
}


