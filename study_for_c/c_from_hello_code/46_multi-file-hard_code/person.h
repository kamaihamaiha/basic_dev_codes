#ifndef STUDY_FOR_C_C_FROM_HELLO_CODE_46_MULTI_FILE_HARD_CODE_PERSON_H_
#define STUDY_FOR_C_C_FROM_HELLO_CODE_46_MULTI_FILE_HARD_CODE_PERSON_H_

#define MAX_NAME_LENGTH 20

typedef struct {
  // 姓名最长 20个字符
  char name[MAX_NAME_LENGTH + 1];
  int gender;
  double height;
  double weight;
}Person;

// 人员信息输入函数
Person newPerson();

// 显示人员信息
void printPerson(const Person *p);
#endif //STUDY_FOR_C_C_FROM_HELLO_CODE_46_MULTI_FILE_HARD_CODE_PERSON_H_
