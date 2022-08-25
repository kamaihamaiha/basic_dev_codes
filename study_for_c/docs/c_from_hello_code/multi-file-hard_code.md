## 更复杂的多文件代码

[代码](../../c_from_hello_code/46_multi-file-hard_code/main.c)

- `#pragma once` 如果编译器支持的话，也能用这个放在头文件首位，防止重复引入。
    - 守卫头文件

### 条件编译和 `#pragma once` 对比

条件编译：
```c
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

```

`#pragma once`
```c
#pragma once

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
```