#include <stdio.h>

// 结构体
int main(){

  struct {
    char name[20];
    int gender;
    double height;
    double weight;
  } arr[10];

  printf("请输入人员信息：姓名、性别、身高、体重\n");

  scanf("%s %d %lf %lf", arr[0].name, &arr[0].gender, &arr[0].height, &arr[0].weight);

  printf("%s,%d,%lf,%lf\n", arr[0].name, arr[0].gender, arr[0].height, arr[0].weight);
  return 0;
}