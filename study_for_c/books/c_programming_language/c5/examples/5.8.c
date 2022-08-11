#include <stdio.h>

char *month_name(int);
int main(){

  printf(month_name(0));

  return 0;
}

char *month_name(int n) {

  // 指针数组：里面的元素为字符指针
  static char *name[] = {
      "Illegal month",
      "January","February","March",
      "April","May","June",
      "July","August","September",
      "October","November","December"
  };

  return (n < 1 || n > 12) ? name[0] : name[n];
}