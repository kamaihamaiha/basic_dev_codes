## const 关键字

[代码](../section_10/main.c)

### 禁止字符数组元素被修改
```c
const char str[] = "Hello\n";
// 或者这么写
char const str[] = "Hello\n";
```

### 修饰指针数据
```c
const char *pstr = "Hello\n";
// 或者这么写
char const *pstr = "Hello\n";
```

### 修饰指针
const 修饰的是 `*`，也就是指针`pstr` 不能再指向别的地方了
```c
char * const pstr = "Hello\n";
```

#### 助记

const 在 `*` 左边，修饰的是指针数据，在 `*` 右边修饰的是指针本身