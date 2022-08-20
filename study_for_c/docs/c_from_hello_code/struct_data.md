## 结构化数据

### 简介

- 结构别名
- 结构初始化
- 定义结构数组
- 嵌套结构
- 指向结构指针
- 函数传递结构

- `struct`
- `->`: 成员间接运算符

### struct 使用

#### 结构变量
```c
// 声明结构变量
struct {
  char name[20];
  int gender;
  double height;
  double weight;
} timmy;

// 使用
timmy.name;
timmy.gender;
```

#### 结构声明（别名）
```c
struct person {
    char name[20];
    int gender;
    double height;
    double weight;
};

// 声明结构变量 david 和 jane
struct person david;
struct person jane;

```

#### 结构初始化
```c
struct person timmy = {"timmy", 1, 170.9, 220.3};
```

#### 结构数组
```c
struct person people[] = {
    {"timmy", 1, 170.9, 220.3},
    {"davie", 1, 171.9, 221.3},
    {"jane", 1, 172.9, 222.3},
};
```

#### 嵌套结构

```c
// struct 通讯方式
struct contact {
  char phone[20];
  char email[20];
};

// struct 人，成员包含了 struct contact
struct person {
    char name[20];
    int gender;
    double height;
    double weight;
    struct contact c;
};
```

#### 指向结构的指针

```c
struct person timmy = {"timmy", 1, 170.9, 220.3};
struct person *pTimmy = &timmy;

// 使用结构体的指针访问结构的成员
(*pTimmy).name;
// 或者使用成员间接运算符: ->
pTimmy->name;
```

#### 结构在函数中传递

要用指针