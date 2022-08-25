#include <stdio.h>
#include "person.h"

Person newPerson(){

  Person p;
  printf("input name（No more than %d letters）:", MAX_NAME_LENGTH);
  scanf("%s", p.name);

  printf("input gender（1: male; 2: female）:");
  scanf("%d", &p.gender);

  printf("input height:");
  scanf("%lf", &p.height);

  printf("input weight:");
  scanf("%lf", &p.weight);

  return p;
}

/**
 * 显示人员信息，只作为显示用，因此用 const，只能读取，不能修改
 * @param p 用指针，为了传递参数时，节省传递的数据空间，只占用 sizeof(*Person) 大小：32位程序占用 4byte，64位程序占用 8byte
 */
void printPerson(const Person *p){
  printf("\nname\tgender\theight\tweight\n");
  printf("%s\t%d\t%lf\t%lf\t", p->name, p->gender, p->height, p->weight);
}