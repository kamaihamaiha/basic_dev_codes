#include <stdio.h>
#include <stdlib.h>

void inputArray();

// 动态创建 size 个数元素的 int 数组
void createIntArray(int size);

int main(){

  int *pInt = NULL;
  pInt = (int*)malloc(sizeof(int));

  double *pDouble = NULL;
  pDouble = (double *) malloc(sizeof(int ));

  *pInt = 1;
  *pDouble = 1.1;
  printf("%d\n", *pInt);
  printf("%f\n", *pDouble);

  printf("请输入数组元素个数:");
  int size;
  scanf("%d", &size);
  createIntArray(size);
}

void createIntArray(int size) {
  int *arr = NULL;
  arr = (int*) malloc(sizeof(int) * size);
  if (arr == NULL) return;

  for (int i = 0; i < size; ++i) {
    arr[i] = i;
  }

  for (int i = 0; i < size; ++i) {
    printf("%d ", arr[i]);
  }

  // 释放空间
  free(arr);
  printf("\n");
}

void inputArray() {
  int n;
  int arr[20];
  printf("请输入要输入的数据个数：");
  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    printf("第%d个数:", i + 1);
    scanf("%d", &arr[i]);
  }

  // 计算最大的数
  int max = arr[0];
  for (int i = 1; i < n; ++i) {
    if (max < arr[i]) {
      max = arr[i];
    }
  }

  printf("其中最大的数为: %d\n", max);
}